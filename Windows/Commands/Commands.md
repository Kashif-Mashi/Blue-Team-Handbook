# Windows Commands Reference

A quick reference guide for commonly used Windows commands used throughout the Windows Fundamentals module.

---

# System Information

| Command | Description |
|----------|-------------|
| hostname | Display computer name |
| whoami | Show current logged-in user |
| systeminfo | Display detailed system information |
| ver | Display Windows version |
| winver | Show Windows version dialog |

---

# File & Directory Management

| Command | Description |
|----------|-------------|
| dir | List files and folders |
| cd | Change directory |
| mkdir | Create a directory |
| rmdir | Remove a directory |
| copy | Copy files |
| move | Move files |
| del | Delete files |
| ren | Rename files |
| tree | Display folder structure |

---

# User Management

| Command | Description |
|----------|-------------|
| net user | Display local users |
| net user username | Display user information |
| net localgroup | Display local groups |
| whoami /groups | Display current user groups |

---

# Networking

| Command | Description |
|----------|-------------|
| ipconfig | Show IP configuration |
| ipconfig /all | Detailed IP configuration |
| ipconfig /release | Release DHCP address |
| ipconfig /renew | Renew DHCP address |
| ping | Test connectivity |
| tracert | Trace network path |
| pathping | Combined ping & tracert |
| nslookup | DNS lookup |
| arp -a | Display ARP cache |
| netstat -ano | Show active connections |
| route print | Display routing table |

---

# Process Management

| Command | Description |
|----------|-------------|
| tasklist | Display running processes |
| taskkill /PID PID | Terminate process |
| taskkill /IM process.exe | Kill process by name |

---

# Services

| Command | Description |
|----------|-------------|
| sc query | List services |
| sc start ServiceName | Start service |
| sc stop ServiceName | Stop service |
| net start | Show running services |

---

# Event Logs

| Command | Description |
|----------|-------------|
| eventvwr | Open Event Viewer |
| wevtutil el | List logs |
| wevtutil qe Security | Query Security log |

---

# PowerShell

| Command | Description |
|----------|-------------|
| Get-Process | List processes |
| Get-Service | List services |
| Get-EventLog | View event logs |
| Get-ChildItem | List files |
| Get-LocalUser | List users |
| Get-LocalGroup | List groups |
| Get-NetIPAddress | Display IP addresses |
| Get-NetFirewallRule | View firewall rules |

---

# Registry

| Command | Description |
|----------|-------------|
| reg query | Query registry |
| reg add | Add registry key |
| reg delete | Delete registry key |

---

# Firewall

| Command | Description |
|----------|-------------|
| netsh advfirewall show allprofiles | Display firewall status |
| netsh advfirewall firewall show rule name=all | Show firewall rules |

---

# System Maintenance

| Command | Description |
|----------|-------------|
| sfc /scannow | System File Checker |
| DISM /Online /Cleanup-Image /RestoreHealth | Repair Windows image |
| chkdsk | Check disk health |

---

# Useful Shortcuts

| Shortcut | Description |
|----------|-------------|
| Win + R | Run dialog |
| Win + X | Power User Menu |
| Win + E | File Explorer |
| Ctrl + Shift + Esc | Task Manager |
| Win + L | Lock computer |
| Win + I | Settings |
| Win + S | Windows Search |

---

> These commands are used throughout the Windows Fundamentals labs.