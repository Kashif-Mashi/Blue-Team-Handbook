# Solution — Lab 10: Windows Registry

> This solution walks through the CEO Laptop Registry Persistence Hunt, demonstrating how to locate, document, and eradicate a malicious autorun entry.

---

# Task 1 — Plant the Persistence

## Steps

```cmd
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemHealthCheck" /t REG_SZ /d "C:\Users\Public\SystemHealthCheck.exe" /f
```

### Investigation Note
The `/f` flag forces the addition without prompting. This simulates an attacker silently adding a Run key entry that will execute `SystemHealthCheck.exe` from `C:\Users\Public\` every time the CEO logs in.

---

# Task 2 — Hunt the Persistence (CMD)

## Steps

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

### Example Output

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    SecurityHealth    REG_EXPAND_SZ    %ProgramFiles%\Windows Defender\MSASCuiL.exe
    SystemHealthCheck    REG_SZ    C:\Users\Public\SystemHealthCheck.exe
```

### Investigation Note
The `SystemHealthCheck` entry is clearly visible. Notice that it points to `C:\Users\Public\` — this is a world-writable directory. No legitimate application installs its binary there. This is a classic indicator of a malicious payload planted for persistence.

---

# Task 3 — Check the System-Wide Run Key

## Steps

```cmd
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
```

### Investigation Note
In our simulation, we only planted the persistence in `HKCU`. In a real attack, always check BOTH `HKCU` and `HKLM` Run keys. `HKLM` entries execute for ALL users who log into the machine.

---

# Task 4 — PowerShell Deep Inspection

## Steps

```powershell
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
```

### Investigation Note
PowerShell returns the values as object properties, making it easy to pipe into `Select-Object`, `Export-Csv`, or `ConvertTo-Json` for automated analysis and reporting.

---

# Task 5 — Check the RunOnce Keys

## Steps

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce"
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce"
```

### Investigation Note
`RunOnce` entries are particularly sneaky: they execute once at the next logon, then the entry is automatically deleted from the registry. If you check the `RunOnce` key AFTER the malware has already run, it will be empty — the evidence is gone. This is why Sysmon Event ID 13 (real-time registry monitoring) is essential.

---

# Task 6 — Inspect the Winlogon Shell

## Steps

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
```

### Expected Output

```
    Shell    REG_SZ    explorer.exe
```

### Investigation Note
This value should ONLY be `explorer.exe`. If it reads something like `explorer.exe, C:\Temp\backdoor.exe`, the attacker's payload launches alongside the Windows desktop. Some malware replaces `explorer.exe` entirely, causing the desktop to never load while the malware runs in its place.

---

# Task 7 — Inspect Userinit

## Steps

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit
```

### Expected Output

```
    Userinit    REG_SZ    C:\Windows\system32\userinit.exe,
```

### Investigation Note
The trailing comma is normal. If additional paths appear after the comma (e.g., `C:\Windows\system32\userinit.exe, C:\Temp\malware.exe`), the attacker has planted persistence in the Winlogon initialization chain.

---

# Task 8 — Export Evidence

## Steps

```cmd
reg export "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" C:\Evidence\HKCU_Run_Export.reg
```

### Investigation Note
Always export before deleting. The `.reg` file is a human-readable text file that serves as forensic evidence. It can be imported back to restore the key if needed, and it documents exactly what was present at the time of investigation.

---

# Task 9 — Eradicate the Persistence

## Steps

```cmd
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemHealthCheck" /f
```

### Investigation Note
The `/f` flag forces deletion without prompting. After this command, the malware will NOT execute on the next logon. However, the malware binary itself (`SystemHealthCheck.exe`) is still on disk in `C:\Users\Public\`. In a real incident, you must also delete the binary and search for additional persistence mechanisms.

---

# Task 10 — Verify the Clean

## Steps

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

### Investigation Note
The `SystemHealthCheck` entry should no longer appear. Only legitimate entries (like `SecurityHealth` for Windows Defender) should remain.

---

# Scenario Conclusion

By systematically checking the `Run`, `RunOnce`, `Winlogon\Shell`, and `Winlogon\Userinit` registry keys, you successfully identified the malicious persistence mechanism on the CEO's laptop. After exporting the evidence and removing the entry, the malware will no longer auto-execute on logon. In a production incident, you would also quarantine the binary, submit it for analysis, and search for lateral movement across other endpoints.
