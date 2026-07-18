# Wazuh Quick Reference

This document provides a quick overview of the most important Wazuh deployment information covered in this guide.

---

# Lab Configuration

| Component | Value |
|-----------|-------|
| Operating System | Ubuntu Server 22.04 LTS |
| Deployment | Single Node |
| Virtualization | Oracle VirtualBox |
| RAM | 8 GB Recommended |
| CPU | 4 vCPUs Recommended |
| Storage | 80 GB |
| Network | NAT + Host-Only |

---

# Recommended IP Addressing

| Machine | IP Address |
|----------|------------|
| Windows Host | 192.168.56.1 |
| Ubuntu Server | 192.168.56.10 |
| Wazuh Server | 192.168.56.20 |
| Kali Linux | 192.168.56.30 |

---

# Wazuh Components

| Component | Purpose |
|-----------|---------|
| Wazuh Manager | Collects and analyzes security events |
| Wazuh Indexer | Stores and indexes security data |
| Wazuh Dashboard | Web interface for monitoring |
| Wazuh Agent | Collects logs from endpoints |

---

# Important Directories

| Path | Description |
|------|-------------|
| /var/ossec | Wazuh Installation Directory |
| /var/ossec/etc | Configuration Files |
| /var/ossec/logs | Wazuh Logs |
| /etc/systemd/system | System Services |

---

# Common Ports

| Port | Service |
|------|---------|
| 443 | Dashboard HTTPS |
| 1514 | Agent Communication |
| 1515 | Agent Registration |
| 55000 | Wazuh API |

---

# Deployment Workflow

```text
Prepare Ubuntu Server
        ↓
Install Wazuh
        ↓
Access Dashboard
        ↓
Configure Manager
        ↓
Deploy Agents
        ↓
Monitor Logs
        ↓
Blue Team Ready
```

---

# Services

- wazuh-manager
- wazuh-indexer
- wazuh-dashboard

---

This quick reference is intended to be used alongside the full deployment guide.