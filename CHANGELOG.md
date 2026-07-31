# Changelog

All notable changes to the **Blue-Team-Handbook** project are documented in this file.

# 31 July 2026
### Improved

- Standardized chapter structure to match the Linux Fundamentals module.
- Added learning objectives, summaries, key takeaways, and professional GitHub formatting.
- Added notes directing readers to the dedicated **Security Operations** repository for the complete Windows installation and configuration guide, avoiding duplicate documentation.

---

## 🗂 Windows File System

### Added

- Started **Chapter 03 — Windows File System & File Explorer**.
- Added an overview of the Windows File System and its responsibilities.
- Explained the relationship between **Disks, Partitions, Volumes, and Drive Letters**.
- Documented the architecture and features of the **NTFS File System**.
- Added Mermaid diagrams to visualize storage hierarchy and NTFS architecture.
- Included Blue Team notes highlighting the forensic importance of NTFS metadata and file system artifacts.

---

## 🧪 Labs

### Added

- Created **Lab 02 — File System Investigation**.
- Added practical exercises for exploring Windows directories, file metadata, hidden files, file extensions, NTFS attributes, and Alternate Data Streams (ADS).
- Included a Blue Team investigation scenario for analyzing a suspicious file.

### Solutions

- Created the complete solution guide for **Lab 02**.
- Added step-by-step explanations, expected outputs, command references, investigation notes, and security recommendations.

---

## 📖 Documentation

### Improved

- Enhanced documentation consistency across chapters and labs.
- Improved Markdown formatting for GitHub readability.
- Added professional notes, tables, and Mermaid diagrams where appropriate.
- Maintained a beginner-friendly learning path while incorporating Blue Team and Digital Forensics perspectives.

## 30 July 2026

### 🚀 Windows Fundamentals Kickoff & Linux Screenshot Repair

Today focused on launching the **Windows Fundamentals** module and completing a full audit and fix of all screenshot references across the **Linux Fundamentals** solutions.

### ✨ Completed

* ✅ **Windows Fundamentals Module Initialization**:
  * Created `Windows/README.md` with complete module overview, learning objectives, hands-on lab listings, and fixed banner image linking to `../assets/Windows-Fundamental.png`.
  * Created `Windows/Cheat Sheet/Commands.md` covering Event IDs, startup locations, Registry hives, and PowerShell essentials for Blue Team analysts.
  * Created `Windows/Commands/Commands.md` quick reference guide for Command Prompt, PowerShell, Services, Registry, and System maintenance.
  * Created `Windows/Resources/Resources.md` listing Microsoft Learn, Sysinternals Suite, recommended books, YouTube channels, and certification paths.

* ✅ **Windows Architecture & Installation Chapters**:
  * Completed **Chapter 01 — Introduction to Windows Operating System** covering Windows architecture, boot process (BIOS/UEFI, POST, Boot Manager, `ntoskrnl.exe`), user vs kernel mode, and 32-bit vs 64-bit architecture.
  * Converted the Windows architecture ASCII diagram into a modern interactive **Mermaid flowchart** with Kernel Mode subgraphs.
  * Completed **Chapter 02 — Windows Installation & Initial Configuration** detailing the installation steps, Out-of-Box Experience (OOBE), Local vs Microsoft accounts, privilege separation, and Windows Update categories.
  * Created **Lab 01 — Windows Installation** guide and solution reference.

* ✅ **Linux Solutions Screenshot Repair & Cleanup**:
  * Audited all 13 solution files in `Linux/Labs/Solutions/`.
  * Fixed 57+ broken screenshot references across Labs 03–13 by unwrapping them from fenced code blocks (` ```md ``` `) to ensure proper rendering on GitHub.
  * Verified all relative image paths (`../../Screenshot/solution/Lab-XX/task-XX.png`).
  * Added `TODO` comments for missing screenshots in Lab 06, Lab 07, Lab 10, Lab 13, and Lab 14.
  * Cleaned up obsolete screenshot placeholders across Linux Fundamentals chapters.
  * Fixed banner image path in `Linux/README.md` to `../assets/Linux-Fundamentals.png`.

---

## 29 July 2026

### 🛠️ Windows Fundamentals Module Structure & Planning

Yesterday focused on designing the structure for the upcoming **Windows Fundamentals** module and preparing repository resources.

### ✨ Completed

* ✅ Outlined the 14-chapter roadmap for Windows Fundamentals (Editions, File System, CMD/PowerShell, NTFS Permissions, Users & Groups, Processes & Services, Event Logs, Windows Security, Registry, Software Management, Scripting, Hardening, and Blue Team Challenge).
* ✅ Standardized directory layout for Windows module (`Chapters/`, `Labs/`, `Solutions/`, `Cheat-Sheets/`, `Commands/`, `Resources/`, `Screenshots/`).
* ✅ Prepared Windows module assets and updated module banners.

