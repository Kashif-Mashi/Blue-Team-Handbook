# Solution — Lab 03: CMD & PowerShell Investigation

> This solution guide walks you through the GUI-locked ransomware precursor scenario, demonstrating how to use CMD and PowerShell to extract forensic host data and identify malicious activity.

---

# Task 1 — Initialize and Verify Context

## Steps

Open Command Prompt as Administrator. Verify your security privileges.

```cmd
whoami /all
```

### Investigation Note
If you are investigating a ransomware alert, you must ensure you have `High Integrity` (Administrator) access. The `whoami /all` command reveals your SID, group memberships (e.g., `BUILTIN\Administrators`), and critical privileges like `SeDebugPrivilege`, which allows you to inspect other processes memory.

---

# Task 2 — Snapshot the Host (CMD)

## Steps

Redirect the system configuration output to a text file for evidence preservation.

```cmd
systeminfo > C:\Users\Public\HostInfo.txt
```

### Investigation Note
Using `>` creates (or overwrites) the file. Capturing the OS version, patch level, and system boot time is vital to determine if the ransomware exploited a missing patch.

---

# Task 3 — Uncover Active Processes (CMD)

## Steps

List all running processes and their associated services.

```cmd
tasklist /svc
```

### Investigation Note
Look for anomalous process names (e.g., `1saas.exe` instead of `lsass.exe`) or binaries running out of unexpected directories like `C:\Users\Public` or `AppData\Local\Temp`.

---

# Task 4 — Trace Network Callbacks (CMD)

## Steps

Identify active Command and Control (C2) connections.

```cmd
netstat -ano | findstr "ESTABLISHED"
```

### Investigation Note
By filtering for `ESTABLISHED`, you ignore listening ports and focus strictly on active, two-way communication. If you spot a suspicious external IP address, note the PID in the far-right column. You can then cross-reference that PID with your `tasklist` output to find the exact malware executable.

---

# Task 5 — Identify Network Interfaces

## Steps

Record the network configuration.

```cmd
ipconfig /all
```

### Investigation Note
You must collect the IPv4 address of the infected host so you can pass it to the network security team. They will use this IP to isolate the host at the firewall/switch level and prevent the ransomware from spreading laterally.

---

# Task 6 — Transition to PowerShell

## Steps

Launch PowerShell and check the execution policy.

```cmd
powershell.exe
Get-ExecutionPolicy -List
```

### Investigation Note
PowerShell is far more powerful for filtering data. Checking the execution policy lets you know if scripts are restricted on this endpoint, though you should remember this can easily be bypassed by an attacker using `powershell -ExecutionPolicy Bypass`.

---

# Task 7 — PowerShell Process Hunting

## Steps

Find resource-heavy processes. Ransomware encryption consumes high CPU and Memory.

```powershell
Get-Process | Where-Object { $_.WorkingSet -gt 50MB }
```

### Investigation Note
Because PowerShell processes data as `.NET Objects`, filtering by `WorkingSet` (memory usage) is a simple numerical comparison (`-gt` means greater than), completely removing the need for complex string parsing (regex).

---

# Task 8 — Extract Custom Process Attributes

## Steps

Select specific process properties and export them to a CSV report.

```powershell
Get-Process | Select-Object ProcessName, Id, Path | Export-Csv -Path C:\Users\Public\ProcessReport.csv -NoTypeInformation
```

### Investigation Note
The `Path` property is incredibly useful. Legitimate Windows processes run from `C:\Windows\System32`. If your CSV shows an unknown process running from `C:\Users\Analyst\Downloads`, it is highly suspect.

---

# Task 9 — Query Event Logs

## Steps

Query the Security log for process creation events.

```powershell
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4688 } | Select-Object -First 10
```

*(Note: Process Creation Auditing must be enabled via Group Policy for Event ID 4688 to populate.)*

### Investigation Note
Event ID 4688 logs exactly when a process started and its command-line arguments. This is how you discover how the malware was originally launched (e.g., via a malicious Word macro spawning CMD).

---

# Task 10 — Automate the Triage

## Steps

Write a simple one-liner to automate data collection.

```powershell
"Host: $env:COMPUTERNAME" > C:\Users\Public\Triage.txt; "User: $env:USERNAME" >> C:\Users\Public\Triage.txt; netstat -ano | findstr "ESTABLISHED" >> C:\Users\Public\Triage.txt
```

### Investigation Note
By using `>>` instead of `>`, you append data to the `Triage.txt` file without overwriting the previous lines. Automating these steps allows SOC analysts to execute rapid triage across hundreds of endpoints simultaneously during a major incident.

---

# Scenario Conclusion

By effectively wielding both CMD and PowerShell, you successfully circumvented the GUI lockout, identified the suspicious processes consuming system resources, and mapped their outbound C2 connections—providing the critical intelligence needed to contain the ransomware attack.
