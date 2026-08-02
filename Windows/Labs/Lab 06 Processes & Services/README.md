# Lab 06 — Processes & Services Investigation

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 08 (Windows Processes & Services).  
**Objectives**:
- Enumerate running processes, Process IDs (PIDs), and Parent Process IDs (PPIDs).
- Map active Windows services to host `svchost.exe` process instances.
- Inspect service startup states and create a test service using `sc.exe`.
- Detect process masquerading and abnormal parent-child relationships.
- Analyze Process Creation Events (Event ID 4688 / Sysmon Event ID 1) and Service Creation Events (Event ID 7045).

---

## Scenario

The Security Operations Center (SOC) detected a suspicious background process executing on endpoint `WORKSTATION-02`. An alert suggests an unverified service was created to establish persistence.

As an Incident Responder, your objective is to perform process lineage analysis, identify running service instances, inspect service configurations, create and verify a controlled lab service, track service creation event logs, and report your triage findings.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: `tasklist.exe`, `sc.exe`, `wmic.exe`, `powershell.exe`, Event Viewer (`eventvwr.msc`)

---

## Tasks

### Task 1: Basic Process Enumeration via CMD
Open an elevated Command Prompt and run `tasklist` to record all active running processes.

### Task 2: Service-to-Process Mapping
Run `tasklist /svc` and identify all service names hosted under `svchost.exe` instances.

### Task 3: Process Lineage Inspection via WMI
Execute `wmic process get Name, ProcessId, ParentProcessId, ExecutablePath` to map process parent-child relationships.

### Task 4: High Memory Process Analysis via PowerShell
Open elevated PowerShell and run `Get-Process | Where-Object {$_.WorkingSet -gt 50MB} | Sort-Object WorkingSet -Descending` to identify heavy memory consumers.

### Task 5: Parent Process Command Line Extraction
Use PowerShell (`Get-CimInstance Win32_Process`) to extract the full `CommandLine` and `ParentProcessId` for `cmd.exe` or `powershell.exe`.

### Task 6: Audit Service States via `sc.exe`
Run `sc query` to view all active background services.

### Task 7: Target Service State Detailed Query
Query the status of the Windows Defender service using `sc query WinDefend`.

### Task 8: Create a Custom Background Test Service
Create a temporary background service named `TriageAgent` using `sc create TriageAgent binPath= "C:\Windows\System32\notepad.exe" start= auto`.

### Task 9: Query Custom Service Configuration
Run `sc qc TriageAgent` to view binary path, start type, and account context.

### Task 10: Modify Service Startup Type
Change the startup type of `TriageAgent` to disabled using `sc config TriageAgent start= disabled`.

### Task 11: Attempt Service Execution
Attempt to start the service using `net start TriageAgent` and document the expected failure.

### Task 12: Delete Custom Test Service
Delete `TriageAgent` service using `sc delete TriageAgent`.

### Task 13: Audit Service Installation Event Logs
Open Event Viewer (`eventvwr.msc`), navigate to `Windows Logs -> System`, and filter for Event ID **7045** (A service was installed in the system).

### Task 14: Inspect Process Creation Audit Logs
Navigate to `Windows Logs -> Security` and filter for Event ID **4688** (Process Creation) to inspect process launch arguments.

### Task 15: Clean Up Lab Artifacts
Verify `TriageAgent` is removed from system service listings using `sc query TriageAgent`.

---

## Verification

To verify success:
- Confirm `sc qc TriageAgent` displayed `START_TYPE: 4 DISABLED` before deletion.
- Confirm Event ID 7045 in the System log records the creation of `TriageAgent`.
- Confirm `sc query TriageAgent` returns `[SC] OpenService FAILED 1060` after deletion.

---

## Blue Team Notes

- **Service Persistence Detection**: Event ID 7045 is one of the highest-fidelity indicators for service-based persistence. SOC rules should alert on any new service created with binary paths pointing to `C:\Users\Public`, `C:\Temp`, or `%APPDATA%`.
- **Process Masquerading**: Attackers often name malicious binaries `svchost.exe` or `lsass.exe`. Legitimate `svchost.exe` instances MUST run out of `C:\Windows\System32\` and have `services.exe` as their parent PID.

---

## Common Errors

- **Forgetting Space After Equals in `sc`**: Running `sc create SvcName binPath="C:\path"` fails. `sc.exe` REQUIRES a space after equal signs (`binPath= "C:\path"`).
- **Non-Elevated Prompt**: Service creation commands fail with "Access is denied" if CMD/PowerShell is not launched as Administrator.

---

## MITRE ATT&CK Mapping

- **T1569.002**: System Services: Service Execution
- **T1057**: Process Discovery
- **T1036.005**: Masquerading: Match Legitimate Name or Location

---

## Challenge Section

1. Write a PowerShell script that inspects all running `svchost.exe` processes and flags any instance executing outside `C:\Windows\System32`.
2. Query Event ID **7045** using `Get-WinEvent` and parse out the Service Name and Image Path.
3. Identify all unquoted service paths on your system using `wmic service get name,displayname,pathname,startmode | findstr /i /v "c:\windows\\" | findstr /i /v """`.
4. Use `Get-Process` to list processes with no associated file path on disk (potential memory injection indicator).
5. Compare process listings between `tasklist` and Sysinternals `Process Explorer` to spot hidden processes.


---

# Solution

➡ **[View Solution](../Solution/Lab%2006%20Solution.md)**