---

##  28 July 2026

### 🚀 Blue Team Handbook – Linux Fundamentals Completed

Today focused on finalizing the **Linux Fundamentals** section of the **Blue Team Handbook**, bringing the module to production-ready quality.

### ✨ Completed

* ✅ Created comprehensive **Solution Guides** for:

  * Lab 08 – Processes & Services
  * Lab 09 – Linux Networking
  * Lab 10 – Logging & Monitoring
  * Lab 11 – Package Management
  * Lab 12 – Bash Scripting
  * Lab 13 – Linux Security & Hardening
  * Lab 14 – Blue Team Linux Investigation Challenge

* ✅ Standardized the solution format across all labs:

  * Overview
  * Task-by-task walkthrough
  * Commands
  * Expected results
  * Screenshot placeholders
  * Challenge answers
  * Lab completion summary

* ✅ Designed a consistent screenshot structure for every lab (`Screenshot/solution/Lab-XX/`) to improve documentation and GitHub readability.

* ✅ Enhanced the final Blue Team Investigation Challenge with:

  * Complete investigation workflow
  * Evidence collection procedures
  * Security hardening steps
  * Professional incident report template
  * SOC-style investigation methodology

* ✅ Improved cross-lab continuity by reusing assets created throughout the course, including:

  * `Incident-2026` investigation workspace
  * `analyst1`, `analyst2`, and `soc-team`
  * Security report automation
  * System hardening workflow

* ✅ Identified Linux distribution differences during testing and updated documentation to support both:

  * **Ubuntu/Debian (rsyslog – `/var/log/auth.log`)**
  * **Modern Kali Linux (systemd-journald – `journalctl`)**

* ✅ Created a GitHub Copilot automation prompt to:

  * Scan all solution files
  * Automatically insert existing screenshots
  * Validate Markdown image paths
  * Report missing screenshots
  * Preserve handbook formatting

### 🛠️ Documentation Improvements

* Standardized Markdown formatting across solution guides.
* Improved GitHub-friendly structure and readability.
* Added Blue Team investigation tips to reinforce practical SOC workflows.
* Ensured every lab follows a consistent educational and documentation style.

### 🎯 Current Status

* ✅ Linux Fundamentals (14 Chapters)
* ✅ Linux Labs (14 Practical Labs)
* ✅ Linux Solution Guides (14 Complete Walkthroughs)
* ✅ Screenshot Structure Standardized
* ✅ Final Investigation Challenge Completed

### 🔜 Next Steps

* Review and validate all screenshots in the repository.
* Complete final QA of the Linux module.
* Publish the Linux Fundamentals section.
* Begin development of the **Windows Fundamentals** module for the Blue Team Handbook.

# July 25, 2026

## Overview

Today's development focused on completing the **Linux Fundamentals** documentation for the **Blue Team Handbook**. The primary objective was to build a comprehensive, beginner-friendly, and GitHub-ready learning resource that serves as the foundation for future Blue Team and SOC-related topics.

---

## ✅ Linux Fundamentals Completed

Successfully completed all **14 chapters** of the Linux Fundamentals handbook.

### Chapters Completed

* Chapter 01 – Introduction to Linux
* Chapter 02 – Installing Linux
* Chapter 03 – Linux File System
* Chapter 04 – Shell & Terminal Basics
* Chapter 05 – Navigation Commands
* Chapter 06 – File & Directory Management
* Chapter 07 – Users & Groups
* Chapter 08 – Permissions & Ownership
* Chapter 09 – Processes & Services
* Chapter 10 – Linux Networking Basics
* Chapter 11 – Logging & Monitoring
* Chapter 12 – Package Management
* Chapter 13 – Bash Scripting Basics
* Chapter 14 – Linux Security Fundamentals

---

## 📖 Documentation Standardization

Every chapter follows a consistent structure to improve readability and maintainability.

Each chapter includes:

* Learning Objectives
* Introduction
* Core Concepts
* Detailed Explanations
* ASCII Diagrams
* Command Syntax
* Practical Examples
* Screenshot Placeholders
* Blue Team Perspective
* Common Mistakes
* Best Practices
* Chapter Summary
* Interview Questions
* References

---

## 📁 Repository Organization

Designed the Linux section with a scalable structure for future content.

```text
Linux/
├── README.md
├── Fundamentals/
├── Labs/
├── Cheat-Sheets/
├── Commands/
├── Screenshots/
├── Resources/
└── Assets/
```

---

## 📄 Documentation Improvements

Created supporting documentation for the Linux section:

* Linux README
* Linux Cheat Sheet
* Linux Learning Resources
* Commands Index

---

## 📝 Documentation Strategy

Decided to use **Markdown (.md)** as the primary documentation format instead of individual PDF files.

Reasons:

* Better GitHub compatibility
* Easier maintenance
* Version control with Git
* Better collaboration
* Easy future updates
* Ability to generate professional PDF releases when required

