# System and Network Administrator (SNA) Cheatsheets Index

> **High-Density Operational Reference Cards**  
> Quick command lookups, syntax reminders, and flag references for terminal operations.  
> Cross-referenced with the in-depth chapter study notes in the [SNA Curriculum Hub](../README.md).

---

## ⚡ Cheatsheet Directory

| Cheatsheet | Domain | High-Density Syntax Covered | Corresponding In-Depth Study Chapter |
|---|---|---|---|
| [Linux Commands Cheatsheet](Linux-Commands-Cheatsheet.md) | Navigation & Inspection | `pwd`, `ls -lah`, `cd`, `whoami`, `id`, `uname -a`, `uptime`, `df -h`, `ps aux`, `top`, `free -m` | [02-Common-Linux-Commands.md](../03-Linux-Fundamentals/02-Common-Linux-Commands.md) |
| [Linux File Management Cheatsheet](Linux-File-Management-Cheatsheet.md) | File System | FHS root tree, relative/absolute paths, `touch`, `mkdir -p`, `cp -rp`, `mv`, `rm -rf`, `tar -czvf` | [03-File-Management.md](../03-Linux-Fundamentals/03-File-Management.md) |
| [Linux Permissions Cheatsheet](Linux-Permissions-Cheatsheet.md) | Access Control | Octal conversion matrix (`755`, `644`, `600`), symbolic `chmod`, `chown`, `chgrp`, umask calculation, SUID/SGID/Sticky | [04-File-Permissions.md](../03-Linux-Fundamentals/04-File-Permissions.md) |
| [Linux User Management Cheatsheet](Linux-User-Management-Cheatsheet.md) | Identity & Sudo | `/etc/passwd` (7 fields), `/etc/shadow` (9 fields), `useradd`, `usermod -aG`, `passwd`, `chage`, `visudo` | [05-User-Management.md](../03-Linux-Fundamentals/05-User-Management.md) |
| [Vim and Nano Cheatsheet](Vim-and-Nano-Cheatsheet.md) | Text Editors | Nano `^O`/`^X`, Vim modal engine (Normal, Insert, Visual, Ex), navigation `h/j/k/l`, `dd`, `yy`, `p`, `:%s`, swap recovery | [07-Vim-and-Nano.md](../03-Linux-Fundamentals/07-Vim-and-Nano.md) |
| [Tcpdump Cheatsheet](Tcpdump-Cheatsheet.md) | Packet Analysis | Sniffing flags (`-nn`, `-X`, `-A`, `-w`, `-r`, `-s 0`), BPF filters (`host`, `net`, `port`), TCP control flag decoding | [01-Tcpdump-Commands.md](../04-Networking/01-Tcpdump-Commands.md) |
| [Regular Expressions Cheatsheet](Regular-Expressions-Cheatsheet.md) | Text Parsing | Anchors (`^`, `$`), character sets (`[0-9]`, `[^0-9]`), quantifiers (`*`, `+`, `?`, `{m,n}`), alternation (`\|`), log parsing | [02-Regular-Expressions.md](../04-Networking/02-Regular-Expressions.md) |
| [Disk Management Cheatsheet](Disk-Management-Cheatsheet.md) | Storage & LVM | `lsblk -f`, `fdisk -l`, MBR vs GPT rules, LVM 3-tier syntax (`pvcreate`, `vgcreate`, `lvcreate`, `lvextend -r`) | [01-MBR-vs-GPT.md](../05-Disk-Management/01-MBR-vs-GPT.md) & [02-RAID-and-LVM.md](../05-Disk-Management/02-RAID-and-LVM.md) |
| [PuTTY and WinSCP Cheatsheet](PuTTY-and-WinSCP-Cheatsheet.md) | Remote Admin | SSH host setup, keepalive configuration, PuTTYgen `.ppk` keys, `authorized_keys`, WinSCP SFTP transfers, CRLF fixes | [01-PuTTY-and-WinSCP.md](../06-Remote-File-Management/01-PuTTY-and-WinSCP.md) |

---

## ⚡ When to Use Cheatsheets vs. Detailed Notes

- **Use Cheatsheets When:**
  - You are actively working in an SSH terminal session and need an immediate syntax reminder (e.g., the exact flags for `tar -czvf` or `usermod -aG`).
  - You need to confirm whether an operation is destructive before pressing Enter.
  - You are performing live maintenance or troubleshooting an active service incident under time pressure.
- **Use Detailed Study Notes When:**
  - You are preparing for university BSIT examinations, technical interviews, or certifications (RHCSA, CCNA, Security+).
  - You need to understand the underlying mechanics of *why* the operating system or network protocol behaves as it does.
  - You need to study architectural trade-offs, security implications, and practice scenarios.

---

## ⚙️ Legacy RHEL 6 vs. Modern RHEL Quick Command Map

| Administrative Task | Legacy RHEL 6 (SysVinit / net-tools) | Modern RHEL 7, 8, and 9 (systemd / iproute2) |
|---|---|---|
| **Start a Service** | `service httpd start` | `systemctl start httpd` |
| **Stop a Service** | `service httpd stop` | `systemctl stop httpd` |
| **Restart a Service** | `service httpd restart` | `systemctl restart httpd` |
| **Service Status** | `service httpd status` | `systemctl status httpd` |
| **Enable on Boot** | `chkconfig httpd on` | `systemctl enable httpd` |
| **Disable on Boot** | `chkconfig httpd off` | `systemctl disable httpd` |
| **Inspect Interfaces** | `ifconfig -a` | `ip addr show` |
| **Inspect Routes** | `route -n` | `ip route show` |
| **Default Boot Target** | `/etc/inittab` (`id:3:initdefault:`) | `systemctl set-default multi-user.target` |
| **Package Management** | `yum install <package>` | `dnf install <package>` |

---

## 🛡️ Pre-Execution Safety Directives

Before pressing `Enter` on any administrative command, verify:
1. **Target Accuracy:** Is the target path or disk device correct? (e.g., verifying with `pwd` or `lsblk`).
2. **Destructive Impact:** Does this command erase, overwrite, or reformat data? (e.g., `>` vs `>>`, `rm -rf`, `fdisk`).
3. **Backup Status:** Is there a recent, verified backup of the file or partition before you modify it?
4. **Authorization:** Are you authorized to execute this command on this specific network or system?
