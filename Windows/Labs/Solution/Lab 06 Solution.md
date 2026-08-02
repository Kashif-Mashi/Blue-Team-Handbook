# Lab 06 Solution — Processes & Services Investigation

## Solution

---

### Task 1: Basic Process Enumeration via CMD

#### Step-by-Step Instructions
1. Open Command Prompt as Administrator.
2. Execute `tasklist`.

#### Expected Output
```cmd
Image Name                   PID Session Name        Session#    Mem Usage
========================= ====== ================ ======== ============
System Idle Process            0 Services                0          8 K
System                         4 Services                0        156 K
smss.exe                     412 Services                0      1,024 K
csrss.exe                    528 Services                0      4,210 K
wininit.exe                  612 Services                0      3,840 K
services.exe                 688 Services                0      8,450 K
lsass.exe                    700 Services                0     14,200 K
cmd.exe                     4820 Console                 1      5,120 K
```

#### Explanation
`tasklist` displays image name, PID, session type, and RAM usage for all active processes on the host.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Service-to-Process Mapping

#### Step-by-Step Instructions
1. Run `tasklist /svc` in CMD.

#### Expected Output
```cmd
Image Name                   PID Services
========================= ====== ============================================
svchost.exe                  812 DcomLaunch, PlugPlay, Power
svchost.exe                  940 RpcSs, RpcEptMapper
svchost.exe                 1240 EventLog
svchost.exe                 1520 WinDefend
```

#### Explanation
Maps generic `svchost.exe` process instances to specific Windows service names hosted inside each process.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Process Lineage Inspection via WMI

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
wmic process get Name, ProcessId, ParentProcessId, ExecutablePath
```

#### Expected Output
```text
ExecutablePath                           Name            ParentProcessId  ProcessId
C:\Windows\System32\smss.exe             smss.exe        4                412
C:\Windows\System32\wininit.exe          wininit.exe     412              612
C:\Windows\System32\services.exe         services.exe    612              688
C:\Windows\System32\cmd.exe              cmd.exe         2140             4820
```

#### Explanation
Lineage tracking allows analysts to verify if child processes were spawned by legitimate parent processes (e.g. `services.exe` -> `svchost.exe`).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: High Memory Process Analysis via PowerShell

#### Step-by-Step Instructions
1. Open PowerShell as Administrator.
2. Run:
```powershell
Get-Process | Where-Object {$_.WorkingSet -gt 50MB} | Sort-Object WorkingSet -Descending
```

#### Expected Output
```text
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
   1420      92   210400     285000      15.20   3412   1 msedge
    890      45    98200     125400       5.10   2140   1 explorer
```

#### Explanation
Filters objects based on WorkingSet RAM usage exceeding 50MB and sorts in descending order.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Parent Process Command Line Extraction

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-CimInstance Win32_Process -Filter "Name = 'cmd.exe'" | Select-Object ProcessId, ParentProcessId, CommandLine
```

#### Expected Output
```text
ProcessId ParentProcessId CommandLine
--------- --------------- -----------
     4820            2140 "C:\Windows\System32\cmd.exe"
```

#### Explanation
Queries WMI CIM class `Win32_Process` to extract executable parameters and parent process IDs.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Audit Service States via `sc.exe`

#### Step-by-Step Instructions
1. Run `sc query` in CMD.

#### Expected Output
```cmd
SERVICE_NAME: Appinfo
DISPLAY_NAME: Application Information
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
```

#### Explanation
`sc query` enumerates active service objects and their operational states.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Target Service State Detailed Query

#### Step-by-Step Instructions
1. Run `sc query WinDefend`.

#### Expected Output
```cmd
SERVICE_NAME: WinDefend
DISPLAY_NAME: Microsoft Defender Antivirus Service
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
```

#### Explanation
Queries the status of the Windows Defender service to verify system protection state.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Create a Custom Background Test Service

#### Step-by-Step Instructions
1. Run in elevated CMD:
```cmd
sc create TriageAgent binPath= "C:\Windows\System32\notepad.exe" start= auto
```

#### Expected Output
```cmd
[SC] CreateService SUCCESS
```

#### Explanation
Registers a new background service named `TriageAgent` pointing to `notepad.exe` in the SCM database.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Query Custom Service Configuration

#### Step-by-Step Instructions
1. Run `sc qc TriageAgent`.

#### Expected Output
```cmd
SERVICE_NAME: TriageAgent
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Windows\System32\notepad.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : TriageAgent
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

#### Explanation
`sc qc` (Query Config) displays startup type, binary path, and user execution context (`LocalSystem`).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Modify Service Startup Type

#### Step-by-Step Instructions
1. Run `sc config TriageAgent start= disabled`.

#### Expected Output
```cmd
[SC] ChangeServiceConfig SUCCESS
```

#### Explanation
Reconfigures the service startup parameter to `DISABLED` (Start Type 4).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: Attempt Service Execution

#### Step-by-Step Instructions
1. Run `net start TriageAgent`.

#### Expected Output
```cmd
System error 1058 has occurred.

The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.
```

#### Explanation
Confirms that disabled services cannot be started by standard execution requests.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Delete Custom Test Service

#### Step-by-Step Instructions
1. Run `sc delete TriageAgent`.

#### Expected Output
```cmd
[SC] DeleteService SUCCESS
```

#### Explanation
Removes the service entry from the SCM registry database.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Audit Service Installation Event Logs

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -LogName "System" | Where-Object {$_.Id -eq 7045} | Select-Object -First 1 | Format-List
```

#### Expected Output
```text
TimeCreated  : 8/2/2026 11:00:15 AM
ProviderName : Service Control Manager
Id           : 7045
Message      : A service was installed in the system.

               Service Name:  TriageAgent
               Service File Name:  C:\Windows\System32\notepad.exe
               Service Type:  user mode service
               Service Start Type:  auto start
               Account Name:  LocalSystem
```

#### Explanation
Event ID 7045 records the installation timestamp, binary file name, and account context of created services.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Inspect Process Creation Audit Logs

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -LogName "Security" | Where-Object {$_.Id -eq 4688} | Select-Object -First 1 | Format-List
```

#### Expected Output
```text
TimeCreated  : 8/2/2026 11:02:00 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4688
Message      : A new process has been created.

               New Process ID:    0x12d4
               New Process Name:  C:\Windows\System32\sc.exe
               CommandLine:       sc delete TriageAgent
```

#### Explanation
Event ID 4688 captures the process creation and executed command line switches.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Clean Up Lab Artifacts

#### Step-by-Step Instructions
1. Run `sc query TriageAgent`.

#### Expected Output
```cmd
[SC] EnumQueryServicesStatus:OpenService FAILED 1060:

The specified service does not exist as an installed service.
```

#### Explanation
Verifies complete removal of test service artifacts from the operating system.

---

### Screenshot

> **Insert Screenshot Here**

---
