# Project Structure

This document explains the structure of the **Blue Team Handbook** repository and the purpose of each directory.

The repository is organized to provide a structured learning path for beginners who want to build practical Blue Team skills through hands-on documentation and home lab environments.

---

# Repository Overview

```text
Blue-Team-Handbook/
│
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── PROJECT_STRUCTURE.md
├── LICENSE
│
├── assets/
│
└── Security-Operations/
```

---

# Root Directory

The root directory contains the files that define and organize the project.

| File | Description |
|------|-------------|
| README.md | Main project overview |
| ROADMAP.md | Project development roadmap |
| CHANGELOG.md | Version history |
| CONTRIBUTING.md | Contribution guidelines |
| PROJECT_STRUCTURE.md | Repository organization |
| LICENSE | Project license |

---

# Assets

```text
assets/
```

The **assets** directory stores images used throughout the repository.

Examples include:

- Repository banner
- Guide banners
- Architecture diagrams
- Network diagrams
- Workflow images
- Screenshots
- Icons

Keeping images in a dedicated folder makes the documentation easier to maintain.

---

# Security-Operations

```text
Security-Operations/
```

This directory contains all documentation guides.

Each guide focuses on a different technology or concept used in Security Operations Centers (SOCs).

---

# Ubuntu Server Guide

```text
Security-Operations/
└── Ubuntu Server Guide/
```

Purpose:

Build the Linux server that hosts security platforms such as Wazuh and future enterprise tools.

Topics include:

- Installation
- Networking
- SSH
- Package Management
- Users
- Services
- Maintenance
- Troubleshooting

---

# Windows 11 Guide

```text
Security-Operations/
└── Windows 11 Guide/
```

Purpose:

Build the Windows endpoint used for security monitoring.

Topics include:

- Windows Installation
- Initial Configuration
- Networking
- Event Viewer
- Windows Security
- PowerShell
- Administrative Tools
- Preparing Windows for Wazuh

---

# Kali Linux Guide

```text
Security-Operations/
└── Kali Linux Guide/
```

Purpose:

Prepare a Linux distribution for security testing and generating events within the home lab.

Topics include:

- Installation
- Networking
- Package Management
- Essential Tools
- Home Lab Preparation

---

# Wazuh Guide

```text
Security-Operations/
└── Wazuh Guide/
```

Purpose:

Deploy and configure the Wazuh platform for centralized security monitoring.

Topics include:

- Architecture
- Installation
- Dashboard
- Manager Configuration
- Agent Deployment
- Log Collection
- Security Features
- Troubleshooting

---

# Future Guides

The repository will continue expanding with additional Blue Team technologies.

Planned guides include:

- Sysmon
- Sigma Rules
- YARA
- Threat Hunting
- Digital Forensics
- Incident Response
- Splunk
- Microsoft Sentinel
- Elastic Stack
- Security Onion
- Velociraptor

---

# Guide Structure

Every guide follows the same documentation format.

```text
Guide
│
├── README.md
├── Quick-Reference.md
├── Cheat-Sheet.md
├── Resources.md
├── assets/
└── Documentation/
```

---

# Documentation Format

Each chapter includes:

- Learning Objectives
- Introduction
- Step-by-Step Instructions
- Command Explanations
- Architecture Diagrams
- Screenshot Placeholders
- Best Practices
- Troubleshooting
- Chapter Summary
- One-Line Summary

This consistent structure makes it easier to learn across different technologies.

---

# Home Lab Architecture

The repository is built around a practical Blue Team home lab.

```text
                     Internet
                         │
                  VirtualBox Network
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Ubuntu Server      Windows 11      Kali Linux
        │                │                │
        │          Wazuh Agent            │
        │                │                │
        └────────────────┼────────────────┘
                         │
                  Wazuh Platform
                         │
                Security Monitoring
                         │
                    SOC Analyst
```

---

# Learning Path

The recommended order for completing the guides is:

1. Ubuntu Server Guide
2. Windows 11 Guide
3. Kali Linux Guide
4. Wazuh Guide
5. Sysmon Guide
6. Sigma Rules Guide
7. YARA Guide
8. Threat Hunting Guide
9. Digital Forensics Guide
10. Incident Response Guide
11. Splunk Guide
12. Microsoft Sentinel Guide

Each guide builds on the knowledge gained in the previous one.

---

# Design Principles

The Blue Team Handbook follows these principles:

- Beginner Friendly
- Practical
- Hands-On
- Well Documented
- Consistent
- Open Source
- Community Driven

---

# Repository Goals

This project aims to:

- Build practical cybersecurity knowledge
- Encourage hands-on learning
- Provide free educational resources
- Help learners build a professional home lab
- Prepare aspiring SOC Analysts for real-world environments

---

# Keeping the Repository Organized

When adding new guides:

- Follow the existing folder structure.
- Include a README.md for every guide.
- Add Quick-Reference.md, Cheat-Sheet.md, and Resources.md where appropriate.
- Store images in the guide's `assets` folder.
- Follow the documentation standards described in `CONTRIBUTING.md`.

Maintaining a consistent structure makes the repository easier to navigate, maintain, and contribute to.