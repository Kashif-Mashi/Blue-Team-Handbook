# Windows Cheat Sheet

Quick reference for Blue Team analysts.

---

# Important Windows Directories

| Directory | Purpose |
|------------|----------|
| C:\Windows | Windows installation |
| C:\Windows\System32 | System files |
| C:\Program Files | Installed applications |
| C:\Users | User profiles |
| C:\Users\Public | Shared user files |
| C:\Temp | Temporary files |

---

# Windows Event Logs

| Log | Description |
|------|-------------|
| Application | Application events |
| Security | Authentication and security |
| Setup | Installation events |
| System | Operating system events |
| Forwarded Events | Remote logs |

---

# Useful Event IDs

| Event ID | Description |
|-----------|-------------|
| 4624 | Successful Logon |
| 4625 | Failed Logon |
| 4634 | User Logoff |
| 4648 | Explicit Credential Logon |
| 4672 | Special Privileges Assigned |
| 4688 | Process Created |
| 4689 | Process Terminated |
| 4720 | User Account Created |
| 4726 | User Account Deleted |
| 4732 | User Added to Group |
| 4733 | User Removed from Group |

---

# PowerShell Execution Policy

| Command | Purpose |
|----------|---------|
| Get-ExecutionPolicy | Check policy |
| Set-ExecutionPolicy RemoteSigned | Change policy |

---

# File Permissions

Permission Types:

- Full Control
- Modify
- Read & Execute
- Read
- Write

---

# Windows Startup Locations

- Startup Folder
- Task Scheduler
- Registry Run Keys
- Services

---

# Registry Hives

| Hive | Description |
|------|-------------|
| HKLM | Local Machine |
| HKCU | Current User |
| HKCR | Classes Root |
| HKU | Users |
| HKCC | Current Configuration |

---

# Networking Commands

- ipconfig
- ping
- tracert
- nslookup
- netstat
- arp

---

# Investigation Tools

- Event Viewer
- Task Manager
- Resource Monitor
- Services
- Registry Editor
- Windows Security
- Windows Firewall

---

# PowerShell Essentials

```powershell
Get-Help
Get-Process
Get-Service
Get-EventLog
Get-ChildItem
Get-NetIPAddress
```

---

# Blue Team Investigation Workflow

1. Identify
2. Collect Evidence
3. Analyze
4. Contain
5. Eradicate
6. Recover
7. Document

---

# Common File Extensions

| Extension | Type |
|------------|------|
| .exe | Executable |
| .dll | Dynamic Library |
| .sys | Driver |
| .ps1 | PowerShell Script |
| .bat | Batch File |
| .cmd | Command Script |
| .log | Log File |

---

# Built-in Security Features

- Windows Defender
- Firewall
- SmartScreen
- BitLocker
- User Account Control (UAC)
- Windows Update

---

> Keep this cheat sheet handy while completing the Windows Fundamentals labs.