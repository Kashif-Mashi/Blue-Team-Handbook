# Lab 14 Solution — Blue Team Windows Investigation

## Solution

---

### Task 1: Initial Triage

#### Step-by-Step Instructions
1. Open an elevated PowerShell session.
2. Run `whoami`, `hostname`, then `systeminfo | findstr /B /C:"OS Name" /C:"System Boot Time"`.

#### Expected Output
```text
WORKSTATION-12
OS Name:                   Microsoft Windows 11 Pro
System Boot Time:          6/2/2026, 7:41:03 AM
```

#### Explanation
Establishes the current user, hostname, and how long the system has been running — useful context for everything that follows.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Account & Access Review

#### Step-by-Step Instructions
1. Run `Get-LocalUser | Select-Object Name, Enabled`.
2. Run `Get-LocalGroupMember -Group "Administrators"`.

#### Expected Output
```text
Name          Enabled
----          -------
Administrator    True
Guest             True
jdoe              True

ObjectClass Name                    PrincipalSource
----------- ----                    ---------------
User        WORKSTATION-12\jdoe     Local
User        WORKSTATION-12\svc_temp Local
```

#### Explanation
The Guest account being enabled is a deviation from baseline (Chapter 15). `svc_temp` is an unfamiliar administrator account not on the expected list.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Process & Service Review

#### Step-by-Step Instructions
1. Run `Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, Id, CPU`.
2. Run `Get-Service | Where-Object { $_.Status -eq "Running" }`.

#### Expected Output
```text
Name        Id    CPU
----        --    ---
updtr32     4820  812.4
explorer    3204   45.1
```

#### Explanation
`updtr32` is an unfamiliar process name consuming a disproportionate amount of CPU compared to normal system processes.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Network Review

#### Step-by-Step Instructions
1. Run:
```powershell
Get-NetTCPConnection -State Established |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess
```
2. Cross-reference `OwningProcess` against the PID (`4820`) found in Task 3.

#### Expected Output
```text
LocalAddress  LocalPort  RemoteAddress    RemotePort  OwningProcess
------------  ---------  -------------    ----------  -------------
10.0.0.15     51322      198.51.100.42    4444        4820
```

#### Explanation
Process ID `4820` (`updtr32`) is connected to an external address on port `4444` — a port commonly associated with reverse shell tooling, and a strong correlating piece of evidence.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Log Review

#### Step-by-Step Instructions
1. Run:
```powershell
Get-WinEvent -LogName Security -MaxEvents 10 |
    Where-Object { $_.Id -eq 4624 -or $_.Id -eq 4625 }
```

#### Expected Output
```text
TimeCreated           Id     Message
-----------           --     -------
6/2/2026 7:42:10 AM   4624   An account was successfully logged on
```

#### Explanation
No failed logons or unusual logon activity found — nothing notable at this stage.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Security Feature & Registry Review

#### Step-by-Step Instructions
1. Run `Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled`.
2. Run `Get-NetFirewallProfile | Select-Object Name, Enabled`.
3. Run `Get-ItemProperty "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"` and the `HKLM` equivalent.

#### Expected Output
```text
RealTimeProtectionEnabled
--------------------------
                     False

UpdaterSvc : C:\Users\jdoe\AppData\Local\Temp\updtr32.exe
```

#### Explanation
Defender's real-time protection has been disabled, and an autorun entry points directly to the same `updtr32.exe` process identified in Task 3, running from a temp folder — a classic persistence pattern.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Software Review

#### Step-by-Step Instructions
1. Run:
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, InstallDate, Publisher |
    Where-Object { $_.DisplayName }
```

#### Expected Output
```text
DisplayName      InstallDate  Publisher
-----------      -----------  ---------
System Updater   20260601     (none)
```

#### Explanation
A program named "System Updater" with no publisher information and an install date matching the timeframe the user reported issues is a strong indicator.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Compare Against Baseline

#### Step-by-Step Instructions
1. Review all findings from Tasks 1–7 against the expected baseline from Chapter 15 (Guest disabled, known admins only, Defender enabled, no unexpected Run entries, only approved software installed).

#### Expected Output
```text
(No command — analytical comparison task)
```

#### Explanation
Multiple deviations from baseline were found together: Guest enabled, an unknown admin account, Defender disabled, a persistence entry, and unapproved software — all pointing the same direction.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Write the Incident Report

#### Step-by-Step Instructions
Write the report using the structure provided in the lab.

#### Expected Output

## Incident Report — WORKSTATION-12

### Summary
Investigation was opened following a user report of system slowdown and an unfamiliar desktop icon. Multiple corroborating indicators of compromise were identified.

### Scope
- User Accounts
- Running Processes
- Network Connections
- Security Logs
- Security Features & Registry
- Installed Software

### Findings
- Guest account enabled, deviating from baseline.
- Unknown local administrator account `svc_temp` present.
- Process `updtr32.exe` consuming high CPU, connected to external IP `198.51.100.42` on port `4444`.
- Windows Defender real-time protection disabled.
- Autorun entry in `HKCU...\Run` pointing to `updtr32.exe` in a temp folder.
- Unapproved software ("System Updater," no publisher) installed the same day symptoms began.

### Conclusion
Compromise is confirmed based on multiple independent, corroborating indicators: an unrecognized persistence entry, a matching high-CPU process with an active connection to an external address, and a disabled security control — consistent with a Blue Team investigation methodology from Chapter 16.

### Recommendations
- Isolate the machine from the network immediately.
- Escalate to the incident response team for full forensic imaging.
- Disable the `svc_temp` account and reset credentials for `jdoe`.
- Re-enable Windows Defender real-time protection organization-wide and audit other machines for the same indicators.
- Review how `updtr32.exe` was initially delivered to the machine.

---

### Screenshot

> **Insert Screenshot Here**

---

## Challenge Answers

| Challenge | Solution |
|---|---|
| Check for account creation | `Get-WinEvent -LogName Security \| Where-Object { $_.Id -eq 4720 }` |
| Pivoting on a suspicious IP | Check the IP against threat intelligence sources (e.g. VirusTotal, AbuseIPDB) before concluding it's malicious |
| Combined investigation script | Combine Tasks 1–7 into one `.ps1` file following the `InvestigationTriage.ps1` pattern from Chapter 14 |
| Why corroboration matters | A single artifact can have an innocent explanation; multiple independent artifacts pointing the same direction are far less likely to be coincidental |

---

## 🎉 Lab Complete!

Congratulations! You have successfully completed **Lab 14 — Blue Team Windows Investigation**.

You should now be able to:

- Conduct a structured, end-to-end Windows security investigation.
- Correlate evidence across accounts, processes, network activity, logs, the Registry, and installed software.
- Compare findings against a hardening baseline to identify deviations.
- Produce a professional incident report suitable for SOC documentation.

**Congratulations on completing all Windows Fundamentals chapters and labs in the Blue Team Handbook!**

You've now applied the same investigative mindset across both Linux and Windows environments — the two operating systems you'll encounter most often as a SOC Analyst, Incident Responder, or Threat Hunter. From here, the handbook moves toward deeper detection engineering and incident response topics, building directly on the fundamentals you've now practiced end-to-end on both platforms.