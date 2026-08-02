<p align="center">
  <img src="assets/banner.png" alt="Blue Team Handbook" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-3b82f6?style=for-the-badge&logo=linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/Focus-Blue%20Team%20%7C%20SOC-0ea5e9?style=for-the-badge" alt="Focus">
  <img src="https://img.shields.io/badge/Level-Beginner%20Friendly-a855f7?style=for-the-badge" alt="Level">
  <img src="https://img.shields.io/badge/Status-Active%20Development-f97316?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/github/stars/kashifkhanamv123/Blue-Team-Handbook?style=for-the-badge&logo=github&color=eab308" alt="Stars">
</p>

<p align="center">
  <strong>A free, open-source learning platform for aspiring SOC Analysts and Blue Team professionals.</strong><br>
  Structured theory &nbsp;&middot;&nbsp; Practical labs &nbsp;&middot;&nbsp; Home lab projects &nbsp;&middot;&nbsp; Cheat sheets &nbsp;&middot;&nbsp; Real-world documentation.
</p>

---

## Table of Contents

- [Introduction](#introduction)
- [Why Blue-Team-Handbook?](#why-blue-team-handbook)
- [Features](#features)
- [Learning Roadmap](#-blue-team-learning-roadmap)
- [Home Lab Architecture](#-home-lab-architecture)
- [Repository Structure](#repository-structure)
- [Learning Modules](#learning-modules)
- [Learning Outcomes](#learning-outcomes)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Repository Progress](#repository-progress)
- [Contributing](#contributing)
- [License](#license)
- [Support the Project](#support-the-project)
- [Connect](#connect)

---

## Introduction

**Blue-Team-Handbook** is a structured, community-driven learning resource built for individuals who want to enter the cybersecurity field as SOC Analysts, Incident Responders, Threat Hunters, or Detection Engineers.

This handbook combines foundational theory with step-by-step practical guides, hands-on home lab projects, and real-world tooling experience — everything you need to build defensive security skills from the ground up.

Whether you are a complete beginner, a student, an IT professional making a career pivot, or a self-taught learner — this handbook provides a clear, structured path to Blue Team readiness.

---

## Why Blue-Team-Handbook?

The cybersecurity skills gap is real. Entry-level job postings expect candidates to already know enterprise tools, SIEM platforms, detection logic, and incident response workflows — but most free resources are fragmented, outdated, or assume prior knowledge.

**Blue-Team-Handbook solves this by:**

| Problem | Solution |
|---|---|
| No clear learning path | Structured, sequential modules from fundamentals to advanced topics |
| Theory without practice | Every module includes hands-on labs and home lab projects |
| Expensive certifications | Completely free and open-source |
| Fragmented documentation | Single, cohesive repository covering the full Blue Team skill set |
| Intimidating tooling | Step-by-step deployment guides with screenshots and explanations |

> **Who is this for?**
> Students &nbsp;&middot;&nbsp; Career changers &nbsp;&middot;&nbsp; IT professionals upskilling &nbsp;&middot;&nbsp; Self-taught learners &nbsp;&middot;&nbsp; Anyone preparing for SOC Analyst roles.

---

## Features

- **Structured Learning Path** — A sequential roadmap from cybersecurity fundamentals to advanced Blue Team operations
- **Hands-On Labs** — Practical exercises designed to reinforce every concept
- **Home Lab Projects** — Complete deployment guides for building a functional security operations lab
- **Cheat Sheets** — Quick-reference cards for Linux, Windows, SIEM queries, and Blue Team tools
- **SIEM & Detection Content** — Real Wazuh rules, detection logic, and monitoring configurations
- **Beginner Friendly** — Every guide assumes no prior experience; all commands are explained
- **Open Source** — Free forever, community contributions welcome
- **Recruiter Ready** — Designed so learners build a documented portfolio of practical skills

---

## 📚 Blue Team Learning Roadmap

The following roadmap defines the recommended learning sequence through this handbook. Each stage builds directly on the previous one.

![Blue Team Learning Roadmap](assets/Learning%20-Roadmap.svg)

> **Recommended Order:** Work through modules sequentially. Each section introduces prerequisite knowledge for the next.

---

## 🏗️ Home Lab Architecture

The home lab replicates a real-world security operations environment using virtualization software (VirtualBox or VMware). It includes a SIEM platform, monitored endpoints, and an attacker machine for realistic threat simulation.

![Wazuh Home Lab Architecture](assets/Wazuh-Security-%20Framework.svg)

**Lab Components:**

| Component | Role |
|---|---|
| Wazuh Manager (Ubuntu Server) | SIEM and XDR platform |
| Windows 11 Endpoint | Monitored workstation with Wazuh agent |
| Kali Linux | Attacker machine for controlled threat simulation |
| Ubuntu Server | Linux endpoint and lab infrastructure |

---

## Repository Structure

```
Blue-Team-Handbook/
│
├── Foundation/                          # Cybersecurity fundamentals and OS basics
│   ├── Operating System Fundamentals/
│   ├── CISSP and 8 Security Domains.pdf
│   ├── NIST Cybersecurity Framework.pdf
│   └── Understanding Logs and SIEM Theory.pdf
│
├── Linux/                               # Linux fundamentals for security professionals
│   ├── Fundamentals/                    # Chapter-by-chapter theory
│   ├── Labs/                            # Hands-on lab exercises
│   ├── Cheat-Sheets/                    # Quick-reference command sheets
│   ├── Resources/                       # External references and documentation
│   └── README.md
│
├── Security-Operations/                 # Security operations and home lab guides
│   ├── Kali Linux Guide/
│   ├── Ubuntu Server Guide/
│   ├── Wazuh Deployment Guide/
│   └── Windows 11 Installation & Configuration Guide/
│
├── assets/                              # Diagrams, banners, and visual assets
│   ├── banner.png
│   ├── Learning-Roadmap.svg
│   └── Wazuh-Security-Framework.svg
│
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── FAQ.md
├── LICENSE
├── PROJECT_STRUCTURE.md
├── SECURITY.md
└── SUPPORT.md
```

---

## Learning Modules

<details>
<summary><strong>🔐 Module 1 — Cybersecurity Foundations</strong></summary>
<br>

Understand the core principles of cybersecurity before touching any tools.

**Topics covered:**
- The CIA Triad (Confidentiality, Integrity, Availability)
- NIST Cybersecurity Framework
- CISSP Security Domains overview
- Threat actors, attack types, and attack surfaces
- Introduction to logs, events, and SIEM theory
- Networking fundamentals for security professionals

**Resources included:**
- `NIST Cybersecurity Framework.pdf`
- `CISSP and 8 Security Domains.pdf`
- `Understanding Logs and SIEM Theory.pdf`

📁 [Foundation Module →](Foundation/)

</details>

<details>
<summary><strong>🐧 Module 2 — Linux Fundamentals</strong></summary>
<br>

Linux powers most servers, cloud environments, and cybersecurity platforms. This module builds the command-line confidence required for every defensive security role.

**Topics covered:**

| Chapter | Topic |
|---|---|
| 01 | Introduction to Linux |
| 02 | Installing Linux |
| 03 | Linux File System |
| 04 | Shell & Terminal Basics |
| 05 | Navigation Commands |
| 06 | File & Directory Management |
| 07 | Users & Groups |
| 08 | Permissions & Ownership |
| 09 | Processes & Services |
| 10 | Networking Basics |
| 11 | Logging & Monitoring |
| 12 | Package Management |
| 13 | Bash Scripting Basics |
| 14 | Linux Security Fundamentals |

📁 [Linux Module →](Linux/README.md)

</details>

<details>
<summary><strong>🪟 Module 3 — Windows Fundamentals</strong></summary>
<br>

The majority of enterprise environments run Windows. This module covers Windows administration concepts directly relevant to SOC and Blue Team work.

**Topics covered:**
- Windows 11 installation and initial configuration
- Windows file system, registry, and architecture
- User account management and Active Directory fundamentals
- Windows Event Logging and log locations
- Group Policy and security hardening

📁 [Security Operations →](Security-Operations/)

</details>

<details>
<summary><strong>🛡️ Module 4 — Security Operations</strong></summary>
<br>

Build and operate a functional security operations home lab. This module provides complete, step-by-step deployment guides for every component.

**Guides included:**
- Ubuntu Server — deployment and hardening
- Windows 11 — installation and security configuration
- Kali Linux — attacker machine setup
- Wazuh — full SIEM/XDR deployment guide

📁 [Security Operations →](Security-Operations/)

</details>

<details>
<summary><strong>📡 Module 5 — Wazuh SIEM</strong></summary>
<br>

Wazuh is an open-source XDR and SIEM platform used in real enterprise environments. This module covers a complete deployment and operational workflow.

**Topics covered:**
- Wazuh Manager installation on Ubuntu Server
- Agent deployment on Windows and Linux endpoints
- Log collection, normalization, and alert management
- Built-in detection rules and decoders
- Dashboard configuration
- File Integrity Monitoring (FIM)

📁 [Wazuh Deployment Guide →](Security-Operations/Wazuh%20Deployment%20Guide/)

</details>

<details>
<summary><strong>🔍 Module 6 — Threat Detection</strong> &nbsp;<em>(Upcoming)</em></summary>
<br>

Learn to identify malicious activity using detection rules, log analysis, and security tooling.

**Planned topics:**
- Sysmon installation and configuration
- Windows Event Log analysis
- Sigma rules — writing and deploying detection logic
- YARA rule fundamentals
- File Integrity Monitoring strategies

</details>

<details>
<summary><strong>🎯 Module 7 — Threat Hunting</strong> &nbsp;<em>(Upcoming)</em></summary>
<br>

Move beyond reactive alerting into proactive, hypothesis-driven threat hunting.

**Planned topics:**
- Threat hunting methodology
- MITRE ATT&CK framework — tactics, techniques, and procedures
- IOC and TTP-based hunting
- Log analysis and correlation techniques
- Hunting workflows in Wazuh and open-source platforms

</details>

<details>
<summary><strong>🚨 Module 8 — Incident Response</strong> &nbsp;<em>(Upcoming)</em></summary>
<br>

Learn the structured process for responding to security incidents following industry-standard frameworks.

**Planned topics:**
- NIST Incident Response Lifecycle
- Evidence collection and chain of custody
- Malware investigation fundamentals
- Memory analysis
- Incident documentation and reporting

</details>

<details>
<summary><strong>⚙️ Module 9 — Detection Engineering</strong> &nbsp;<em>(Upcoming)</em></summary>
<br>

Build detection logic that scales — from individual Sigma rules to structured detection pipelines.

**Planned topics:**
- Detection engineering methodology
- Writing and testing Sigma rules
- MITRE ATT&CK-aligned detection coverage
- Alert tuning and false positive reduction
- Detection-as-code concepts

</details>

<details>
<summary><strong>🧑‍💼 Module 10 — Blue Team / SOC Analyst</strong> &nbsp;<em>(Upcoming)</em></summary>
<br>

Integrate everything into the day-to-day workflow of a Security Operations Center analyst.

**Planned topics:**
- SOC analyst workflows and alert triage processes
- Alert investigation and escalation methodology
- Communication and documentation standards
- SOC metrics and reporting
- Career preparation — certifications, resume, and portfolio guidance

</details>

---

## Learning Outcomes

After completing this handbook, you will be able to:

- **Deploy and operate** a fully functional Blue Team home lab
- **Navigate Linux and Windows** environments with professional confidence
- **Configure and use** Wazuh as a production-grade SIEM/XDR platform
- **Write detection rules** using Sigma and Wazuh rule syntax
- **Analyze logs** across Linux and Windows endpoints
- **Apply the MITRE ATT&CK framework** to real detection and hunting scenarios
- **Respond to security incidents** using structured, industry-standard processes
- **Document and communicate** security findings professionally
- **Demonstrate practical skills** through a documented, public portfolio

---

## Technologies Used

| Category | Technologies |
|---|---|
| **Operating Systems** | Ubuntu Server · Windows 11 · Kali Linux |
| **SIEM / XDR** | Wazuh |
| **Virtualization** | VirtualBox · VMware Workstation |
| **Detection** | Sigma · YARA · Sysmon |
| **Frameworks** | MITRE ATT&CK · NIST CSF · CISSP Domains |
| **Planned** | Splunk · Microsoft Sentinel · Elastic Stack · Security Onion |

---

## Getting Started

**Prerequisites:** A computer with at least 16 GB RAM and 100 GB free disk space. No prior cybersecurity experience is required.

### Step 1 — Clone the repository

```bash
git clone https://github.com/kashifkhanamv123/Blue-Team-Handbook.git
cd Blue-Team-Handbook
```

### Step 2 — Choose your starting point

| Experience Level | Recommended Starting Point |
|---|---|
| Complete beginner | [Cybersecurity Foundations →](Foundation/) |
| Familiar with IT basics | [Linux Fundamentals →](Linux/) |
| Comfortable with Linux/Windows | [Security Operations →](Security-Operations/) |

### Step 3 — Build the home lab

Follow the deployment guides in [Security Operations →](Security-Operations/) to build your lab environment. The Wazuh deployment guide is the centrepiece of the practical experience.

### Step 4 — Work through the modules

Follow the learning roadmap sequentially. Each module builds on the knowledge from the previous one.

> **Tip:** Document your progress. Screenshot your lab setups, write notes, and publish your work on GitHub — this builds a portfolio that hiring managers can review.

---

## Repository Progress

| Module | Status |
|---|---|
| Repository Structure & Documentation | ✅ Complete |
| Cybersecurity Foundations | ✅ Complete |
| Linux Fundamentals | ✅ Complete |
| Windows Fundamentals | 🚧 In Progress |
| Security Operations — Ubuntu Server Guide | ✅ Complete |
| Security Operations — Windows 11 Guide | ✅ Complete |
| Security Operations — Kali Linux Guide | ✅ Complete |
| Security Operations — Wazuh Deployment Guide | ✅ Complete |
| Threat Detection (Sysmon · Sigma · YARA) | 📋 Planned |
| Threat Hunting | 📋 Planned |
| Incident Response | 📋 Planned |
| Detection Engineering | 📋 Planned |
| Blue Team / SOC Analyst | 📋 Planned |

---

## Contributing

Contributions are welcome from everyone — whether you are fixing a typo, improving an explanation, creating a new lab, or adding a diagram.

**Quick start:**

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/your-username/Blue-Team-Handbook.git

# 2. Create a descriptive feature branch
git checkout -b improve/linux-permissions-guide

# 3. Make your changes, then commit with a clear message
git commit -m "Improve Linux permissions chapter with additional examples"

# 4. Push your branch and open a Pull Request on GitHub
git push origin improve/linux-permissions-guide
```

**Before contributing**, please read:
- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution guidelines and documentation standards
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community expectations

**Ways to contribute:**
- Fix errors, improve explanations, or update outdated content
- Add screenshots, architecture diagrams, or visual aids
- Create new lab exercises or cheat sheets
- Suggest new topics via [GitHub Issues](../../issues)
- Share the project with the community

---

## License

This project is licensed under the **MIT License**.

You are free to use, share, and adapt this material for educational purposes. See the [LICENSE](LICENSE) file for full terms.

---

## Support the Project

If this handbook has helped you, here is how you can support its growth:

- ⭐ **Star the repository** — It helps others discover this resource
- 🍴 **Fork and contribute** — Improve guides, add labs, fix errors
- 📢 **Share it** — Recommend it to students, colleagues, or your community
- 💬 **Open an Issue** — Report problems or suggest improvements

Every star and every contribution keeps this project moving forward.

---

## Connect

This project is maintained by a practitioner building in public.

- **GitHub:** [Kashif-Mashi](https://github.com/Kashif-Mashi/)

---

<p align="center">
  <strong>The best time to start learning cybersecurity was yesterday. The second best time is now.</strong><br><br>
  Build your skills. &nbsp; Build your lab. &nbsp; Build your career.<br><br>
  ⭐ Star this repository if it helped you on your journey.
</p>