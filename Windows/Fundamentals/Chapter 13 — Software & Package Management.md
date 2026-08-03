# Chapter 13 — Software & Package Management

## Introduction

Every program on a Windows computer had to get there somehow — downloaded and installed by a user, pushed out by an IT department, or in some cases, quietly installed by malware without anyone noticing. Knowing what software is supposed to be on a machine, and how to check what's actually installed, is a basic skill every Blue Team beginner needs.

This chapter covers how software gets installed on Windows, how to list what's currently installed using the command line, and how to remove it — all skills that come up constantly during both routine administration and security investigations.

---

## Learning Objectives

Students should be able to:

- Describe the common ways software is installed on Windows.
- List installed software using PowerShell and the command line.
- Explain what `winget` is and how it's used to install and manage software.
- Uninstall software from the command line.
- Explain why an unexpected or unknown program in a software list is worth investigating.

---

## Why Blue Teams Care

1. **Unwanted Software Is a Red Flag.** Malware often installs itself the same way legitimate software does — it just doesn't ask permission first. Comparing an installed-software list against what's expected on a machine can reveal unauthorized programs.
2. **Old Software Is a Risk.** Outdated versions of common software (browsers, PDF readers, Java) often contain known vulnerabilities. Being able to quickly list installed software and their versions supports vulnerability management.
3. **Evidence for Investigations.** When investigating an incident, knowing exactly what was installed — and when — helps build a timeline of what happened on the machine.

---

## Core Concepts

### 1. How Software Gets Installed on Windows

| Method | Description |
|---|---|
| **MSI Installer** | A structured, database-driven installer format (`.msi`) commonly used by business and enterprise software |
| **EXE Installer** | A traditional executable setup file (`.exe`) — the most common format for everyday downloads |
| **Microsoft Store** | Sandboxed apps installed and updated through the built-in Store app |
| **Windows Package Manager (`winget`)** | A command-line tool for installing and updating software directly from a curated catalog |

### 2. Listing Installed Software

There are several ways to check what's installed, and it's worth knowing more than one — because malware sometimes hides itself from the slower, more obvious methods.

**Using PowerShell (fast, but only shows installer-registered software):**

```powershell
# Read the Uninstall registry key directly — usually the fastest method
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Where-Object { $_.DisplayName }
```

**Using `winget` (only shows software winget knows how to manage):**

```powershell
# List software winget can see and manage
winget list
```

**Using WMI (thorough, but noticeably slower):**

```powershell
# A comprehensive but slower query of installed software
Get-CimInstance -ClassName Win32_Product | Select-Object Name, Version, Vendor
```

> **Note**
>
> No single command shows 100% of installed software — that's exactly why analysts learn more than one method. A program that hides from one list may still show up in another.

### 3. Using `winget` to Install and Update Software

`winget` is Microsoft's official command-line package manager. It lets you search for, install, update, and remove software without opening a browser.

```powershell
# Search the winget catalog for a package
winget search "notepad++"

# Install a package
winget install Notepad++.Notepad++

# Update all installed packages that winget manages
winget upgrade --all
```

### 4. Uninstalling Software

```powershell
# Uninstall a package using winget
winget uninstall Notepad++.Notepad++
```

```cmd
:: List installed programs from CMD (legacy method, works on older systems too)
wmic product get name,version
```

---

## Practical Examples

### A Simple Software Inventory Check

```powershell
# Export a snapshot of installed software to a file for later comparison
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Where-Object { $_.DisplayName } |
    Export-Csv -Path "$env:USERPROFILE\Desktop\software_inventory.csv" -NoTypeInformation
```

Saving a snapshot like this lets you compare software lists over time, or compare a suspicious machine against a known-good baseline.

---

## Blue Team Investigation Notes

> **Blue Team Insight: Spotting Unauthorized Software**
>
> When reviewing a software inventory, look for:
>
> - **Unfamiliar publisher names**, especially generic or misspelled ones that try to imitate a real company.
> - **Installation dates that don't match any approved change**, such as software that appeared overnight with no ticket or record.
> - **Software installed in unusual locations**, like a user's temp or downloads folder instead of `C:\Program Files`.
> - Remember that `Get-CimInstance Win32_Product` only reliably reports software installed via MSI — it can miss EXE-based installers, so cross-check with the registry method above.

---

## Common Mistakes

| Mistake | Consequence | How to Avoid |
|---|---|---|
| Relying on only one listing method | Some installed software (especially malware) won't show up in every method | Check the registry, `winget`, and WMI methods together |
| Assuming `Win32_Product` shows everything | This query only reliably reports MSI-installed software | Prefer the Uninstall registry key for a fuller picture |
| Treating every unfamiliar name as malicious | Many legitimate utilities have unfamiliar or generic-sounding names | Verify publisher, install date, and file location before concluding anything |

---

## Best Practices

1. **Keep a baseline software inventory** for reference machines so unusual entries stand out quickly.
2. **Check more than one listing method** rather than trusting a single command.
3. **Use `winget upgrade --all`** regularly to reduce the number of outdated, vulnerable applications on a machine.
4. **Record install dates and publishers** whenever reviewing software, since both are useful clues during an investigation.

---

## Summary

- Windows software commonly arrives through MSI installers, EXE installers, the Microsoft Store, or `winget`.
- PowerShell can list installed software by reading the Uninstall registry key, using `winget list`, or querying WMI — each method has gaps, so it's best to use more than one.
- `winget` is Microsoft's command-line package manager for searching, installing, updating, and removing software.
- Comparing an installed-software list against a known-good baseline is a simple but effective way to spot unauthorized programs.

The next chapter builds on the command-line skills from this and earlier chapters to introduce basic PowerShell scripting.

---

## Key Commands

| Command / Cmdlet | Purpose | Example |
|---|---|---|
| `Get-ItemProperty` | Lists installed software from the Uninstall registry key | `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*"` |
| `winget list` | Lists software winget can manage | `winget list` |
| `winget search` | Searches the winget catalog | `winget search "notepad++"` |
| `winget install` | Installs a package | `winget install Notepad++.Notepad++` |
| `winget upgrade --all` | Updates all winget-managed software | `winget upgrade --all` |
| `winget uninstall` | Removes a package | `winget uninstall Notepad++.Notepad++` |
| `Get-CimInstance Win32_Product` | Lists MSI-installed software (slower) | `Get-CimInstance -ClassName Win32_Product` |

---

## Further Reading

- [Microsoft Learn: Windows Package Manager (winget)](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Microsoft Learn: Get-CimInstance](https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance)
- [MITRE ATT&CK: Software Discovery (T1518)](https://attack.mitre.org/techniques/T1518/)

# Next Chapter

➡ **[Chapter 14 — PowerShell Scripting Basics](./Chapter%2014%20%E2%80%94%20PowerShell%20Scripting%20Basics.md)**
