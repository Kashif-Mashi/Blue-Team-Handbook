# Lab 10 — Windows Registry

## Scenario

A CEO's executive laptop was flagged by the endpoint detection platform after exhibiting suspicious boot-time behavior. A program titled `SystemHealthCheck.exe` is launching automatically every time the CEO logs in, but no one in IT installed it. The SOC suspects malware has established **registry-based persistence**.

As an Incident Responder, you must hunt through the Windows Registry `Run` keys and service entries to find and remove the persistence mechanism before the malware can exfiltrate more data.

---

# Mission

Use `regedit`, `reg.exe`, and PowerShell to inspect common persistence registry locations, identify the malicious autorun entry, remove it, and verify the registry has been cleaned.

---

# Story

The CISO calls you directly:

> *"The CEO's laptop is compromised. Something called `SystemHealthCheck.exe` is running at startup and we didn't put it there. IT says it's not in Program Files and it's not a scheduled task. That means it's hiding in the registry. Find it, kill it, and prove it's gone."*

---

# Learning Objectives

After completing this lab, you will be able to:

* Navigate the Windows Registry using `regedit`, `reg.exe`, and PowerShell.
* Identify persistence entries in `Run`, `RunOnce`, and `Services` registry keys.
* Add, query, and delete registry values using command-line tools.
* Export registry keys for forensic evidence preservation.
* Inspect the Winlogon Shell and Userinit keys for tampering.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 12 (Windows Registry Fundamentals).

---

# Clues

> **"Malware loves the `Run` key. If it's in `HKCU\...\Run`, it executes every time THAT user logs in. If it's in `HKLM\...\Run`, it executes for EVERY user."**

> **"Always export the key before deleting anything. If you break the registry, you need a backup to restore."**

---

# Your Tasks

### Task 1 — Plant the Persistence
Simulate the attacker by adding a malicious autorun entry. Open Command Prompt as Administrator:

```cmd
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemHealthCheck" /t REG_SZ /d "C:\Users\Public\SystemHealthCheck.exe" /f
```

---

### Task 2 — Hunt the Persistence (CMD)
As an investigator, your first check should always be the Run keys.
Query the current user's Run key:

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

Do you see the `SystemHealthCheck` entry?

---

### Task 3 — Check the System-Wide Run Key
The attacker might have planted persistence for ALL users too.

```cmd
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
```

---

### Task 4 — PowerShell Deep Inspection
Get a detailed view of all autorun entries using PowerShell:

```powershell
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
```

---

### Task 5 — Check the RunOnce Keys
Some malware uses `RunOnce` — it executes once and then the entry is automatically deleted, making it harder to find.

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce"
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce"
```

---

### Task 6 — Inspect the Winlogon Shell
The `Shell` value under Winlogon should ONLY be `explorer.exe`. If malware has modified it, the attacker's payload runs instead of (or alongside) the Windows desktop.

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
```

---

### Task 7 — Inspect Userinit
The `Userinit` value should ONLY be `C:\Windows\system32\userinit.exe,`. If it contains additional entries, a payload is being launched at every logon.

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit
```

---

### Task 8 — Export Evidence
Before removing anything, export the registry key as forensic evidence.

```cmd
reg export "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" C:\Evidence\HKCU_Run_Export.reg
```

---

### Task 9 — Eradicate the Persistence
Remove the malicious autorun entry:

```cmd
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemHealthCheck" /f
```

---

### Task 10 — Verify the Clean
Confirm the entry is gone:

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

The `SystemHealthCheck` entry should no longer appear.

---

# Success Criteria

You have successfully completed this lab if you can:

* Query the `Run`, `RunOnce`, `Winlogon\Shell`, and `Winlogon\Userinit` registry keys.
* Identify a malicious autorun entry planted by an attacker.
* Export a registry key to a `.reg` file before making changes.
* Successfully delete the malicious registry value and verify it's gone.

---

# 💙 Blue Team Insight

Registry-based persistence is the #1 technique used by commodity malware, RATs, and APT implants. During every incident response engagement, your first five minutes should include checking: `Run` keys (HKCU + HKLM), `RunOnce` keys, `Services`, `Winlogon\Shell`, and `Winlogon\Userinit`. Sysinternals **Autoruns** automates this entire process and highlights entries that are NOT digitally signed by Microsoft.

---

# Key Takeaways

After completing this lab, you should be able to:

* Navigate and query the Windows Registry from the command line.
* Identify and eradicate registry-based persistence mechanisms.
* Preserve forensic evidence by exporting registry keys before modification.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2010%20Solution.md)**
