# Solution — Lab 09: Windows Security

> This solution walks through the Security Posture Audit scenario, verifying Defender, BitLocker, Firewall, and UAC configurations, plus testing Defender with the EICAR test file.

---

# Task 1 — Audit Windows Defender

## Steps

```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled, AntivirusSignatureLastUpdated
```

### Example Output

```
AntivirusEnabled                : True
RealTimeProtectionEnabled       : True
AntispywareEnabled              : True
AntivirusSignatureLastUpdated   : 8/1/2026 3:14:22 PM
```

### Investigation Note
All three should be `True`. If `RealTimeProtectionEnabled` is `False`, the endpoint is NOT actively scanning files on access — any malware downloaded or dropped on disk will execute undetected. Signature freshness matters too: signatures older than 48 hours may miss newly discovered threats.

---

# Task 2 — Check for Defender Exclusions

## Steps

```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

### Investigation Note
A clean workstation should have no exclusion paths. If you see entries like `C:\Users\Public`, `C:\Windows\Temp`, or `C:\Tools`, these are red flags — an attacker may have added them so Defender ignores their malware payload location.

---

# Task 3 — Test Defender with EICAR

## Steps

```powershell
New-Item -Path "C:\Temp" -ItemType Directory -Force
$eicar = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
Set-Content -Path "C:\Temp\eicar_test.txt" -Value $eicar
```

### Expected Behavior
Windows Defender should immediately detect and quarantine the file. You may see a notification popup.

Verify the detection:

```powershell
Get-MpThreatDetection | Select-Object -First 1 ThreatID, DomainUser, ActionSuccess, Resources
```

### Investigation Note
The EICAR string is an industry-standard test payload recognized by ALL commercial antivirus products. It is completely harmless but triggers detection. If Defender does NOT flag it, real-time protection is either disabled or broken.

---

# Task 4 — Audit Firewall Status

## Steps

```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

### Example Output

```
Name    Enabled DefaultInboundAction DefaultOutboundAction
----    ------- -------------------- ---------------------
Domain     True                Block                 Allow
Private    True                Block                 Allow
Public     True                Block                 Allow
```

### Investigation Note
All profiles must show `Enabled: True`. `DefaultInboundAction: Block` means unsolicited inbound traffic is blocked by default. If any profile shows `Enabled: False`, the workstation is wide open to inbound attacks on that network type.

---

# Task 5 — Audit BitLocker

## Steps

```powershell
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionMethod
```

### Example Output

```
MountPoint     : C:
VolumeStatus   : FullyEncrypted
ProtectionStatus : On
EncryptionMethod : XtsAes256
```

### Investigation Note
`ProtectionStatus: On` and `VolumeStatus: FullyEncrypted` confirms the drive is encrypted. `XtsAes256` is the recommended encryption method for Windows 10/11. If the status shows `FullyDecrypted`, the drive is NOT protected and a physical attacker could extract all data by removing the hard drive.

---

# Task 6 — Verify UAC Configuration

## Steps

```powershell
$uac = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
Write-Host "EnableLUA: $($uac.EnableLUA)"
Write-Host "ConsentPromptBehaviorAdmin: $($uac.ConsentPromptBehaviorAdmin)"
```

### Expected Values

| Setting | Value | Meaning |
|---|---|---|
| `EnableLUA` | `1` | UAC is enabled. |
| `ConsentPromptBehaviorAdmin` | `5` | Prompt for consent on secure desktop (default). |

### Investigation Note
If `EnableLUA` is `0`, UAC is completely disabled — any application can silently gain administrator privileges without the user seeing a consent prompt. This is a critical misconfiguration.

---

# Task 7 — Verify Secure Boot

## Steps

```powershell
Confirm-SecureBootUEFI
```

### Expected Output: `True`

### Investigation Note
If this returns `False` or throws an error, the machine is either running Legacy BIOS mode or Secure Boot is disabled. Without Secure Boot, bootkits and rootkits can load before the OS kernel, making them invisible to Defender.

---

# Task 8 — Check Integrity Level

## Steps

Standard CMD:
```cmd
whoami /groups | findstr "Integrity"
```
Output: `Mandatory Label\Medium Mandatory Level`

Elevated CMD:
```cmd
whoami /groups | findstr "Integrity"
```
Output: `Mandatory Label\High Mandatory Level`

### Investigation Note
Standard processes run at **Medium** integrity. Elevated processes run at **High** integrity. This is UAC in action — it creates a split token. Processes at Medium integrity cannot write to system directories, modify the registry `HKLM` hive, or interact with High-integrity processes.

---

# Task 9 — Generate a Security Posture Report

## Steps

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

### Investigation Note
This script produces a rapid overview of the workstation's security health. In production, you could extend this script to output results as JSON and feed it into a compliance dashboard.

---

# Scenario Conclusion

By auditing Defender, BitLocker, the Firewall, UAC, and Secure Boot, you confirmed that the Finance workstation meets the organization's security baseline. The EICAR test validated that Defender's real-time protection is functional. This workstation is cleared for production deployment.
