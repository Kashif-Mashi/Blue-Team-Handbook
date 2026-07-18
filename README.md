<p align="center">
  <img src="assets/banner.png" alt="Blue Team Handbook Banner" width="100%">
</p>
# 🛡️ Blue Team Handbook

A practical, beginner-friendly cybersecurity handbook focused on **Blue Team operations**, **Security Operations Center (SOC)** concepts, and **hands-on lab implementation**.

This repository documents my journey of learning cybersecurity by building a complete Blue Team home lab from scratch. Instead of only sharing notes, it provides practical guides, diagrams, troubleshooting steps, and real-world lab exercises that anyone can follow.

---

## 📖 About

The goal of this repository is to provide a structured learning path for aspiring SOC Analysts, cybersecurity students, and anyone interested in defensive security.

The handbook combines:

- 📚 Theory and concepts
- 🖥️ Practical home lab setup
- 📄 Step-by-step installation guides
- 🔍 Troubleshooting
- 📝 Commands with explanations
- 📊 Architecture diagrams
- 📸 Screenshots and expected outputs

Everything included here has been tested in my own home lab.

---

# 📂 Repository Structure

```text
Blue-Team-Handbook
│
├── Foundation
│   ├── CISSP and 8 Security Domains
│   ├── NIST Cybersecurity Framework
│   ├── Understanding Logs and SIEM Theory
│   ├── Linux Fundamentals (Future)
│   ├── Networking Fundamentals (Future)
│   └── Windows Fundamentals (Future)
│
├── Security-Operations
│   │
│   ├── Ubuntu Server
│   │
│   ├── Kali Linux
│   │
│   ├── Wazuh
│   │
│   ├── Windows Agent
│   │
│   ├── Linux Agent
│   │
│   └── Active Directory (Future)
│
├── Resources
│   ├── Command Cheat Sheet
│   ├── Troubleshooting
│   ├── Useful Resources
│   └── Glossary
│
└── README.md
```

---

# 🎯 Learning Objectives

This handbook covers:

- Blue Team Fundamentals
- SOC Fundamentals
- Linux Basics
- Networking Fundamentals
- Log Analysis
- SIEM Concepts
- Wazuh
- Endpoint Monitoring
- Threat Detection
- Incident Response
- Home Lab Deployment

---

# 🧪 Home Lab

The practical exercises are performed in a virtual lab built using VirtualBox.

```text
Internet
    │
Home Router
    │
Host Computer
    │
VirtualBox
    │
──────────────────────────
NAT Network
──────────────────────────
        │
 Ubuntu Server
 (Internet Access)

──────────────────────────
Host-Only Network
192.168.56.0/24
──────────────────────────

Ubuntu Server
192.168.56.10

Windows 11
192.168.56.20

Kali Linux
192.168.56.30
```

---

# 📚 Current Guides

## Foundation

- CISSP & 8 Security Domains
- NIST Cybersecurity Framework
- Understanding Logs and SIEM Theory

---

## Security Operations

### Wazuh

- Introduction
- Home Lab Planning
- VirtualBox Configuration
- Ubuntu Server Installation
- Networking Configuration
- SSH Configuration
- Wazuh Installation
- Agent Enrollment *(In Progress)*
- Dashboard Configuration *(Coming Soon)*

---

# 🚧 Roadmap

- [x] Foundation Notes
- [x] Wazuh Introduction
- [x] Lab Planning
- [x] Ubuntu Installation
- [x] Networking Configuration
- [x] SSH Configuration
- [ ] Wazuh Dashboard
- [ ] Windows Agent
- [ ] Linux Agent
- [ ] Active Directory Integration
- [ ] Sysmon
- [ ] Sigma Rules
- [ ] Threat Hunting
- [ ] Incident Response
- [ ] Detection Engineering

---

# 💻 Technologies Used

- Ubuntu Server 22.04 LTS
- Kali Linux
- Windows 11
- VirtualBox
- Wazuh
- Linux
- Bash
- SSH

---

# 🤝 Contributing

Suggestions, corrections, and improvements are always welcome.

If you find any mistakes or have ideas to improve the handbook, feel free to open an Issue or submit a Pull Request.

---

# 📌 Disclaimer

This repository is intended for educational purposes only.

All demonstrations, configurations, and practical exercises are performed in a personal home lab environment.

Do not use these techniques on systems that you do not own or have explicit permission to test.

---

# 👨‍💻 Author

**Kashif Mashi**

- GitHub: https://github.com/kashifkhanamv123-cmd
- LinkedIn: *(https://www.linkedin.com/in/kashif-masih-79b8813b7/)*

---

## ⭐ Support

If you find this repository useful, consider giving it a **Star ⭐**.

It helps others discover the project and motivates me to continue improving the handbook.
