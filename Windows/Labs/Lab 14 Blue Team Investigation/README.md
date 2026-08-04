# Lab 14 — Blue Team Windows Investigation

## Difficulty

🟡 Intermediate

**Estimated Time**: 90 Minutes  
**Prerequisites**: Completion of Chapters 04–16 and Labs 03–13.  
**Objectives**:
- Conduct a full, structured Windows investigation from initial triage to conclusion.
- Apply account, process, network, log, Registry, and software checks together.
- Compare findings against a hardening baseline.
- Produce a short, professional incident report suitable for SOC documentation.

---

## Scenario

A user on `WORKSTATION-12` reports that their computer has been "acting weird" — it's noticeably slower than usual, and an unfamiliar program icon appeared on the desktop overnight. No malware has been confirmed yet. Your SOC lead has assigned you to investigate the machine end-to-end, following the nine-stage workflow from Chapter 16, and to produce a short incident report at the end.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Tools Used**: CMD, PowerShell, Registry tools, Event Viewer

---

## Tasks

### Task 1: Initial Triage
Run `whoami`, `hostname`, and `systeminfo | findstr /B /C:"OS Name" /C:"System Boot Time"` to establish basic context.

### Task 2: Account & Access Review
Run `Get-LocalUser | Select-Object Name, Enabled` and `Get-LocalGroupMember -Group "Administrators"` to check for unexpected accounts or elevated access.

### Task 3: Process & Service Review
Run `Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, Id, CPU` and `Get-Service | Where-Object { $_.Status -eq "Running" }` to identify anything consuming excessive resources or running unexpectedly.

### Task 4: Network Review
Run `Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess` and cross-reference any unfamiliar remote addresses against the process list from Task 3.

### Task 5: Log Review
Run `Get-WinEvent -LogName Security -MaxEvents 10 | Where-Object { $_.Id -eq 4624 -or $_.Id -eq 4625 }` to check recent logon activity for anything unusual.

### Task 6: Security Feature & Registry Review
Run `Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled`, `Get-NetFirewallProfile | Select-Object Name, Enabled`, and check both `HKCU` and `HKLM` `Run` keys for unfamiliar entries.

### Task 7: Software Review
Run `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | Select-Object DisplayName, InstallDate, Publisher | Where-Object { $_.DisplayName }` and look for anything with a recent `InstallDate` and unfamiliar publisher.

### Task 8: Compare Against Baseline
Using what you learned in Chapter 15, compare your findings against expected baseline behavior (Guest disabled, known admin accounts only, all security features enabled, no unexpected autorun entries).

### Task 9: Write the Incident Report
Using the structure below, write a short incident report summarizing your investigation:
- **Summary** (2–3 sentences)
- **Scope** (what was checked)
- **Findings** (what you found at each stage)
- **Conclusion** (was compromise confirmed, suspected, or ruled out?)
- **Recommendations** (what should happen next)

---

## Verification

To verify success:
- Confirm you have output captured from all nine tasks.
- Confirm your incident report references specific findings from your own command output, not general statements.
- Confirm your conclusion is supported by at least two independent pieces of evidence (for example, an unfamiliar Run-key entry AND a matching high-CPU process).

---

## Blue Team Notes

- **This Is the Whole Job, Compressed**: Every command in this lab has appeared in an earlier chapter. What's new here is doing them together, in order, and using the combination of results to reach a conclusion — exactly what a real Tier 1 investigation looks like.
- **A Clean Result Is Still a Valid Result**: If nothing suspicious turns up, "investigation performed, no compromise found" is a legitimate and useful conclusion — don't force a finding that isn't supported by evidence.

---

## Common Errors

- **Concluding compromise from a single artifact**: One unfamiliar process name is not proof of anything by itself — corroborate across stages.
- **Skipping the baseline comparison**: Without Task 8, you have no reference point for what counts as "unusual" on this specific machine.
- **Writing a report with no supporting evidence**: Every claim in your Task 9 report should trace back to a specific command's output from Tasks 1–8.

---

## MITRE ATT&CK Mapping

- **T1547.001**: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- **T1057**: Process Discovery
- **T1049**: System Network Connections Discovery
- **T1078**: Valid Accounts

---

## Challenge Section

1. Extend the investigation to check `Get-WinEvent` for Event ID 4720 (account creation) over the last 30 days.
2. Research how you would pivot from a suspicious remote IP address (found in Task 4) to determine whether it's a known-malicious address.
3. Turn Tasks 1–7 into a single combined PowerShell script, following the pattern from Chapter 14's `InvestigationTriage.ps1` example.
4. Explain, in your own words, why corroborating evidence across multiple stages produces a stronger conclusion than relying on the single most "interesting" finding.