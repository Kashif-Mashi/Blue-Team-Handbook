# Lab 03 — CMD & PowerShell Investigation

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 04 (CMD) and Chapter 05 (PowerShell Fundamentals).  
**Objectives**:
- Perform system enumeration using native CMD and PowerShell utilities.
- Analyze running processes and identify network connections.
- Collect volatile diagnostic data using CLI redirection and piping.
- Query Windows event logs for suspicious command execution indicators.

---

## Scenario

You have joined the SOC team as a Tier 1 Analyst. A security alert indicates suspicious activities on workstation `DESKTOP-TRIAGE`. An unverified command-line process was launched by an endpoint user.

Your supervisor has tasked you with investigating the endpoint using Command Prompt and PowerShell to gather host information, identify active processes, inspect network connections, and record findings into a triage summary report.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: `cmd.exe`, `powershell.exe`

---

## Tasks

### Task 1: Initialize Command Prompt Context
Open Command Prompt as Administrator and verify your privilege level.

### Task 2: Host System Enumeration via CMD
Run `systeminfo` and export the detailed system output to `C:\Users\Public\HostInfo.txt`.

### Task 3: Current Identity & Privilege Audit
Use `whoami /all` to list your account SID, group memberships, and assigned user privileges.

### Task 4: Active Process Inspection via CMD
Use `tasklist /svc` to view all running processes along with their associated services.

### Task 5: Filter Suspicious Network Connections
Execute `netstat -ano` and filter the results using `findstr` to display all connections with state `ESTABLISHED`.

### Task 6: Network Interface Configuration
Use `ipconfig /all` to record the IPv4 address, subnet mask, default gateway, and DNS servers.

### Task 7: Directory Navigation & File Search
Navigate to `C:\Windows\System32\drivers\etc` and display the contents of the `hosts` file using `type`.

### Task 8: Environment Variable Inspection
Display all currently set system environment variables using `set` and locate `%TEMP%`.

### Task 9: Initialize PowerShell Session
Launch an elevated PowerShell session (`powershell.exe`).

### Task 10: Query Running Services via PowerShell
Use `Get-Service` to list all services currently in the `Running` state.

### Task 11: High Memory Process Identification
Use PowerShell pipeline filtering (`Get-Process | Where-Object ...`) to list all processes using over 50MB of Working Set memory.

### Task 12: Select & Export Custom Process Attributes
Export the `ProcessName`, `Id`, and `Path` of all active processes to a CSV file at `C:\Users\Public\ProcessReport.csv` using `Export-Csv`.

### Task 13: Query Event Logs for Process Creation
Use `Get-WinEvent` to query the `Security` log for recent process creation events (Event ID 4688) or `System` log errors.

### Task 14: Inspect PowerShell Execution Policy
Check the local PowerShell execution policy using `Get-ExecutionPolicy -List`.

### Task 15: Create an Automated Triage Script
Write a basic `.ps1` script that collects host computer name, logged-in user, and active network connections into `C:\Users\Public\Triage.txt`.

---

## Verification

To verify success:
- Verify `C:\Users\Public\HostInfo.txt` exists and contains full `systeminfo` output.
- Verify `C:\Users\Public\ProcessReport.csv` contains process details in valid CSV format.
- Verify `C:\Users\Public\Triage.txt` contains automated script output.

---

## Blue Team Notes

- **Command Line Auditing**: Adversaries frequently execute host discovery commands within seconds of initial access. Automating triage via PowerShell scripts enables rapid incident response.
- **Process vs Network Correlation**: Matching `netstat -ano` PIDs to `tasklist` processes allows analysts to trace network callbacks back to specific binaries on disk.

---

## Common Errors

- **Access Denied on Logs**: Running `Get-WinEvent -LogName Security` in non-elevated PowerShell triggers permission errors. Ensure shell is launched as Administrator.
- **Overwriting Log Data**: Accidentally using `>` instead of `>>` when appending data.

---

## MITRE ATT&CK Mapping

- **T1059.001**: Command and Scripting Interpreter: PowerShell
- **T1059.003**: Command and Scripting Interpreter: Windows Command Shell
- **T1082**: System Information Discovery
- **T1057**: Process Discovery
- **T1049**: System Network Connections Discovery

---

## Challenge Section

1. Write a single PowerShell one-liner that retrieves all running processes and sorts them by CPU usage in descending order.
2. Use `Get-WinEvent` to find all events logged by source `Microsoft-Windows-PowerShell` in the last 24 hours.
3. Pipe `netstat -ano` into `findstr` to identify any process listening on port `445` (SMB).
4. Create a hash table in PowerShell containing key workstation metadata and convert it to JSON format using `ConvertTo-Json`.
5. Identify any running process whose file path resides outside `C:\Windows` or `C:\Program Files`.
