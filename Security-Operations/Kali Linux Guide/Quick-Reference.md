# Kali Linux Quick Reference

This document provides a quick overview of the most important configuration details covered in this guide.

---

# Lab Configuration

| Component | Value |
|----------|-------|
| Operating System | Kali Linux Rolling |
| Virtualization | Oracle VirtualBox |
| RAM | 4 GB |
| CPU | 2 vCPUs |
| Storage | 80 GB Dynamic |
| Adapter 1 | NAT |
| Adapter 2 | Host-Only |

---

# Recommended IP Addressing

| Machine | IP Address |
|----------|------------|
| Windows Host | 192.168.56.1 |
| Ubuntu Server | 192.168.56.10 |
| Wazuh Server | 192.168.56.20 |
| Kali Linux | 192.168.56.30 |

---

# Important Directories

| Path | Description |
|------|-------------|
| /home/username | User Home Directory |
| /etc/apt/sources.list | Package Repositories |
| /etc/ssh/sshd_config | SSH Configuration |
| /etc/hosts | Local Host Mapping |
| /var/log | System Logs |
| /tmp | Temporary Files |

---

# Home Lab Workflow

```text
Download Kali
      ↓
Create VM
      ↓
Install Kali
      ↓
Update System
      ↓
Configure Network
      ↓
Enable SSH
      ↓
Install Common Utilities
      ↓
Verify Connectivity
      ↓
Ready for Blue Team Lab
```

---

# VirtualBox Configuration

| Setting | Value |
|---------|-------|
| Firmware | BIOS |
| Video Memory | 128 MB |
| Graphics Controller | VMSVGA |
| Clipboard | Bidirectional |
| Drag & Drop | Bidirectional |

---

# Important Services

| Service | Purpose |
|----------|---------|
| ssh | Remote Access |
| NetworkManager | Network Configuration |

---

# Update Schedule

| Task | Frequency |
|------|-----------|
| apt update | Weekly |
| full-upgrade | Weekly |
| autoremove | Monthly |
| clean | Monthly |
| Snapshot | Before Major Changes |

---

This quick reference is intended to be used alongside the full installation guide.