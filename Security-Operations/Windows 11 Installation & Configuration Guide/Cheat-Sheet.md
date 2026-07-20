# Windows 11 Cheat Sheet

A quick cheat sheet for Windows administration and Blue Team operations.

---

# Essential Windows Tools

| Tool | Purpose |
|------|----------|
| Event Viewer | View system and security logs |
| Windows Security | Endpoint protection |
| Task Manager | Monitor processes |
| Services | Manage Windows services |
| Device Manager | Hardware management |
| PowerShell | Automation & administration |
| Command Prompt | System administration |

---

# Common Commands

## Networking

```cmd
ipconfig
ping
netstat
route print
nslookup
```

---

## System Information

```cmd
systeminfo
hostname
whoami
```

---

## PowerShell

```powershell
Get-Process
Get-Service
Get-ComputerInfo
Get-NetIPAddress
```

---

# Important Windows Locations

| Location | Purpose |
|----------|---------|
| C:\Windows | Operating System |
| C:\Users | User Profiles |
| C:\Program Files | Installed Applications |
| C:\ProgramData | Shared Application Data |
| C:\Windows\System32 | Windows System Files |

---

# Blue Team Workflow

```
Windows

↓

Generate Logs

↓

Wazuh Agent

↓

Wazuh Server

↓

SOC Dashboard

↓

Investigation
```

---

# Recommended Learning Order

1. Windows Administration
2. Event Viewer
3. Networking
4. PowerShell
5. Wazuh
6. Sysmon
7. Sigma Rules
8. Threat Hunting