# Windows 11 Quick Reference

A quick reference guide for the Windows 11 Installation & Configuration Guide.

---

# Virtual Machine

| Setting | Recommended |
|----------|-------------|
| Hypervisor | Oracle VirtualBox |
| Operating System | Windows 11 Pro |
| RAM | 4–8 GB |
| CPU | 2–4 Cores |
| Storage | 60 GB (Dynamic) |
| Video Memory | 128 MB |
| Network Adapter 1 | NAT |
| Network Adapter 2 | Host-Only |

---

# Default Lab Network

| Machine | Example IP |
|----------|------------|
| Ubuntu Server | 192.168.56.20 |
| Windows 11 | 192.168.56.30 |
| Kali Linux | 192.168.56.40 |

---

# Frequently Used Commands

## Network

```cmd
ipconfig
```

Display IP configuration.

```cmd
ipconfig /all
```

Display detailed network information.

```cmd
ping 192.168.56.20
```

Test connectivity.

```cmd
netstat -ano
```

Display active network connections.

```cmd
nslookup google.com
```

DNS lookup.

---

## PowerShell

```powershell
Get-Process
```

List running processes.

```powershell
Get-Service
```

Display services.

```powershell
Get-ComputerInfo
```

System information.

```powershell
Get-NetIPAddress
```

Network information.

---

# Administrative Tools

| Tool | Command |
|------|---------|
| Event Viewer | eventvwr.msc |
| Services | services.msc |
| Device Manager | devmgmt.msc |
| Computer Management | compmgmt.msc |
| Registry Editor | regedit |
| Local Security Policy* | secpol.msc |

*Windows Pro editions only.

---

# Useful Shortcuts

| Shortcut | Function |
|-----------|----------|
| Win + R | Run Dialog |
| Win + X | Power User Menu |
| Ctrl + Shift + Esc | Task Manager |
| Win + E | File Explorer |
| Win + I | Settings |
| Win + L | Lock Computer |

---

# Lab Checklist

- Windows Installed
- Guest Additions Installed
- Internet Working
- Host-Only Network Working
- Windows Updated
- Wazuh Agent Installed
- Snapshot Created