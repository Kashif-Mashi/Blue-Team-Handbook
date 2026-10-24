# System and Network Administrator (SNA) Cheatsheets

> **Operational Quick Reference Cards**  
> High-density command syntax, patterns, and parameters for terminal maintenance.  
> Each cheatsheet links directly to its parent foundational guide for in-depth theory.

---

## 📑 Cheatsheet Index

| Cheatsheet | Domain | Focus & Key Syntax | Detailed Guide |
|---|---|---|:---:|
| [Linux Commands Cheatsheet](Linux-Commands-Cheatsheet.md) | CLI Basics | Navigation, inspection (`ls`, `cat`, `less`), pipes (`\|`), streams (`>`, `>>`, `2>`), output counts (`wc`, `head`, `tail`) | [02-Common-Linux-Commands.md](../03-Linux-Fundamentals/02-Common-Linux-Commands.md) |
| [Linux File Management Cheatsheet](Linux-File-Management-Cheatsheet.md) | Filesystem | Creation (`touch`, `mkdir`), copying (`cp -p`), moving (`mv`), links (`ln`, `ln -s`), safe removal (`rm -i`) | [03-File-Management.md](../03-Linux-Fundamentals/03-File-Management.md) |
| [Linux Permissions Cheatsheet](Linux-Permissions-Cheatsheet.md) | Security | Octal permissions (`755`, `644`, `600`), symbolic `chmod`, `chown`, SUID/SGID/Sticky bits, umask calculation | [04-File-Permissions.md](../03-Linux-Fundamentals/04-File-Permissions.md) |
| [Linux User Management Cheatsheet](Linux-User-Management-Cheatsheet.md) | Identity | Account creation (`useradd`), modification (`usermod -aG`), password policies (`chage`, `passwd -l`), `su -` vs `sudo` | [05-User-Management.md](../03-Linux-Fundamentals/05-User-Management.md) |
| [Vim and Nano Cheatsheet](Vim-and-Nano-Cheatsheet.md) | Editors | Nano keybindings, Vim modal transitions (Normal, Insert, Visual, Command-line), search/replace, swap recovery | [07-Vim-and-Nano.md](../03-Linux-Fundamentals/07-Vim-and-Nano.md) |
| [Tcpdump Cheatsheet](Tcpdump-Cheatsheet.md) | Networking | Sniffing flags (`-nn`, `-X`, `-A`, `-w`, `-r`), BPF filters (hosts, ports, CIDRs, TCP control flags) | [01-Tcpdump-Commands.md](../04-Networking/01-Tcpdump-Commands.md) |
| [Regular Expressions Cheatsheet](Regular-Expressions-Cheatsheet.md) | Text Parsing | Anchors (`^`, `$`), digit patterns (`[0-9]`, `[0-9][0-9]`), syllabus codes (`BSCS$`), BRE vs ERE operators | [02-Regular-Expressions.md](../04-Networking/02-Regular-Expressions.md) |
| [Disk Management Cheatsheet](Disk-Management-Cheatsheet.md) | Storage | Block inspection (`lsblk`, `fdisk -l`), MBR vs GPT rules, LVM hierarchy (`pvcreate`, `vgcreate`, `lvcreate`, `lvextend`) | [01-MBR-vs-GPT.md](../05-Disk-Management/01-MBR-vs-GPT.md) & [02-RAID-and-LVM.md](../05-Disk-Management/02-RAID-and-LVM.md) |
| [PuTTY and WinSCP Cheatsheet](PuTTY-and-WinSCP-Cheatsheet.md) | Remote Admin | SSH host setup, PuTTYgen `.ppk` generation, server `authorized_keys` deployment, WinSCP SFTP transfers | [01-PuTTY-and-WinSCP.md](../06-Remote-File-Management/01-PuTTY-and-WinSCP.md) |

---

## ⚡ When to Use Cheatsheets vs. Detailed Notes

- **Use Cheatsheets When**:
  - You are actively working in a terminal or troubleshooting an active outage.
  - You need the exact syntax of a flag (e.g., `grep -E`, `usermod -aG`, `tcpdump -nn`).
  - You need to confirm whether an operation is destructive before pressing Enter.
- **Use Detailed Notes When**:
  - You are studying for academic exams, certifications (RHCSA, CCNA), or job interviews.
  - You need to understand *how* the Linux kernel, BPF virtual machine, or filesystem inodes function internally.
  - You are architecting enterprise infrastructure or designing backup/recovery policies.

---

## ⚠️ Pre-Execution Safety Directives

1. **Verify Operating System Version**:
   - Check whether your target environment is **RHEL 6 (SysVinit)** or **RHEL 7/8/9 (systemd)**:
     ```bash
     cat /etc/redhat-release
     ```
   - Legacy RHEL 6 uses `service <name> status` and `chkconfig <name> on`.
   - Modern systems use `systemctl status <name>` and `systemctl enable <name>`.
2. **Double-Check Block Devices**:
   - Never run formatting (`mkfs`) or partition table modification (`fdisk`, `parted`) commands without confirming the disk letter using `lsblk`.
3. **Respect Destructive Warnings**:
   - Commands marked with `⚠️ DESTRUCTIVE` permanently overwrite, wipe, or drop data. Always create configuration backups (`cp -p file file.bak`) prior to modification.
