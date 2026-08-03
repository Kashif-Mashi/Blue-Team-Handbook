# Chapter 11 — Windows Security Features

---

# 📖 Overview

Microsoft Windows includes a comprehensive suite of built-in security features designed to protect endpoints from malware, unauthorized access, data theft, and exploitation. These features operate across multiple defense layers — from kernel-level protections and boot integrity to user-facing controls like Windows Defender and BitLocker.

For Blue Teams, understanding these native security features is essential. They form the first line of defense on every Windows endpoint, and their proper configuration (or misconfiguration) directly impacts the organization's security posture.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Explain the role and architecture of Windows Defender Antivirus, including real-time protection, cloud-delivered protection, and controlled folder access.
- Describe User Account Control (UAC) integrity levels and how they prevent unauthorized privilege escalation.
- Understand BitLocker Drive Encryption, TPM integration, and recovery key management.
- Configure Windows Defender Firewall profiles and create granular inbound/outbound rules.
- Describe Windows Secure Boot, UEFI, and Trusted Platform Module (TPM) boot integrity chain.
- Explain Credential Guard, Device Guard, and Attack Surface Reduction (ASR) rules.
- Audit security feature status using PowerShell and command-line tools.

---

# Why Blue Teams Care

1. **Baseline Security Validation**: Before performing any investigation, responders must verify that endpoint security features are actually enabled. Attackers routinely disable Windows Defender, turn off the firewall, or lower UAC settings.
2. **Defense-in-Depth**: No single feature prevents all attacks. BitLocker protects data at rest, Defender catches known malware, UAC limits privilege escalation, and Credential Guard prevents credential dumping — together they form a layered defense.
3. **Compliance Requirements**: Enterprise compliance frameworks (CIS Benchmarks, NIST 800-171, PCI-DSS) mandate specific configurations for Defender, BitLocker, and firewall policies.

---

# Core Concepts

## 1. Windows Defender Antivirus

Windows Defender is the built-in anti-malware engine that provides:

- **Real-Time Protection (RTP)**: Scans files on access, download, and execution.
- **Cloud-Delivered Protection**: Submits suspicious samples to Microsoft's cloud analysis backend for rapid verdict.
- **Behavior Monitoring**: Detects malicious behavior patterns even for unknown (zero-day) malware.
- **Controlled Folder Access**: Prevents ransomware from encrypting files in protected folders (Documents, Desktop, etc.).

```powershell
# Check Defender status
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled

# Run a quick scan
Start-MpScan -ScanType QuickScan

# Run a full system scan
Start-MpScan -ScanType FullScan

# Update signature definitions
Update-MpSignature

# View Defender threat history
Get-MpThreatDetection
```

---

## 2. User Account Control (UAC)

UAC prevents applications from making unauthorized system changes by requiring explicit administrator approval. When enabled, even administrator accounts operate with standard-user tokens unless elevation is explicitly requested.

### UAC Integrity Levels

| Level | Description | Example |
|---|---|---|
| **Low** | Sandboxed, minimal privileges. | Internet Explorer Protected Mode. |
| **Medium** | Standard user privileges. Default for all non-elevated processes. | `explorer.exe`, `notepad.exe`. |
| **High** | Administrative privileges. Granted after UAC consent prompt. | Elevated `cmd.exe`, `regedit.exe`. |
| **System** | Highest OS privilege. Reserved for system services. | `lsass.exe`, `services.exe`. |

```cmd
:: Check current integrity level and privileges
whoami /groups
whoami /priv
```

> 💙 **Blue Team Note**: If UAC is disabled or set to "Never notify," attackers can silently elevate privileges without any user interaction. Always verify UAC is set to at least the default level.

---

## 3. BitLocker Drive Encryption

BitLocker encrypts entire disk volumes to protect data at rest. Even if an attacker steals the physical hard drive, they cannot read the data without the encryption key.

- **TPM Integration**: BitLocker stores encryption keys in the Trusted Platform Module (TPM) chip, which releases keys only if the boot process integrity is verified.
- **Recovery Key**: A 48-digit numeric key used to unlock the drive if the TPM is unavailable or boot integrity fails.

```powershell
# Check BitLocker status on all drives
Get-BitLockerVolume

# Check BitLocker status on C: drive
manage-bde -status C:

# Enable BitLocker on C: drive with TPM
Enable-BitLocker -MountPoint "C:" -TpmProtector
```

---

## 4. Windows Defender Firewall

The Windows Defender Firewall operates with three profiles:

| Profile | When Active | Default |
|---|---|---|
| **Domain** | Machine is joined to an Active Directory domain. | Inbound blocked, Outbound allowed. |
| **Private** | Connected to a trusted home/work network. | Inbound blocked, Outbound allowed. |
| **Public** | Connected to an untrusted network (coffee shop, hotel). | Most restrictive. |

```powershell
# View firewall profile status
Get-NetFirewallProfile | Select-Object Name, Enabled

# Disable firewall (DANGEROUS — for testing only)
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

# Create a rule to block inbound RDP from all sources
New-NetFirewallRule -DisplayName "Block RDP" -Direction Inbound -LocalPort 3389 -Protocol TCP -Action Block
```

---

## 5. Secure Boot & TPM

- **Secure Boot**: A UEFI feature that verifies the digital signature of the bootloader and kernel before allowing execution. Prevents bootkits and rootkits.
- **Trusted Platform Module (TPM)**: A hardware security chip that stores encryption keys, measures boot integrity, and provides hardware-based random number generation.

```powershell
# Check Secure Boot status
Confirm-SecureBootUEFI

# Check TPM status
Get-Tpm
```

---

## 6. Advanced Security Features

