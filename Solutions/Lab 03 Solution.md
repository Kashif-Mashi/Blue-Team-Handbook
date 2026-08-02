# Lab 03 Solution — CMD & PowerShell Investigation

## Solution

---

### Task 1: Initialize Command Prompt Context

#### Step-by-Step Instructions
1. Press the **Windows Key**, type `cmd`.
2. Right-click **Command Prompt** and select **Run as administrator**.
3. Accept the UAC prompt.

#### Expected Output
```cmd
Microsoft Windows [Version 10.0.22631.3007]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\System32>
```

#### Explanation
Launching CMD as Administrator provides a High Integrity Level token required for administrative discovery and system log inspection.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Host System Enumeration via CMD

#### Step-by-Step Instructions
1. In CMD, execute the following command:
```cmd
systeminfo > C:\Users\Public\HostInfo.txt
```
2. Verify file creation by typing `dir C:\Users\Public\HostInfo.txt`.

#### Expected Output
```cmd
 Directory of C:\Users\Public

08/02/2026  10:15 AM            14,250 HostInfo.txt
```

#### Explanation
The `systeminfo` command queries WMI/OS layers to collect host properties, hotfix patches, net cards, and domain status. Overwrite redirection (`>`) saves output to disk.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Current Identity & Privilege Audit

#### Step-by-Step Instructions
1. Execute `whoami /all` in CMD.

#### Expected Output
```cmd
USER INFORMATION
----------------
User Name       SID
=============== =================----------------------------
desktop-1\admin S-1-5-21-3623811015-3361044348-30300820-1001

GROUP INFORMATION
-----------------
Group Name                                  Type           SID          Attributes
=========================================== ============== ============ ==================================================
Everyone                                    Well-known group S-1-1-0    Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                      Alias          S-1-5-32-544 Mandatory group, Enabled by default, Enabled group

PRIVILEGES INFORMATION
----------------------
Privilege Name                  Description                         State
=============================== =================================== ========
SeDebugPrivilege                Debug programs                      Enabled
SeShutdownPrivilege             Shut down the system                Disabled
```

#### Explanation
`whoami /all` lists the active User SID, local group SIDs, and active token privileges. Debug privilege (`SeDebugPrivilege`) confirms elevated administrative rights.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Active Process Inspection via CMD

#### Step-by-Step Instructions
1. Run `tasklist /svc` in CMD.

#### Expected Output
```cmd
Image Name                   PID Services
========================= ====== ============================================
System Idle Process            0 N/A
System                         4 N/A
smss.exe                     412 N/A
csrss.exe                    528 N/A
wininit.exe                  612 N/A
services.exe                 688 N/A
lsass.exe                    700 KeyIso, SamSs
svchost.exe                  812 DcomLaunch, PlugPlay
```

#### Explanation
`tasklist /svc` maps running process image names and PIDs to Windows services hosted within each process.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Filter Suspicious Network Connections

#### Step-by-Step Instructions
1. Run `netstat -ano | findstr "ESTABLISHED"` in CMD.

#### Expected Output
```cmd
  TCP    192.168.1.50:49672     142.250.190.46:443     ESTABLISHED     4820
  TCP    192.168.1.50:49688     20.189.173.12:443      ESTABLISHED     2140
```

#### Explanation
Piping `netstat -ano` output to `findstr "ESTABLISHED"` filters out idle listening sockets and isolates active TCP sessions along with foreign IP addresses and PIDs.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Network Interface Configuration

#### Step-by-Step Instructions
1. Run `ipconfig /all` in CMD.

#### Expected Output
```cmd
Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : localdomain
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection
   Physical Address. . . . . . . . . : 00-0C-29-88-AB-12
   DHCP Enabled. . . . . . . . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.50(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 1.1.1.1, 8.8.8.8
```

#### Explanation
`ipconfig /all` reveals host MAC addresses, local IP assignments, gateways, and configured DNS servers.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Directory Navigation & File Search

#### Step-by-Step Instructions
1. Navigate to the target directory: `cd C:\Windows\System32\drivers\etc`
2. Display hosts file contents: `type hosts`

#### Expected Output
```cmd
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
127.0.0.1       localhost
::1             localhost
```

#### Explanation
The `hosts` file maps hostnames to IP addresses locally. Attackers sometimes modify `hosts` for DNS redirection or command-and-control (C2) domain hijacking.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Environment Variable Inspection

