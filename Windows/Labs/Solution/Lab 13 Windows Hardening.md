# Lab 13 Solution — Windows Hardening

## Solution

---

### Task 1: Check the Guest Account Status

#### Step-by-Step Instructions
1. Open an elevated PowerShell session.
2. Run `Get-LocalUser -Name "Guest" | Select-Object Name, Enabled`.

#### Expected Output
```text
Name  Enabled
----  -------
Guest    True
```

#### Explanation
Confirms whether the built-in Guest account is currently active — it should normally be disabled.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Disable the Guest Account

#### Step-by-Step Instructions
1. Run `Disable-LocalUser -Name "Guest"`.
2. Re-run `Get-LocalUser -Name "Guest" | Select-Object Name, Enabled` to confirm.

#### Expected Output
```text
Name  Enabled
----  -------
Guest   False
```

#### Explanation
Disabling unused accounts follows the principle of least privilege from Chapter 15.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Review Running Services

#### Step-by-Step Instructions
1. Run `Get-Service | Where-Object { $_.Status -eq "Running" } | Select-Object Name, DisplayName`.

#### Expected Output
```text
Name       DisplayName
----       -----------
WinDefend  Microsoft Defender Antivirus Service
Dnscache   DNS Client
Spooler    Print Spooler
```

#### Explanation
Any service on this list that isn't recognized or expected on this machine should be researched before being assumed safe.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Check Windows Update History

#### Step-by-Step Instructions
1. Run `Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5`.

#### Expected Output
```text
Source        Description      HotFixID    InstalledOn
------        -----------      --------    -----------
WORKSTATION09 Security Update  KB5037771   6/11/2026 12:00:00 AM
```

#### Explanation
An `InstalledOn` date far in the past would indicate the machine hasn't been patched recently — a hardening gap.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Confirm Security Features Are Enabled

#### Step-by-Step Instructions
1. Run `Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled`.
2. Run `Get-NetFirewallProfile | Select-Object Name, Enabled`.

#### Expected Output
```text
RealTimeProtectionEnabled
--------------------------
                      True

Name    Enabled
----    -------
Domain     True
Private    True
Public     True
```

#### Explanation
Confirms the Chapter 11 security baseline is still intact before the machine is redeployed.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Check Administrators Group Membership

#### Step-by-Step Instructions
1. Run `Get-LocalGroupMember -Group "Administrators"`.

#### Expected Output
```text
ObjectClass Name                         PrincipalSource
----------- ----                         ---------------
User        WORKSTATION09\Administrator  Local
User        WORKSTATION09\ITAdmin        Local
```

#### Explanation
Any account in this list that isn't an expected IT or system account should be flagged and investigated.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Build a Hardening Review Script

#### Step-by-Step Instructions
1. Create `HardeningReview.ps1`:
```powershell
# HardeningReview.ps1
# Runs a basic hardening review across accounts, services, updates, and security features

Write-Host "=== Account Check: Guest Account ===" -ForegroundColor Cyan
Get-LocalUser -Name "Guest" | Select-Object Name, Enabled

Write-Host "`n=== Running Services ===" -ForegroundColor Cyan
Get-Service | Where-Object { $_.Status -eq "Running" } | Select-Object Name, DisplayName

Write-Host "`n=== Recent Windows Updates ===" -ForegroundColor Cyan
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5

Write-Host "`n=== Security Features ===" -ForegroundColor Cyan
Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled
Get-NetFirewallProfile | Select-Object Name, Enabled
```

#### Expected Output
```text
(File created — output is produced in Task 8 when run)
```

#### Explanation
Combines the earlier tasks into one repeatable script, following the same pattern introduced in Chapter 14.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Run the Script and Document Findings

#### Step-by-Step Instructions
1. Run `.\HardeningReview.ps1`.
2. Review each section's output.
3. Write a short summary noting anything that deviates from baseline (for example: Guest account was enabled and has now been disabled; all other checks passed).

#### Expected Output
```text
=== Account Check: Guest Account ===
Name  Enabled
----  -------
Guest   False

=== Running Services ===
...

=== Recent Windows Updates ===
...

=== Security Features ===
...
```

#### Explanation
Documenting findings — even ones that pass — creates a record that this machine was properly reviewed before redeployment.

---

### Screenshot

> **Insert Screenshot Here**

---

## Challenge Answers

| Challenge | Solution |
|---|---|
| Add BitLocker check | Add `Get-BitLockerVolume \| Select-Object MountPoint, ProtectionStatus` to the script |
| CIS Benchmark example | E.g. "Ensure 'Guest account status' is Disabled" maps directly to `Get-LocalUser -Name "Guest"` |
| Check Remote Desktop Users | `Get-LocalGroupMember -Group "Remote Desktop Users"` |
| One-time vs repeatable hardening | A one-time check only proves compliance at that moment; a repeatable script (scheduled or reused) catches configuration drift over time |

---

## 🎉 Lab Complete!

You have performed a full hardening review covering accounts, services, patch status, and security features, and built a reusable script to repeat it on future machines.