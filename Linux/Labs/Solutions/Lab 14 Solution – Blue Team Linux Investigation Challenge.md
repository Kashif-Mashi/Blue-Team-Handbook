# Lab 14 Solution – Blue Team Linux Investigation Challenge

## Overview

This solution demonstrates one possible approach to completing **Lab 14 – Blue Team Linux Investigation Challenge**.

> **Note:** This lab combines the knowledge gained throughout the previous 13 labs. Some commands require **sudo** privileges. Outputs will vary depending on your Linux distribution and environment.

---

# Task 1 – Establish the Investigation Environment

### Approach

Record basic system information and create an investigation workspace to preserve evidence.

### Commands

Display current date and time:

```bash
date
```

Identify the logged-in user:

```bash
whoami
```

View the hostname:

```bash
hostname
```

Create the investigation workspace:

```bash
mkdir -p ~/Incident-2026/{Evidence,Logs,Reports}
```

Verify:

```bash
tree ~/Incident-2026
```

---

# Task 2 – Investigate User Accounts

### Approach

Review user accounts, administrative users, and group memberships.

### Commands

List users:

```bash
cat /etc/passwd
```

View sudo users:

```bash
getent group sudo
```

Display logged-in users:

```bash
who
```

View group memberships:

```bash
groups analyst1
```

---

# Task 3 – Examine File Permissions

### Approach

Review sensitive files and the evidence directory created in earlier labs.

### Commands

Check system files:

```bash
ls -l /etc/passwd
```

```bash
ls -l /etc/shadow
```

Review investigation directory:

```bash
ls -ld ~/Incident-2026
```

Correct permissions if required:

```bash
chmod 750 ~/Incident-2026
```
---

# Task 4 – Investigate Running Processes

### Approach

Identify resource-intensive or suspicious processes.

### Commands

View running processes:

```bash
ps aux
```

Monitor system activity:

```bash
top
```

Search for a specific process:

```bash
ps aux | grep sleep
```
---

# Task 5 – Examine Network Activity

### Approach

Review interfaces, ports, and active network connections.

### Commands

View interfaces:

```bash
ip addr
```

Display routing table:

```bash
ip route
```

View listening ports:

```bash
sudo ss -tulnp
```

Review active connections:

```bash
ss -tunap
```
# Task 6 – Analyze System Logs

### Approach

Review authentication and system logs to build an investigation timeline.

### Commands

Authentication logs:

```bash
sudo grep ssh /var/log/auth.log
```

Failed logins:

```bash
sudo grep "Failed" /var/log/auth.log
```

Sudo activity:

```bash
sudo grep sudo /var/log/auth.log
```

Recent journal entries:

```bash
journalctl -b
```

Reboot history:

```bash
last reboot
```
# Task 7 – Verify Software & System Security

### Approach

Review installed software, updates, services, and firewall configuration.

### Commands

Check updates:

```bash
sudo apt update
```

List upgradable packages:

```bash
apt list --upgradable
```

View running services:

```bash
systemctl --type=service
```

Check firewall:

```bash
sudo ufw status verbose
```

# Task 8 – Secure the System

### Approach

Apply basic hardening measures based on investigation findings.

### Commands

Remove unused packages:

```bash
sudo apt autoremove
```

Disable unnecessary services:

```bash
sudo systemctl disable apache2
```

Enable firewall:

```bash
sudo ufw enable
```

Correct permissions:

```bash
chmod 750 ~/Incident-2026
```

Generate a security report:

```bash
./system_check.sh
```
# Challenge Answers

| Challenge | Solution |
|-----------|----------|
| Build investigation workspace | `mkdir -p ~/Incident-2026/{Evidence,Logs,Reports}` |
| Audit users | `cat /etc/passwd`, `getent group sudo` |
| Investigate processes | `ps aux`, `top` |
| Review network connections | `ss -tunap`, `ss -tulnp` |
| Analyze authentication logs | `grep ssh /var/log/auth.log` |
| Verify installed software | `dpkg -l`, `apt list --upgradable` |
| Perform system hardening | Update packages, enable UFW, disable unused services, review permissions |
---

# Sample Incident Report

## Executive Summary

A security investigation was conducted after alerts indicated unusual login attempts, increased CPU usage, and unexpected network activity. The investigation identified normal administrative activity with no confirmed system compromise. Several hardening measures were applied to improve the server's security posture.

---

## Scope

- User Accounts
- File Permissions
- Running Processes
- Network Activity
- Authentication Logs
- Services
- Software Updates
- Firewall Configuration

---

## Evidence Collected

- Authentication logs
- Process list
- Network connections
- Running services
- Firewall status
- Package information

---

## Timeline

| Time | Event |
|------|-------|
| 03:17 | SOC alert received |
| 03:20 | Investigation workspace created |
| 03:30 | User accounts reviewed |
| 03:40 | Processes analyzed |
| 03:50 | Network connections reviewed |
| 04:00 | Authentication logs analyzed |
| 04:15 | Security hardening completed |

---

## Findings

- No unauthorized administrator accounts detected.
- SSH service operating normally.
- Firewall enabled.
- System packages updated.
- No unexpected listening ports identified.
- Investigation directory secured with appropriate permissions.

---

## Actions Taken

- Reviewed user accounts.
- Verified file permissions.
- Inspected running processes.
- Reviewed network activity.
- Examined authentication logs.
- Applied available updates.
- Removed unnecessary packages.
- Enabled firewall protection.

---

## Recommendations

- Continue regular log monitoring.
- Apply security updates promptly.
- Review firewall rules periodically.
- Audit user accounts regularly.
- Perform routine security assessments.
- Maintain regular backups.

---

## Lessons Learned

Following a structured investigation process makes it easier to identify suspicious activity, preserve evidence, and improve system security.

---

## 🎉 Lab Complete!

Congratulations! You have successfully completed **Lab 14 – Blue Team Linux Investigation Challenge**.

You should now be able to:

- Conduct a structured Linux security investigation.
- Preserve and collect digital evidence.
- Analyze users, processes, services, and network activity.
- Review authentication and system logs.
- Perform Linux system hardening.
- Produce a professional incident report suitable for SOC documentation.

**Congratulations on completing all 14 Linux Fundamentals labs in the Blue Team Handbook!**

Your next step is **Windows Fundamentals**, where you'll apply the same investigative mindset to Microsoft Windows environments.