# Lab 09 — Windows Security

## Scenario

Your organization is deploying a batch of new Windows workstations for the Finance department. Before they go live, the Security team requires a pre-deployment audit. You must verify that Windows Defender, BitLocker, the Windows Firewall, and User Account Control (UAC) are all properly configured according to company policy.

Additionally, you must test Defender's effectiveness against a simulated test payload (the industry-standard EICAR test file).

---

# Mission

Perform a comprehensive security posture audit of a Windows workstation using PowerShell and native tools. Verify that all critical security features are enabled and properly configured. Then, test Windows Defender's detection capability against a harmless test payload.

---

# Story

The IT Security Manager sends you the audit requirements:

> *"Finance handles sensitive customer financial data. Before these workstations go into production, I need PROOF that Defender is on, BitLocker is encrypting the drives, the firewall is active on all profiles, and UAC is at default or above. Run the EICAR test too — if Defender doesn't catch it, we have a serious problem."*

---

# Learning Objectives

After completing this lab, you will be able to:

* Audit Windows Defender Antivirus status using PowerShell.
* Verify BitLocker Drive Encryption status.
* Check Windows Firewall profile configurations.
* Verify UAC integrity levels and settings.
* Test Defender detection using the industry-standard EICAR test file.
* Generate a basic security posture report.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 11 (Windows Security Features).

---

# Clues

> **"The EICAR test string is a standardized, harmless string that EVERY antivirus product on the planet is designed to detect. If Defender doesn't flag it, real-time protection is disabled."**

> **"Check `EnableLUA` in the registry. If it's `0`, UAC is completely disabled and any program can silently gain admin rights."**

---

# Your Tasks

### Task 1 — Audit Windows Defender
Open PowerShell as Administrator. Check Defender's current status:

```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled, AntivirusSignatureLastUpdated
```

Is Real-Time Protection enabled? When were the signatures last updated?

---

### Task 2 — Check for Defender Exclusions
Attackers sometimes add exclusion paths so Defender ignores their malware.

```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

Are there any suspicious exclusion paths?

---

### Task 3 — Test Defender with EICAR
Create the EICAR test file to verify that Defender's real-time protection is working.

```powershell
$eicar = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
Set-Content -Path "C:\Temp\eicar_test.txt" -Value $eicar
```

Windows Defender should immediately detect and quarantine this file. Check the threat detection log:

```powershell
Get-MpThreatDetection
```

---

### Task 4 — Audit Firewall Status
Check that the firewall is active on ALL profiles (Domain, Private, Public).

```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

All profiles should show `Enabled: True` and `DefaultInboundAction: Block`.

---

### Task 5 — Audit BitLocker
Check if the system drive is encrypted.

```powershell
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionMethod
```

Or via CMD: `manage-bde -status C:`

---

### Task 6 — Verify UAC Configuration
Check the registry to confirm UAC is enabled.

```powershell
$uac = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
Write-Host "EnableLUA: $($uac.EnableLUA)"
Write-Host "ConsentPromptBehaviorAdmin: $($uac.ConsentPromptBehaviorAdmin)"
```

`EnableLUA` should be `1`. `ConsentPromptBehaviorAdmin` should be `5` (Prompt for consent on secure desktop).

---

### Task 7 — Verify Secure Boot
Check if the machine is using UEFI Secure Boot.

```powershell
Confirm-SecureBootUEFI
```

This should return `True`.

---

### Task 8 — Check Integrity Level
Open a standard (non-elevated) Command Prompt and run:
`whoami /groups | findstr "Integrity"`

Then open an elevated Command Prompt and run the same command. Compare the Integrity Level (Medium vs. High).

---

### Task 9 — Generate a Security Posture Report
Combine everything into a single script output:

```powershell
Write-Host "====== SECURITY POSTURE REPORT ======" -ForegroundColor Green
Write-Host "`n[Defender]" -ForegroundColor Cyan
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
Write-Host "`n[Firewall]" -ForegroundColor Cyan
Get-NetFirewallProfile | Select-Object Name, Enabled
Write-Host "`n[UAC]" -ForegroundColor Cyan
Write-Host "EnableLUA: $((Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).EnableLUA)"
Write-Host "`n[Secure Boot]" -ForegroundColor Cyan
Confirm-SecureBootUEFI
```

---

# Success Criteria

You have successfully completed this lab if you can:

* Confirm Windows Defender real-time protection is enabled via PowerShell.
* Successfully trigger and detect the EICAR test file.
* Verify all three firewall profiles are enabled.
* Confirm UAC is enabled via registry inspection.

---

# 💙 Blue Team Insight

One of the first things sophisticated malware does after gaining admin access is **disable security features**: it turns off Defender, adds exclusion paths, disables the firewall, and lowers UAC. During incident response, if you find that any of these features are disabled and the organization didn't do it intentionally, treat it as a strong indicator of compromise.

---

# Key Takeaways

After completing this lab, you should be able to:

* Perform a rapid security posture audit of any Windows endpoint using PowerShell.
* Validate endpoint defenses before deployment or during incident response.
* Test antivirus effectiveness using standardized test payloads.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2009%20Solution.md)**
