# Chapter 13 — Software & Package Management

---

# 📖 Overview

Managing installed software on Windows endpoints is a critical operational and security function. Every application installed on a system expands the attack surface — outdated browsers, unpatched Java runtimes, and vulnerable PDF readers are among the most commonly exploited entry points for malware.

Windows provides multiple mechanisms for installing, querying, updating, and removing software, ranging from the traditional Control Panel to modern PowerShell cmdlets and package managers like `winget`.

For Blue Teams, software inventory and patch management are essential. Knowing exactly what is installed, at what version, and whether it is vulnerable directly supports vulnerability management, compliance auditing, and incident response.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Query installed software using Control Panel, `wmic`, PowerShell (`Get-Package`, `Get-WmiObject`), and the registry.
- Understand MSI installer architecture and Windows Installer service.
- Use `winget` (Windows Package Manager) to search, install, and update packages from the command line.
- Identify vulnerable software versions and correlate them with known CVEs.
- Audit installed software for compliance with organizational baselines.
- Uninstall software silently using command-line tools.

---

# Why Blue Teams Care

1. **Vulnerability Exploitation**: Attackers target known vulnerabilities in outdated software (e.g., CVE-2023-21716 in Microsoft Word, Log4Shell in Java applications). Knowing installed software versions allows rapid vulnerability assessment.
2. **Shadow IT Detection**: Unauthorized applications (torrent clients, remote access tools, cryptocurrency miners) installed by users violate security policies and introduce risk.
3. **Incident Scoping**: During incident response, the installed software list reveals potential attack vectors — was the vulnerable version of Adobe Reader installed when the phishing PDF was opened?
4. **Patch Compliance**: Compliance frameworks require documented evidence that critical patches have been applied within defined SLAs.

---

# Core Concepts

## 1. Windows Software Installation Methods

| Method | Description |
|---|---|
| **MSI (Windows Installer)** | Standardized installer packages (`.msi`) managed by the Windows Installer service (`msiserver`). |
| **EXE Installers** | Custom setup executables. No standardized uninstall mechanism. |
| **MSIX / AppX** | Modern Windows 10/11 package format for UWP and desktop apps. |
| **Microsoft Store** | Curated app store with automatic updates. |
| **winget** | Command-line package manager (similar to `apt` on Linux). |
| **Chocolatey** | Community-driven Windows package manager. |

---

## 2. Querying Installed Software

### Using WMIC (Legacy)

```cmd
:: List all installed programs
wmic product get name, version, vendor

:: Find a specific application
wmic product where "name like '%%Java%%'" get name, version
```

### Using PowerShell

```powershell
# Query installed packages (modern method)
Get-Package | Select-Object Name, Version, ProviderName

# Query via WMI (comprehensive but slow)
Get-WmiObject Win32_Product | Select-Object Name, Version, Vendor

# Query from the Uninstall registry key (fastest method)
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Sort-Object DisplayName
```

> 💙 **Blue Team Note**: `Get-WmiObject Win32_Product` triggers a consistency check on every installed MSI package, which can be slow and may even trigger repairs. For speed, query the **Uninstall registry key** instead.

### Using winget

```cmd
:: List all installed software
winget list

:: Search for a package
winget search firefox

:: Install a package
winget install Mozilla.Firefox

:: Upgrade all outdated packages
winget upgrade --all
```

---

## 3. Uninstalling Software

```cmd
:: Uninstall via WMIC (silent, no reboot)
wmic product where "name='VulnerableApp'" call uninstall /nointeractive

:: Uninstall via MSI (silent)
msiexec /x {PRODUCT-GUID} /qn

:: Uninstall via winget
winget uninstall "AppName"
```

```powershell
# Uninstall via PowerShell
Get-Package -Name "VulnerableApp" | Uninstall-Package -Force
```

---

# Practical Examples

## Software Vulnerability Audit

```powershell
# Find all installed software and check for old versions
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Where-Object {$_.DisplayName -like "*Java*" -or $_.DisplayName -like "*Adobe*" -or $_.DisplayName -like "*Flash*"} |
    Select-Object DisplayName, DisplayVersion, Publisher
```

---

# Blue Team Investigation Notes

> 💙 **Blue Team Note: Hunting Unauthorized Software**
> 
> During an investigation, compare the installed software list against the organization's **approved software baseline**. Flag:
> - Remote access tools (AnyDesk, TeamViewer) not approved by IT.
> - Hacking tools (Mimikatz, PsExec) installed by attackers.
> - Cryptocurrency mining software.
> - Outdated software with known CVEs.

---

# Common Mistakes

| Mistake | Consequence | How to Avoid |
|---|---|---|
| Using only `wmic product` for queries | Slow, triggers MSI consistency checks. | Use the registry Uninstall key for speed. |
| Not checking both 32-bit and 64-bit registries | Missing 32-bit software on 64-bit OS. | Also check `HKLM:\SOFTWARE\Wow6432Node\...\Uninstall\*`. |
| Ignoring user-installed software | Per-user installs are in `HKCU`, not `HKLM`. | Query `HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*` too. |

---

# Best Practices

1. **Maintain a Software Baseline**: Document approved software and versions for each endpoint role.
2. **Automate Patch Management**: Use WSUS, SCCM, Intune, or winget to automate updates.
3. **Audit Regularly**: Schedule monthly software audits to detect unauthorized installations.
4. **Block Unapproved Software**: Use Application Control policies (AppLocker, WDAC) to prevent unauthorized executables.

---

# 🔑 Key Takeaways

- Windows software can be queried via WMIC, PowerShell, the registry Uninstall key, or `winget list`.
- The registry Uninstall key is the fastest and safest method for software inventory.
- `winget` provides a modern, Linux-like package management experience on Windows.
- Software auditing is critical for vulnerability management and compliance.
- Unauthorized software (remote access tools, hacking tools) must be flagged during incident response.

---

# Key Commands

| Command / Cmdlet | Purpose | Example |
|---|---|---|
| `winget list` | Lists all installed software | `winget list` |
| `winget install` | Installs a package | `winget install Mozilla.Firefox` |
| `winget upgrade --all` | Updates all outdated packages | `winget upgrade --all` |
| `Get-Package` | PowerShell software query | `Get-Package` |
| `wmic product get` | WMI software query (legacy) | `wmic product get name, version` |

---

# Quick Quiz

1. **Which method is fastest for querying installed software on Windows?**
   - A) `wmic product get name`
   - B) Querying the Uninstall registry key
   - C) `Get-WmiObject Win32_Product`
   - D) Control Panel

2. **What command-line tool provides Linux-like package management on Windows?**
   - A) `apt`
   - B) `yum`
   - C) `winget`
   - D) `pip`

3. **Why should Blue Teams audit installed software during incident response?**
   - A) To check wallpaper settings
   - B) To identify vulnerable applications and unauthorized tools
   - C) To count total disk space usage
   - D) To update the screensaver

---

## Quiz Answers

1. **B** (Querying the Uninstall registry key)
2. **C** (`winget`)
3. **B** (To identify vulnerable applications and unauthorized tools)

---

# Further Reading

- [Microsoft Learn: winget Documentation](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Microsoft Learn: Windows Installer](https://learn.microsoft.com/en-us/windows/win32/msi/windows-installer-portal)
- [MITRE ATT&CK: Software Discovery (T1518)](https://attack.mitre.org/techniques/T1518/)

---

# Next Chapter

➡ **[Chapter 14 — PowerShell Scripting Basics](./Chapter%2014%20%E2%80%94%20PowerShell%20Scripting%20Basics.md)**
