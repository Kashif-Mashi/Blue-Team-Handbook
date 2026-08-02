# Lab 08 Solution — Windows Event Viewer & Log Analysis

## Solution

---

### Task 1: Launch Event Viewer Interface

#### Step-by-Step Instructions
1. Press `Win + R`, type `eventvwr.msc`, and press **Enter**.
2. Alternatively, right-click Start Menu and select **Event Viewer**.

#### Expected Output
Event Viewer MMC console window opens displaying Local Event Logs.

#### Explanation
Launches the built-in Microsoft Management Console snap-in for inspecting Windows event channels.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Explore Standard Windows Logs

#### Step-by-Step Instructions
1. Expand **Windows Logs** in the left navigation pane.
2. Select `Application`, `Security`, and `System` to view record counts.

#### Expected Output
```text
Log Name: Security
Number of Events: 12,450
Enabled: True
Size: 20.0 MB
```

#### Explanation
Provides an overview of log channel sizes and current event volume across host subsystems.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Filter Security Log for Successful Logons

#### Step-by-Step Instructions
1. Click **Filter Current Log...** in the right Actions pane.
2. Enter `4624` in the `<All Event IDs>` box and click **OK**.

#### Expected Output
```text
Event 4624, Security-Auditing
An account was successfully logged on.
Subject: User SID S-1-5-18 (SYSTEM)
Target User: admin (S-1-5-21-...-1001)
Logon Type: 2 (Interactive)
```

#### Explanation
Event ID 4624 logs user logons. Logon Type 2 indicates interactive physical keyboard logons.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Filter Security Log for Failed Logons

#### Step-by-Step Instructions
1. Click **Filter Current Log...** and set Event ID filter to `4625`.

#### Expected Output
```text
Event 4625, Security-Auditing
An account failed to log on.
Target Account: UnknownUser
Failure Reason: Unknown user name or bad password.
Status: 0xC000006D
Sub Status: 0xC000006A
Logon Type: 3 (Network)
```

#### Explanation
Event ID 4625 captures failed authentication attempts. Sub Status `0xC000006A` indicates correct username but incorrect password.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Enable Command-Line Auditing via Local Security Policy

#### Step-by-Step Instructions
1. Press `Win + R`, type `secpol.msc`, and press **Enter**.
2. Navigate to `Local Policies -> Audit Policy -> Audit process creation` and set to **Success and Failure**.
3. Open `gpedit.msc` or registry to enable "Include command line in process creation events".

#### Expected Output
```text
Local Security Policy updated. Process creation auditing enabled.
```

#### Explanation
Enables command line string capturing inside process creation event payloads.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Trigger Test Command Execution

#### Step-by-Step Instructions
1. Open CMD as Administrator.
2. Execute:
```cmd
whoami /priv
netstat -ano > C:\Users\Public\test.txt
```

#### Expected Output
```cmd
PRIVILEGES INFORMATION
----------------------
Privilege Name                  Description                         State
=============================== =================================== ========
SeDebugPrivilege                Debug programs                      Enabled
```

#### Explanation
Generates process creation events containing command-line arguments to test policy auditing.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Query Process Creation Events via PowerShell

#### Step-by-Step Instructions
1. Open PowerShell as Administrator.
2. Run:
```powershell
Get-WinEvent -LogName "Security" -MaxEvents 10 | Where-Object {$_.Id -eq 4688}
```

#### Expected Output
```text
TimeCreated  ProviderName  Id Message
-----------  ------------  -- -------
08/02/2026   Microsoft... 4688 A new process has been created.
```

#### Explanation
Queries the Security log for Event ID 4688 programmatically using `Get-WinEvent`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Extract Command-Line Arguments via PowerShell

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688} -MaxEvents 5 | ForEach-Object {
    $xml = [xml]$_.ToXml()
    [PSCustomObject]@{
        Time = $_.TimeCreated
        NewProcess = $xml.Event.EventData.Data | Where-Object {$_.Name -eq 'NewProcessName'} | Select-Object -ExpandProperty '#text'
        CommandLine = $xml.Event.EventData.Data | Where-Object {$_.Name -eq 'CommandLine'} | Select-Object -ExpandProperty '#text'
    }
}
```

#### Expected Output
```text
Time                 NewProcess                    CommandLine
----                 ----------                    -----------
8/2/2026 11:15:02 AM C:\Windows\System32\whoami.exe whoami /priv
8/2/2026 11:15:10 AM C:\Windows\System32\cmd.exe    netstat -ano > C:\Users\Public\test.txt
```

#### Explanation
Parses underlying XML EventData elements to extract exact process names and executed command-line parameters.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Query System Log for Service Creation

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -ErrorAction SilentlyContinue | Format-List TimeCreated, Message
```

#### Expected Output
```text
TimeCreated : 8/2/2026 11:00:15 AM
Message     : A service was installed in the system.
              Service Name: TriageAgent
              Service File Name: C:\Windows\System32\notepad.exe
```

#### Explanation
Parses System log entries for newly registered system services.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Query Application Log for Errors

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Level=2; StartTime=(Get-Date).AddDays(-1)} -MaxEvents 5
```

#### Expected Output
```text
TimeCreated  ProviderName  Id Message
-----------  ------------  -- -------
08/02/2026   ESENT       454 Database recovery failed...
```

#### Explanation
Level=2 filters specifically for Error events logged in the last 24 hours.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: Export Event Log to `.evtx` File

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
wevtutil epl Security "C:\Users\Public\SecurityLog_Export.evtx" /q:"*[System[(EventID=4688 or EventID=4624)]]"
```

#### Expected Output
```text
Command completes silently. "C:\Users\Public\SecurityLog_Export.evtx" is created.
```

#### Explanation
Exports matching event records into binary `.evtx` format for external forensic analysis.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Query Sysmon Operational Log (If Installed)

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 5 -ErrorAction SilentlyContinue
```

#### Expected Output
```text
TimeCreated  ProviderName  Id Message
-----------  ------------  -- -------
08/02/2026   Microsoft...   1 Process Create: RuleName: - ...
```

#### Explanation
Queries Sysmon operational channels for high-fidelity endpoint telemetry.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Detect Audit Log Clearing (Event ID 1102)

#### Step-by-Step Instructions
1. Query for log clearance events in PowerShell:
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102} -ErrorAction SilentlyContinue
```

#### Expected Output
```text
No events returned (indicates Security Log has not been cleared).
```

#### Explanation
Event ID 1102 triggers whenever a user or script executes `wevtutil cl Security` or clears the log via Event Viewer.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Convert Event Log Records to CSV

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-WinEvent -LogName "Security" -MaxEvents 20 | Select-Object TimeCreated, Id, RecordId, Message | Export-Csv -Path "C:\Users\Public\Security_Events.csv" -NoTypeInformation
```

#### Expected Output
```text
Command completes silently. "C:\Users\Public\Security_Events.csv" is created.
```

#### Explanation
Converts log objects into structured CSV for easy triage reporting.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Clean Up Lab Artifacts

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
del /f /q C:\Users\Public\test.txt
del /f /q C:\Users\Public\SecurityLog_Export.evtx
del /f /q C:\Users\Public\Security_Events.csv
```

#### Expected Output
```cmd
C:\Windows\System32> del /f /q C:\Users\Public\test.txt
```

#### Explanation
Cleans up temporary lab test files.

---

### Screenshot

> **Insert Screenshot Here**

---
