# Windows Fundamentals

<p align="center">
  <img src="../assets/Windows-Fundamentals.png" alt="Windows Fundamentals Banner" width="100%">
</p>

<p align="center">
  <strong>Master Windows Operating System Fundamentals for Blue Team Operations</strong>
</p>

<p align="center">
  Learn • Investigate • Secure • Defend
</p>

---

## 📖 Overview

Windows is the most widely used operating system in enterprise environments and a primary target for cyber threats. Whether you're an aspiring SOC Analyst, Blue Team Engineer, Incident Responder, or System Administrator, understanding Windows internals is an essential cybersecurity skill.

This module provides a hands-on, investigation-focused introduction to Windows. Instead of simply learning how to use Windows, you'll learn how it works, how attackers abuse it, and how defenders investigate and secure it.

Throughout this module, you'll work through practical labs that simulate real-world administrative and security tasks using built-in Windows tools.

> **No Windows Server Required**
>
> All labs are designed to run on a standard Windows 10 or Windows 11 system unless otherwise specified.

---

# 🎯 Learning Objectives

By completing this module, you will be able to:

- Understand Windows architecture and components
- Navigate the Windows file system
- Use Command Prompt and PowerShell
- Manage users and groups
- Investigate running processes and services
- Configure Windows networking
- Analyze Windows Event Logs
- Understand Windows Registry fundamentals
- Manage installed software
- Write basic PowerShell scripts
- Apply Windows security best practices
- Perform basic Blue Team investigations

---

# 📚 Module Structure

```
Windows/
│
├── README.md
├── Chapters/
├── Labs/
│   ├── Lab 01 Windows Installation
│   ├── Lab 02 File System Investigation
│   ├── Lab 03 CMD & PowerShell
│   ├── Lab 04 File Permissions
│   ├── Lab 05 Users & Groups
│   ├── Lab 06 Processes & Services
│   ├── Lab 07 Networking
│   ├── Lab 08 Event Viewer
│   ├── Lab 09 Windows Security
│   ├── Lab 10 Registry
│   ├── Lab 11 Software Management
│   ├── Lab 12 PowerShell Scripting
│   ├── Lab 13 Windows Hardening
│   └── Lab 14 Blue Team Investigation
│
├── Solutions/
├── Cheat-Sheets/
├── Commands/
├── Resources/
└── Screenshots/
```

---

# 📘 Chapters

| Chapter | Topic | Description |
|----------|-------|-------------|
| 01 | Windows Installation & Architecture | Learn Windows editions, architecture, boot process, and desktop environment. |
| 02 | Windows File System | Understand NTFS, files, folders, drives, hidden files, and navigation. |
| 03 | CMD & PowerShell | Learn essential Windows command-line tools and PowerShell basics. |
| 04 | File Permissions | Understand NTFS permissions, ownership, inheritance, and access control. |
| 05 | Users & Groups | Manage local users, groups, passwords, and administrative privileges. |
| 06 | Processes & Services | Explore Task Manager, Windows services, startup programs, and process management. |
| 07 | Networking | Learn TCP/IP configuration, DNS, ports, network troubleshooting, and connectivity testing. |
| 08 | Event Viewer | Analyze Windows logs and investigate system and security events. |
| 09 | Windows Security | Explore Windows Defender, Firewall, User Account Control (UAC), and BitLocker. |
| 10 | Registry | Learn Registry structure, startup locations, and safe registry investigation. |
| 11 | Software Management | Install, update, remove, and manage Windows applications. |
| 12 | PowerShell Scripting | Automate administrative tasks using PowerShell scripts. |
| 13 | Windows Hardening | Apply security best practices to strengthen Windows systems. |
| 14 | Blue Team Investigation | Perform a complete Windows security investigation using knowledge gained throughout the module. |

---

# 🧪 Hands-on Labs

Every chapter includes a practical lab.

