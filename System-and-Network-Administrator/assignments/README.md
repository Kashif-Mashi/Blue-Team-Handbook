# System and Network Administration (SNA) — Coursework & Assignments Hub

Welcome to the **Assignments & Practical Coursework** section for System and Network Administration (SNA). 

This directory contains structured assignments designed to translate conceptual systems administration knowledge into hands-on command-line proficiency. Each assignment includes a pedagogical overview, architectural breakdowns, visual Mermaid diagrams, realistic command demonstrations, hands-on lab exercises, and self-assessment review questions with complete answer keys.

---

## 📚 Curriculum Assignment Index

| Assignment ID | Topic | Target Competency | Document Reference |
|---|---|---|---|
| **Assignment 01** | **Linux Filesystem Hierarchy Standard (FHS)** | Understanding the unified inverted directory tree (`/`), contrasting Linux with Windows drive letters, distinguishing `/` vs. `root` vs. `/root`, exploring all 18 FHS directories, inspecting dynamic virtual filesystems (`/proc`, `/sys`), and hands-on system exploration. | [Assignment 01: Linux FHS](Assignment-01-Linux-File-System-Hierarchy.md) |
| **Assignment 02** | **Remote Linux Server Management Using PuTTY & WinSCP** | Remote SSH administration via PuTTY, GUI SFTP file operations via WinSCP, Linux discretionary access permissions (`chmod`), root escalation (`su -`), configuration editing with safety rollback (`diff`/`nano`), 500 MB transfer with SHA-256 verification, firewall rule persistence (`iptables`), and RSA-2048 public-key authentication. | [Assignment 02: PuTTY & WinSCP Management](Remote%20linux%20server%20manage%20using%20putty/README.md) |
| **Assignment 03** | **Disk Partitioning, Swap, and Software RAID 1 Mirroring** | MBR disk repartitioning (`fdisk`), troubleshooting device/resource busy locks (`swapoff`, `vgremove`), creating equal partitions with Hex types `fd` (RAID) and `82` (Swap), activating virtual memory (`mkswap`/`swapon`), creating mirrored array (`mdadm`), formatting with `ext4`, and verification via `lsblk` and `/proc/mdstat`. | [Assignment 03: Partitioning, Swap & RAID 1](Raid%20assigment/README.md) |

---

## 🎯 Recommended Prerequisite Reading

Before starting this assignment, students are strongly encouraged to review the corresponding theoretical and operational reference modules:

- **Primary Study Note:** [03-Linux-Fundamentals / 03-File-Management.md](../03-Linux-Fundamentals/03-File-Management.md)
- **Permissions & Security Note:** [03-Linux-Fundamentals / 04-File-Permissions.md](../03-Linux-Fundamentals/04-File-Permissions.md)
- **Field Reference Cheatsheet:** [cheatsheets / Linux-File-Management-Cheatsheet.md](../cheatsheets/Linux-File-Management-Cheatsheet.md)
- **Common CLI Commands:** [03-Linux-Fundamentals / 02-Common-Linux-Commands.md](../03-Linux-Fundamentals/02-Common-Linux-Commands.md)

---

## 📝 Student Assignment Guidelines

1. **Active Terminal Practice:** Do not simply read through the material. Open a terminal session on your Linux virtual machine (e.g., Red Hat Enterprise Linux, Rocky Linux, Ubuntu Server) and execute every demonstration command.
2. **Observe & Compare:** Note differences between expected textbook output and what your specific distribution reports (e.g., symlinked `/bin` paths due to UsrMerge).
3. **Complete the Lab Exercises:** Work through the practical exercises at the end of each assignment and document your findings.
4. **Self-Assessment:** Attempt the review questions independently before expanding the hidden answer keys.