| Feature | Purpose |
|---|---|
| **Credential Guard** | Uses virtualization-based security (VBS) to isolate LSASS credential storage from the OS kernel, preventing tools like Mimikatz from dumping passwords. |
| **Attack Surface Reduction (ASR)** | GPO-configurable rules that block common attack vectors (e.g., Office macros spawning child processes, credential stealing from LSASS). |
| **Windows Sandbox** | An isolated, disposable desktop environment for safely testing suspicious files. |
| **SmartScreen** | Reputation-based filtering for downloaded files and visited URLs. |

---

# Practical Examples

## Auditing Security Features via PowerShell

```powershell
# Full security posture check
Write-Host "=== Windows Defender ===" -ForegroundColor Cyan
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled

Write-Host "`n=== Firewall Status ===" -ForegroundColor Cyan
Get-NetFirewallProfile | Select-Object Name, Enabled

Write-Host "`n=== BitLocker Status ===" -ForegroundColor Cyan
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus

Write-Host "`n=== Secure Boot ===" -ForegroundColor Cyan
Confirm-SecureBootUEFI

Write-Host "`n=== UAC Setting ===" -ForegroundColor Cyan
(Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).EnableLUA
```

---

# Blue Team Investigation Notes

> 💙 **Blue Team Note: First Responder Security Check**
> 
> During every incident response engagement, the FIRST thing you should do is verify the security posture of the compromised host:
> 1. Is Windows Defender running? (`Get-MpComputerStatus`)
> 2. Is the Firewall enabled? (`Get-NetFirewallProfile`)
> 3. Is UAC enabled? (Registry `EnableLUA` = 1)
> 4. Has Defender detected anything? (`Get-MpThreatDetection`)
> 
> If any of these are disabled, the attacker likely turned them off during post-exploitation.

---

# Common Mistakes

| Mistake | Consequence | How to Avoid |
|---|---|---|
| Disabling UAC | Malware silently elevates to admin without consent. | Keep UAC at default or higher setting. |
| Excluding entire drives from Defender | Malware in excluded paths runs undetected. | Use narrow, specific exclusions only. |
| Not backing up BitLocker recovery keys | Drive is permanently inaccessible after hardware changes. | Store recovery keys in Active Directory or Azure AD. |

---

# Best Practices

1. **Enable Tamper Protection**: Prevents malware from disabling Defender programmatically.
2. **Enable Controlled Folder Access**: Protects Documents, Desktop, and Pictures from ransomware encryption.
3. **Deploy ASR Rules**: Block Office macro child processes, credential stealing, and untrusted USB executables.
4. **Enforce BitLocker via GPO**: Require BitLocker on all organizational endpoints with recovery keys escrowed to AD.
5. **Set UAC to Maximum**: "Always notify" ensures every elevation attempt requires explicit consent.

---

# 🔑 Key Takeaways

- Windows Defender provides real-time antimalware protection, cloud analysis, and controlled folder access.
- UAC enforces integrity levels that prevent unauthorized privilege escalation.
- BitLocker encrypts drives at rest using TPM-backed encryption keys.
- Windows Defender Firewall operates across Domain, Private, and Public profiles.
- Secure Boot and TPM protect the boot chain integrity against rootkits.
- Credential Guard uses virtualization to prevent credential dumping (Mimikatz).

---

# Key Commands

| Command / Cmdlet | Purpose | Example |
|---|---|---|
| `Get-MpComputerStatus` | Checks Defender status | `Get-MpComputerStatus` |
| `Start-MpScan` | Runs a Defender scan | `Start-MpScan -ScanType QuickScan` |
| `Get-BitLockerVolume` | Checks BitLocker encryption status | `Get-BitLockerVolume` |
| `Get-NetFirewallProfile` | Displays firewall profile status | `Get-NetFirewallProfile` |
| `Confirm-SecureBootUEFI` | Checks Secure Boot status | `Confirm-SecureBootUEFI` |
| `whoami /groups` | Displays current integrity level | `whoami /groups` |

---

# Quick Quiz

1. **Which Windows Defender feature prevents ransomware from encrypting files in protected folders?**
   - A) Real-Time Protection
   - B) Controlled Folder Access
   - C) Cloud-Delivered Protection
   - D) SmartScreen

2. **What UAC integrity level do standard non-elevated processes run at?**
   - A) Low
   - B) Medium
   - C) High
   - D) System

3. **Which hardware component stores BitLocker encryption keys and verifies boot integrity?**
   - A) BIOS
   - B) GPU
   - C) TPM (Trusted Platform Module)
   - D) NIC

4. **Which security feature uses virtualization-based security to protect LSASS from credential dumping?**
   - A) BitLocker
   - B) Credential Guard
   - C) SmartScreen
   - D) UAC

5. **What is the registry value that indicates UAC is enabled?**
   - A) `EnableUAC = 1`
   - B) `EnableLUA = 1`
   - C) `UACEnabled = True`
   - D) `SecurityLevel = High`

---

## Quiz Answers

1. **B** (Controlled Folder Access)
2. **B** (Medium)
3. **C** (TPM)
4. **B** (Credential Guard)
5. **B** (`EnableLUA = 1`)

---

# Further Reading

- [Microsoft Learn: Windows Defender Antivirus](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-antivirus-windows)
- [Microsoft Learn: BitLocker Overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)
- [Microsoft Learn: Credential Guard](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/)
- [CIS Benchmarks for Windows](https://www.cisecurity.org/benchmark/microsoft_windows_desktop)

---

# Next Chapter

➡ **[Chapter 12 — Windows Registry Fundamentals](./Chapter%2012%20%E2%80%94%20Windows%20Registry%20Fundamentals.md)**