#### Step-by-Step Instructions
1. Run `set` in CMD to view variables.
2. Display `%TEMP%` specifically: `echo %TEMP%`

#### Expected Output
```cmd
C:\Users\admin\AppData\Local\Temp
```

#### Explanation
Environment variables define operational paths. `%TEMP%` is frequently targeted by malware droppers to unpack executable files.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Initialize PowerShell Session

#### Step-by-Step Instructions
1. In CMD, type `powershell` or launch PowerShell as Administrator from Start Menu.

#### Expected Output
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\System32>
```

#### Explanation
Initializes the PowerShell .NET object runtime.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Query Running Services via PowerShell

#### Step-by-Step Instructions
1. Execute `Get-Service | Where-Object {$_.Status -eq "Running"}` in PowerShell.

#### Expected Output
```text
Status   Name               DisplayName
------   ----               -----------
Running  Appinfo            Application Information
Running  AudioSrv           Windows Audio
Running  Dhcp               DHCP Client
Running  EventLog           Windows Event Log
Running  WinDefend          Microsoft Defender Antivirus Service
```

#### Explanation
`Get-Service` returns service objects; `Where-Object` filters objects based on `Status`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: High Memory Process Identification

#### Step-by-Step Instructions
1. Execute:
```powershell
Get-Process | Where-Object { $_.WorkingSet -gt 50MB } | Sort-Object WorkingSet -Descending
```

#### Expected Output
```text
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
   1240      85   180400     240500      12.40   3412   1 msedge
    850      42    92400     110200       4.15   2140   1 explorer
```

#### Explanation
`WorkingSet` measures current RAM usage. Sorting identifies memory-heavy processes or potential memory injection targets.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Select & Export Custom Process Attributes

#### Step-by-Step Instructions
1. Execute:
```powershell
Get-Process | Select-Object ProcessName, Id, Path | Export-Csv -Path "C:\Users\Public\ProcessReport.csv" -NoTypeInformation
```

#### Expected Output
```text
Command completes silently. "C:\Users\Public\ProcessReport.csv" is created.
```

#### Explanation
`Select-Object` isolates specific properties; `Export-Csv` converts objects to standard CSV format for external SOC analysis.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Query Event Logs for Process Creation

#### Step-by-Step Instructions
1. Run:
```powershell
Get-WinEvent -LogName "Security" -MaxEvents 5 | Where-Object {$_.Id -eq 4688 -or $_.Id -eq 4624}
```

#### Expected Output
```text
TimeCreated  ProviderName  Id Message
-----------  ------------  -- -------
08/02/2026   Microsoft... 4624 An account was successfully logged on...
```

#### Explanation
`Get-WinEvent` queries event logs programmatically to inspect audit events.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Inspect PowerShell Execution Policy

#### Step-by-Step Instructions
1. Run `Get-ExecutionPolicy -List`.

#### Expected Output
```text
Scope          ExecutionPolicy
-----          ---------------
MachinePolicy  Undefined
UserPolicy     Undefined
Process        Undefined
CurrentUser    Undefined
LocalMachine   RemoteSigned
```

#### Explanation
Shows policies applied at different scopes. `RemoteSigned` requires internet-downloaded scripts to be digitally signed.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Create an Automated Triage Script

#### Step-by-Step Instructions
1. Create file `C:\Users\Public\Triage.ps1` with content:
```powershell
$Report = @(
    "Host Name: $env:COMPUTERNAME"
    "Current User: $env:USERNAME"
    "Date: $(Get-Date)"
    "----------------------------------------"
    "Active ESTABLISHED Connections:"
    (netstat -ano | findstr "ESTABLISHED")
)
$Report | Out-File -FilePath "C:\Users\Public\Triage.txt"
```
2. Execute: `powershell -ExecutionPolicy Bypass -File C:\Users\Public\Triage.ps1`
3. Inspect `C:\Users\Public\Triage.txt`.

#### Expected Output
```text
Host Name: DESKTOP-TRIAGE
Current User: admin
Date: 08/02/2026 10:30:00
----------------------------------------
Active ESTABLISHED Connections:
  TCP    192.168.1.50:49672     142.250.190.46:443     ESTABLISHED     4820
```

#### Explanation
Automates host metadata harvesting into a central triage report file.

---

### Screenshot

> **Insert Screenshot Here**

---