| Lab | Practical Exercise |
|------|--------------------|
| Lab 01 | Windows Installation |
| Lab 02 | File System Investigation |
| Lab 03 | CMD & PowerShell |
| Lab 04 | File Permissions |
| Lab 05 | Users & Groups |
| Lab 06 | Processes & Services |
| Lab 07 | Networking |
| Lab 08 | Event Viewer |
| Lab 09 | Windows Security |
| Lab 10 | Registry Investigation |
| Lab 11 | Software Management |
| Lab 12 | PowerShell Scripting |
| Lab 13 | Windows Hardening |
| Lab 14 | Blue Team Investigation Challenge |

Each lab contains:

- Learning Objectives
- Scenario
- Step-by-Step Instructions
- Practical Exercises
- Challenges
- Verification
- Screenshots
- Cleanup Instructions

---

# 📂 Additional Resources

## 📄 Solutions

Complete walkthroughs for every lab with:

- Commands
- Screenshots
- Challenge answers
- Explanations

---

## 📑 Cheat Sheets

Quick reference guides covering:

- CMD Commands
- PowerShell Commands
- Event Viewer
- Registry
- Networking
- Windows Security

---

## 💻 Commands

A collection of commonly used Windows commands including:

### Command Prompt

- `dir`
- `cd`
- `tree`
- `whoami`
- `hostname`
- `systeminfo`
- `tasklist`
- `taskkill`
- `ipconfig`
- `ping`
- `tracert`
- `netstat`

### PowerShell

- `Get-Process`
- `Get-Service`
- `Get-EventLog`
- `Get-ChildItem`
- `Get-NetIPConfiguration`
- `Get-NetFirewallRule`
- `Get-LocalUser`
- `Get-LocalGroup`

---

## 📚 Resources

Additional learning resources including:

- Microsoft Learn
- Microsoft Documentation
- Sysinternals Suite
- Windows Security Documentation
- PowerShell Documentation
- Blue Team References

---

## 📸 Screenshots

Every lab includes screenshots to help learners verify their progress and compare expected results.

---

# 🛡️ Blue Team Skills Covered

By completing this module, you'll develop practical experience with:

- Windows Administration
- Windows Security
- Windows Logging
- Event Analysis
- User Management
- Process Investigation
- Service Analysis
- File Permission Auditing
- Registry Investigation
- PowerShell Automation
- Network Troubleshooting
- Endpoint Hardening

---

# 💻 Recommended Environment

| Requirement | Recommendation |
|-------------|----------------|
| Operating System | Windows 10 or Windows 11 |
| RAM | 8 GB or higher |
| Storage | 20 GB free space |
| Administrator Access | Recommended |
| Internet Connection | Optional |

> **Note:** Windows Server is **not required** for this module. All exercises are designed to work on a standard Windows workstation.

---

# ⚠️ Safety Notice

Some labs involve modifying Windows settings such as:

- User accounts
- NTFS permissions
- Firewall rules
- Registry keys
- Services
- Scheduled tasks

Always read each lab carefully and complete the **Cleanup** section to restore your system to its original state.

No malware or destructive techniques are used in this module.

---

# 🎓 Prerequisites

Before starting this module, it is recommended that you complete:

- Computer Fundamentals
- Networking Fundamentals
- Linux Fundamentals

These topics provide a solid foundation for understanding Windows security and system administration.

---

# 🚀 What's Next?

After completing **Windows Fundamentals**, continue your Blue Team journey with:

- PowerShell for Blue Teams
- Active Directory Fundamentals
- Windows Event Logging
- Sysinternals
- Sysmon
- Wazuh
- Microsoft Sentinel
- Splunk
- Threat Detection
- Incident Response
- Digital Forensics

---

# 🤝 Contributing

Contributions are welcome!

You can help by:

- Reporting issues
- Improving documentation
- Adding screenshots
- Creating new labs
- Fixing errors
- Enhancing explanations

Please open an Issue or submit a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">

**Understand • Investigate • Secure • Defend**

**Blue Team Handbook – Windows Fundamentals**

</p>