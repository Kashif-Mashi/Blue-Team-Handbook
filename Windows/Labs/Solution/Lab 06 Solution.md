# Solution — Lab 06: Windows Processes & Services

> This solution guide walks you through the Cryptominer/Backdoor Hunt scenario, demonstrating how to identify rogue processes, trace parent-child lineage, and eradicate service-based persistence.

---

# Task 1 — Simulate the Compromise

## Steps

Open Command Prompt as Administrator and create the simulated malicious service.

```cmd
sc create UpdaterSvc binPath= "cmd.exe /c start /B C:\Windows\System32\notepad.exe"
net start UpdaterSvc
```

### Investigation Note
The `sc create` command registers a new Windows service with the Service Control Manager (SCM). The `binPath=` parameter tells the SCM what binary to execute when the service starts. In this simulation, we're using `notepad.exe` as a safe stand-in for actual malware. In the real world, this would be a cryptominer binary or a reverse shell payload.

---

# Task 2 — The Initial Hunt (CLI)

## Steps

Locate the running process.

```cmd
tasklist | findstr notepad
```

### Example Output

```
notepad.exe                  7284 Console                    1     12,340 K
```

### Investigation Note
The PID `7284` (your number will differ) is our target. Note this number for the next steps. The `tasklist` command is often the first tool a responder reaches for during live triage.

---

# Task 3 — Identify the Parent Process

## Steps

Use WMI to trace who spawned this process.

```cmd
wmic process where processid=7284 get name,processid,parentprocessid
```

### Example Output

```
Name          ParentProcessId  ProcessId
notepad.exe   6512             7284
```

### Investigation Note
The Parent Process ID (PPID) is `6512`. This is the process that launched our "malware." We need to identify what process `6512` is.

---

# Task 4 — Trace the Lineage

## Steps

Look up the parent process.

```cmd
tasklist /fi "PID eq 6512"
```

### Example Output

```
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
cmd.exe                      6512 Services                   0      4,108 K
```

### Investigation Note
The parent is `cmd.exe` running in Session `0` (the services session). This is a red flag! Legitimate `notepad.exe` is typically launched by `explorer.exe` (Session 1, the user's desktop). A `notepad.exe` spawned by `cmd.exe` in Session 0 means it was launched by a Windows service — exactly the persistence mechanism the attacker planted.

---

# Task 5 — Sysinternals Deep Dive

## Steps

1. Launch `procexp.exe` (Process Explorer) as Administrator.
2. In the process tree, locate `notepad.exe`.
3. Right-click → **Properties** → **Image** tab.

### Investigation Note
In the Image tab, observe:
- **Path**: Should be `C:\Windows\System32\notepad.exe` (the binary itself is legitimate, but the *context* of how it was launched is not).
- **Parent**: `cmd.exe` — this confirms our CLI findings.
- **Current directory**: May show `C:\Windows\System32` or the service working directory.

Process Explorer also lets you check the **Verified Signer** to see if a binary is digitally signed by Microsoft. Malware binaries impersonating `svchost.exe` will NOT have a valid Microsoft signature.

---

# Task 6 — Link the Process to the Persistence Mechanism

## Steps

Map running processes to hosted services.

```cmd
tasklist /svc
```

Or use PowerShell for more targeted analysis:

```powershell
Get-WmiObject win32_service | Where-Object {$_.Name -eq 'UpdaterSvc'} | Select-Object Name, State, StartMode, PathName, ProcessId
```

### Example Output

```
Name        : UpdaterSvc
State       : Running
StartMode   : Auto
PathName    : cmd.exe /c start /B C:\Windows\System32\notepad.exe
ProcessId   : 6512
```

### Investigation Note
We have confirmed the link: `UpdaterSvc` is the service responsible for launching the rogue process, and the `PathName` reveals the full attacker command line.

---

# Task 7 — Investigate the Rogue Service

## Steps

Query the service configuration.

```cmd
sc query UpdaterSvc
sc qc UpdaterSvc
```

### Example Output (`sc qc`)

```
[SC] QueryServiceConfig SUCCESS
SERVICE_NAME: UpdaterSvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        BINARY_PATH_NAME   : cmd.exe /c start /B C:\Windows\System32\notepad.exe
        ...
```

### Investigation Note
The `BINARY_PATH_NAME` is the smoking gun. No legitimate Windows service would use `cmd.exe /c start /B` as its binary path. This is a clear indicator of a manually planted backdoor service.

---

# Task 8 — Stop the Bleeding

## Steps

Terminate the malicious process.

```cmd
taskkill /F /PID 7284
```

### Investigation Note
The `/F` flag forces the termination. Without it, the process might not respond to a graceful shutdown request. Always use `/F` when killing suspected malware.

---

# Task 9 — Eradicate the Persistence

## Steps

Delete the malicious service.

```cmd
sc delete UpdaterSvc
```

### Expected Output

```
[SC] DeleteService SUCCESS
```

### Investigation Note
Deleting the service removes the entry from the Service Control Manager. The malware will NOT restart on the next reboot. In a real incident, you would also:
1. Check for additional persistence (Registry Run keys, Scheduled Tasks).
2. Collect forensic evidence (memory dump, disk image) before cleanup.
3. Submit the malware sample to VirusTotal or your internal sandbox.

---

# Scenario Conclusion

By tracing the process lineage from `notepad.exe` → `cmd.exe` → `UpdaterSvc`, you successfully identified a service-based persistence mechanism. You terminated the active threat and eradicated the persistence by deleting the malicious service from the SCM. In a production environment, this same workflow applies when hunting real cryptominers, RATs, and backdoor implants.