---

## 🎯 Current Progress

* ✅ Linux Fundamentals documentation completed (14 Chapters)
* ✅ Repository structure finalized
* ✅ Documentation standardized
* ✅ Cheat Sheet created
* ✅ Learning Resources compiled
* ✅ Commands Index created
* ✅ Markdown-based documentation workflow established

---

## 🚀 Next Phase

The next phase of the project will focus on transforming the documentation into a complete learning experience by adding practical visual content.

Planned tasks include:

* Capture screenshots for every Linux command and example.
* Organize screenshots into chapter-wise folders.
* Replace screenshot placeholders with actual images.
* Create practical Linux labs.
* Develop additional command reference guides.
* Review and proofread all chapters.
* Generate the first official **Linux Fundamentals v1.0** release.

---

## Status

**Linux Fundamentals documentation is now complete.** The next milestone is to enhance the handbook with screenshots, practical labs, and visual assets before publishing the first release on GitHub.

---

# Changelog

All notable changes to the **Blue-Team-Handbook** project are documented in this file.

---

## 13 July 2026 — Project Kickoff

### Added
- Started learning Security Information and Event Management (SIEM).
- Began studying Wazuh fundamentals.
- Completed Chapters 1–4 of the Wazuh learning path.
- Planned the structure for a beginner-friendly Blue Team documentation project.

---

## 14 July 2026 — Ubuntu Server Preparation

### Added
- Installed Ubuntu Server.
- Configured the server environment.
- Learned Ubuntu Server networking fundamentals.
- Continued Wazuh deployment documentation.

---

## 15 July 2026 — Deployment Challenges

### Fixed
- Investigated Wazuh installation failures caused by insufficient system resources.
- Identified storage and resource limitations.

### Learned
- Always verify hardware and software requirements before deployment.
- Importance of troubleshooting before reinstalling.

---

## 16 July 2026 — Ubuntu Configuration

### Added
- Completed Ubuntu Server configuration.
- Verified networking and system readiness.
- Updated installation documentation.

---

## 17 July 2026 — Kali Linux Setup

### Added
- Installed Kali Linux.
- Configured networking.
- Prepared Kali Linux for future Wazuh agent deployment.

---

## 18 July 2026 — Windows Endpoint

### Added
- Installed Windows 11.
- Completed Windows configuration.
- Prepared Windows as a Wazuh endpoint.

---

## 20 July 2026 — Wazuh Deployment

### Added
- Installed Wazuh Manager.
- Installed Wazuh Dashboard.
- Installed Wazuh Indexer.
- Began Wazuh configuration and deployment documentation.

---

## 21 July 2026 — Documentation Progress

### Added
- Completed the first five chapters of the Wazuh Installation Guide.
- Improved documentation formatting.
- Organized repository structure.

---

## 22 July 2026 — Successful Deployment

### Added
- Successfully deployed the Wazuh environment.
- Connected Windows 11 agent.
- Connected Kali Linux agent.
- Verified communication between endpoints and the Wazuh Manager.

### Fixed
- Storage space issues.
- LVM partition expansion.
- Package installation failures.
- VirtualBox networking issues.
- NAT and Host-Only adapter configuration.
- DNS resolution problems.
- Agent enrollment issues.
- Incorrect Wazuh Manager IP configuration.

### Documentation
- Added troubleshooting notes based on real deployment scenarios.
- Updated installation guides with common fixes.

---

## 23–25 July 2026 — Repository Enhancement

### Added
- Professional repository structure.
- Project roadmap.
- README files for all major guides.
- Cheat Sheets.
- Quick Reference guides.
- Resource documentation.
- Project badges.
- GitHub improvements.

### Improved
- Repository organization.
- Documentation consistency.
- Navigation between guides.
- Markdown formatting.
- Overall project presentation.

---

# Current Progress

## Completed

- ✅ Foundation structure
- ✅ Ubuntu Server Guide
- ✅ Windows Guide
- ✅ Kali Linux Guide
- ✅ Wazuh Installation & Deployment (7 Chapters)
- ✅ Wazuh Home Lab
- ✅ Windows Agent Deployment
- ✅ Kali Linux Agent Deployment
- ✅ Troubleshooting Documentation
- ✅ Repository Documentation

---

# Next Milestone

The next phase of the project will focus on practical learning and Blue Team operations.

### Planned

- Linux Fundamentals
- Linux Practical Labs
- Bash Scripting
- Log Analysis
- File Integrity Monitoring (FIM)
- Security Configuration Assessment (SCA)
- Vulnerability Detection
- Active Response
- Rules & Decoders
- Threat Hunting
- Detection Engineering
- SOC Analyst Practical Labs
- Incident Response Scenarios
- Additional diagrams and screenshots

---

**Project Status:** 🟢 Active Development

**Last Updated:** July 2026