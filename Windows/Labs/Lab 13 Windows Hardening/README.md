# Lab 13 — Windows Hardening

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 15 (Windows Hardening).  
**Objectives**:
- Check and disable an unused local account.
- Review running services against expected baseline services.
- Check Windows Update history for patch currency.
- Confirm core security features remain enabled.
- Build and run a combined hardening review script.

---

## Scenario

`WORKSTATION-09` is being prepared for redeployment to a new department. Before it's handed over, your team lead has asked you to run a full hardening review — checking accounts, services, updates, and security features — and to flag anything that doesn't match the organization's baseline.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Tools Used**: PowerShell

---

## Tasks

### Task 1: Check the Guest Account Status
Run `Get-LocalUser -Name "Guest" | Select-Object Name, Enabled` to check whether the account is enabled.

### Task 2: Disable the Guest Account
If enabled, run `Disable-LocalUser -Name "Guest"` and confirm the change with Task 1's command.

### Task 3: Review Running Services
Run `Get-Service | Where-Object { $_.Status -eq "Running" } | Select-Object Name, DisplayName` and review the list for anything unfamiliar.

### Task 4: Check Windows Update History
Run `Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5` to check how recently the machine was patched.

### Task 5: Confirm Security Features Are Enabled
Run `Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled` and `Get-NetFirewallProfile | Select-Object Name, Enabled` to confirm Chapter 11's baseline is still intact.

### Task 6: Check Administrators Group Membership
Run `Get-LocalGroupMember -Group "Administrators"` and confirm only expected accounts have administrator rights.

### Task 7: Build a Hardening Review Script
Combine Tasks 1, 3, 4, and 5 into a single script named `HardeningReview.ps1`.

### Task 8: Run the Script and Document Findings
Run `.\HardeningReview.ps1` and write a short summary of any findings that don't match the expected baseline (all security features enabled, Guest disabled, no unfamiliar admin accounts, recent updates installed).

---

## Verification

To verify success:
- Confirm the Guest account shows `Enabled : False` after Task 2.
- Confirm `HardeningReview.ps1` runs end-to-end and prints output for all four check areas.
- Confirm your written summary in Task 8 references actual command output, not assumptions.

---

## Blue Team Notes

- **Hardening Is a Checklist, Not a Feeling**: Every finding in this lab should be backed by a specific command's output — "it looks fine" is not a hardening review.
- **A Disabled Guest Account Is Expected, Not Optional**: If Task 1 shows the Guest account enabled with no documented reason, that's a deviation from baseline worth flagging immediately.

---

## Common Errors

- **Disabling accounts without checking dependencies first**: Confirm the Guest account isn't intentionally in use for a specific business reason before disabling it.
- **Assuming an unfamiliar service is malicious**: Research a service before concluding it shouldn't be running.
- **Skipping the Administrators group check**: An extra account in this group is one of the most common signs of privilege misuse.

---

## MITRE ATT&CK Mapping

- **T1078**: Valid Accounts
- **T1136**: Create Account
- **T1562**: Impair Defenses

---

## Challenge Section

1. Extend `HardeningReview.ps1` to also check BitLocker status, reusing the command from Chapter 11.
2. Research one CIS Benchmark recommendation for Windows 10/11 and explain how you would check for it using PowerShell.
3. Modify Task 6 to also list members of the local `Remote Desktop Users` group.
4. Explain, in your own words, the difference between hardening a machine once versus building a repeatable hardening review process.