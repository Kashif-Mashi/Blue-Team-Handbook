![System and Network Administrator Banner](assets/sna-banner.png)

# System and Network Administrator (SNA)
**Foundational Notes | Linux | Networking | Infrastructure Administration**

This section organizes foundational System and Network Administration topics into detailed notes and quick-reference cheatsheets. It focuses on how operating systems, users, files, storage, network traffic, and remote administration work together.

## Objectives
- Understand the role of system and network administration.
- Learn foundational Linux and RHEL concepts.
- Manage files, users, groups, and permissions.
- Understand system startup, text editors, packet capture, and regex.
- Compare MBR/GPT and learn RAID/LVM fundamentals.
- Understand remote terminal access and file transfer.

## Learning notes
- [Introduction to SNA](01-Introduction-to-SNA.md)
- [SNA Certifications](02-SNA-Certifications.md)
- [RHEL](03-Linux-Fundamentals/01-Introduction-to-RHEL.md)
- [Common Linux Commands](03-Linux-Fundamentals/02-Common-Linux-Commands.md)
- [File Management](03-Linux-Fundamentals/03-File-Management.md)
- [File Permissions](03-Linux-Fundamentals/04-File-Permissions.md)
- [User Management](03-Linux-Fundamentals/05-User-Management.md)
- [System Initialization](03-Linux-Fundamentals/06-System-Initialization.md)
- [Vim and Nano](03-Linux-Fundamentals/07-Vim-and-Nano.md)
- [Tcpdump](04-Networking/01-Tcpdump-Commands.md)
- [Regular Expressions](04-Networking/02-Regular-Expressions.md)
- [MBR vs GPT](05-Disk-Management/01-MBR-vs-GPT.md)
- [RAID and LVM](05-Disk-Management/02-RAID-and-LVM.md)
- [PuTTY and WinSCP](06-Remote-File-Management/01-PuTTY-and-WinSCP.md)

## Cheatsheets
Browse the [Cheatsheets Index](cheatsheets/README.md) for concise command references.

## Environment and safety
My learning environment includes RHEL 6 and Windows-based remote administration tools. Commands vary by operating-system version. RHEL 6 is an old release; keep legacy lab systems isolated and do not expose them to untrusted networks.

**Safety:** Disk partitioning, formatting, permission changes, and service configuration can cause data loss or downtime. Inspect targets first and use a disposable VM for risky operations. Never assume a device such as `/dev/hdc` exists.

## How to use
Read the notes in sequence, practice only in authorized environments, and use cheatsheets for revision. These are learning materials, not a claim of certification or professional mastery. No labs, assignments, or screenshot placeholders are included.
