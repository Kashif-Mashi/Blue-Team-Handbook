# Lab 08 — Windows Event Viewer & Log Analysis

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 10 / Concepts (Windows Event Viewer & Logging).  
**Objectives**:
- Navigate Windows Event Viewer (`eventvwr.msc`) and inspect standard log channels.
- Filter, query, and export Windows Event Logs to `.evtx` and `.csv` formats.
- Enable Process Command-Line Auditing via Local Security Policy (`secpol.msc`).
- Query Security, System, and Sysmon event logs using PowerShell `Get-WinEvent`.
- Analyze critical security Event IDs (4624, 4625, 4688, 4720, 7045, 1102).

---

## Scenario

A security incident alert was triggered on workstation `WORKSTATION-04`. An unauthorized account logon was reported, followed by suspected command execution and audit log tampering attempts.

As a SOC Security Analyst, you are tasked with investigating the endpoint's Windows Event Logs, configuring audit policies to capture full command-line parameters, querying logon failures and process executions via PowerShell, and extracting security event indicators for your incident report.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: Event Viewer (`eventvwr.msc`), Local Security Policy (`secpol.msc`), PowerShell (`Get-WinEvent`)

---

## Tasks

### Task 1: Launch Event Viewer Interface
Press `Win + R`, type `eventvwr.msc`, and launch Event Viewer as Administrator.

### Task 2: Explore Standard Windows Logs
Expand **Windows Logs** and inspect the total record count and log size for `Application`, `Security`, and `System`.

### Task 3: Filter Security Log for Successful Logons
Apply an Event Viewer filter on the `Security` log for Event ID **4624** (Successful Logon).

### Task 4: Filter Security Log for Failed Logons
Apply a filter for Event ID **4625** (Failed Logon) and inspect logon types (e.g. Type 2 Interactive, Type 3 Network, Type 10 RemoteDesktop).

### Task 5: Enable Command-Line Auditing via Local Security Policy
Open `secpol.msc`, navigate to `Local Policies -> Audit Policy`, enable **Audit Process Creation** (Success and Failure), and enable **Include command line in process creation events** under Administrative Templates.

### Task 6: Trigger Test Command Execution
Open CMD and run `whoami /priv` and `netstat -ano > C:\Users\Public\test.txt` to generate audit events.

### Task 7: Query Process Creation Events via PowerShell
Open elevated PowerShell and run `Get-WinEvent -LogName "Security" -MaxEvents 10 | Where-Object {$_.Id -eq 4688}`.

### Task 8: Extract Command-Line Arguments via PowerShell
Execute a PowerShell script using `Get-WinEvent` to extract `ProcessName` and `CommandLine` from Event ID 4688 payloads.

### Task 9: Query System Log for Service Creation
Query the `System` log for Event ID **7045** using `Get-WinEvent -LogName "System" | Where-Object {$_.Id -eq 7045}`.

### Task 10: Query Application Log for Errors
Query the `Application` log for `Error` level events occurring within the past 24 hours.

### Task 11: Export Event Log to `.evtx` File
Export the filtered `Security` log to `C:\Users\Public\SecurityLog_Export.evtx` using `Get-WinEvent` or Event Viewer export options.

### Task 12: Query Sysmon Operational Log (If Installed)
Query `Microsoft-Windows-Sysmon/Operational` for Event ID **1** (Process Creation) or Event ID **3** (Network Connection).

### Task 13: Detect Audit Log Clearing (Event ID 1102)
Explain the significance of Event ID **1102** (The audit log was cleared) and test log clearance detection rules.

### Task 14: Convert Event Log Records to CSV
Export the latest 20 Security events to `C:\Users\Public\Security_Events.csv` using `Export-Csv`.

### Task 15: Clean Up Lab Artifacts
Remove `C:\Users\Public\test.txt` and exported `.evtx`/`.csv` files.

---

## Verification

To verify success:
- Confirm Event ID 4688 captures the full command line `whoami /priv` in the Event Data.
- Confirm `C:\Users\Public\Security_Events.csv` is created and populated with event objects.
- Confirm `secpol.msc` shows Audit Process Creation set to Success/Failure.

---

## Blue Team Notes

- **Command-Line Logging Visibility**: Without enabling "Include command line in process creation events" in GPO/secpol, Event ID 4688 records the binary name but leaves the `CommandLine` field blank, hiding attacker switches (`-EncodedCommand`, `Bypass`).
- **Log Clearance Indicators**: Event ID 1102 (Security log cleared) or Event ID 104 (System log cleared) indicates active adversary defense evasion. High-severity alerts must trigger immediately upon log clearance.

---

## Common Errors

- **Permission Denied on Security Log**: Non-elevated PowerShell windows return "Access is denied" when querying `Security` log channels. Ensure shell is run as Administrator.
- **Log Overwrite / Small Log Size**: Default log size limits (e.g. 20MB) cause old events to be overwritten quickly on busy hosts.

---

## MITRE ATT&CK Mapping

- **T1070.001**: Indicator Removal on Host: Clear Windows Event Logs
- **T1059.001**: Command and Scripting Interpreter: PowerShell
- **T1059.003**: Command and Scripting Interpreter: Windows Command Shell

---

## Challenge Section

1. Write an advanced PowerShell XPath filter query to retrieve all Event ID **4625** events where `LogonType` equals 10 (Remote Desktop).
2. Create a PowerShell script that parses Event ID **4720** (User Account Created) and outputs Creator Username, Target Username, and Time.
3. Query Event ID **4670** (Permissions on an object were changed) to identify ACL modifications.
4. Calculate the average number of logon events per hour on the machine using `Group-Object`.
5. Export Sysmon Event ID **1** records to a JSON file using `ConvertTo-Json`.
