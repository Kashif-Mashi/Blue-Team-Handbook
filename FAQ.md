# Frequently Asked Questions (FAQ)

Welcome to the **Blue Team Handbook FAQ**.

This document answers the most common questions about the repository, home lab setup, and learning path.

---

# General Questions

## What is the Blue Team Handbook?

The Blue Team Handbook is an open-source learning project that provides practical, step-by-step guides for building a Blue Team home lab and learning Security Operations concepts.

The project focuses on:

- Home Lab Setup
- Linux Administration
- Windows Administration
- Security Monitoring
- SIEM Deployment
- Detection Engineering
- Threat Hunting
- Incident Response

---

## Who is this repository for?

This repository is designed for:

- Beginners in Cybersecurity
- BSIT / BSCS Students
- SOC Analyst Aspirants
- Blue Team Learners
- IT Professionals
- Home Lab Builders

No previous Blue Team experience is required.

---

## Is this project free?

Yes.

The Blue Team Handbook is completely free and open source.

---

## Can I contribute?

Absolutely.

Please read:

- CONTRIBUTING.md

before submitting a Pull Request.

---

# Home Lab Questions

## Which virtualization software should I use?

The guides use **Oracle VirtualBox** because it is:

- Free
- Cross-platform
- Beginner-friendly
- Well documented

You may also use VMware Workstation, Hyper-V, or Proxmox if you are comfortable with them.

---

## Why do we use Ubuntu Server?

Ubuntu Server acts as the operating system for server-based applications.

For example:

```text
Ubuntu Server
        │
        ▼
Wazuh Manager
```

The operating system manages hardware, networking, storage, and services, while Wazuh runs as an application on top of Ubuntu.

---

## Why do I need Windows 11?

Windows is used as the monitored endpoint.

It generates:

- Windows Event Logs
- Security Events
- PowerShell Logs
- Defender Alerts

These events are collected by Wazuh for monitoring and analysis.

---

## Why do I need Kali Linux?

Kali Linux is used to generate activity within the home lab.

Examples include:

- Network scanning
- Authentication testing
- Web application testing
- Security tool practice

These activities help you understand how security events appear in monitoring platforms.

---

# Wazuh Questions

## Is Wazuh an operating system?

No.

Wazuh is a security platform that runs on a Linux operating system such as Ubuntu Server.

Example:

```text
Ubuntu Server
        │
        ▼
Wazuh Platform
```

---

## Why does Wazuh need Ubuntu Server?

Ubuntu provides:

- Networking
- Storage
- Process management
- User management
- System services

Wazuh depends on the operating system to provide these capabilities.

---

## Can Wazuh monitor Windows?

Yes.

Windows endpoints are monitored using the **Wazuh Agent**, which sends security events to the Wazuh Manager.

---

# Learning Path

## Which guide should I start with?

Follow this order:

1. Ubuntu Server Guide
2. Windows 11 Guide
3. Kali Linux Guide
4. Wazuh Guide
5. Sysmon Guide
6. Sigma Rules Guide
7. Threat Hunting Guide
8. Incident Response Guide
9. Splunk Guide
10. Microsoft Sentinel Guide

Each guide builds on the previous one.

---

## Can I skip Ubuntu?

No.

Ubuntu Server is required because it hosts the Wazuh platform used in later guides.

---

## Can I skip Windows?

Not recommended.

Many security events covered in this repository come from Windows systems.

---

## Can I skip Kali?

You can, but you will miss many practical exercises that involve generating security events and testing your lab.

---

# Hardware Requirements

## What are the minimum requirements?

Recommended:

| Component | Recommendation |
|-----------|----------------|
| CPU | Quad-Core or better |
| RAM | 16 GB minimum |
| Storage | 250 GB SSD or larger |
| Virtualization | Intel VT-x / AMD-V Enabled |

More RAM will provide a better experience when running multiple virtual machines simultaneously.

---

# Software Requirements

The following software is used throughout the repository:

- Oracle VirtualBox
- Ubuntu Server
- Windows 11
- Kali Linux
- Wazuh

Additional software will be introduced in future guides.

---

# Documentation

## Why are there screenshot placeholders?

The guides are designed so screenshots can be updated as software interfaces change.

This keeps the documentation easier to maintain over time.

---

## Why do all guides follow the same format?

Consistency improves the learning experience.

Each guide includes:

- Learning Objectives
- Step-by-Step Instructions
- Command Explanations
- Best Practices
- Troubleshooting
- Chapter Summary

---

# Future Plans

## What topics will be added next?

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

See **ROADMAP.md** for the latest development plans.

---

# Support

## I found an error.

Please open a GitHub Issue and include:

- Guide name
- Chapter number
- Description of the problem
- Suggested correction (if possible)

---

## I have a suggestion.

Feature requests and documentation improvements are always welcome.

Please open a GitHub Issue to discuss your idea.

---

# License

This project is released under the MIT License.

See the LICENSE file for details.

---

Thank you for using the **Blue Team Handbook**.

We hope this project helps you build practical cybersecurity skills and grow your confidence in Blue Team operations.