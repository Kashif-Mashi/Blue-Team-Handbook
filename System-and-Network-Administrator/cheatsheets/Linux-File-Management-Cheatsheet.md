# Linux File Management Cheatsheet

> **Operational Quick Reference for System Administrators & BSIT Students**  
> Companion detailed notes: [03-File-Management.md](../03-Linux-Fundamentals/03-File-Management.md)

---

## 🗂️ Filesystem Hierarchy Standard (FHS) Quick Directory Map

| Directory | Primary Content & Operational Purpose | Administrator Significance |
|---|---|---|
| **`/`** | The root directory; foundation of the entire unified tree | Never fill to 100%; system crashes |
| **`/boot`** | Kernel binary (`vmlinuz`), `initramfs`, and GRUB2 bootloader | Isolated boot partition; essential for startup |
| **`/dev`** | Special hardware device nodes (`/dev/sda`, `/dev/null`, `/dev/urandom`) | Virtual RAM nodes managed dynamically by `udev` |
| **`/etc`** | Host-specific plain text configuration files (no binaries) | Most critical directory for disaster backups |
| **`/home`** | Personal workspaces for regular human user accounts | Often mounted on dedicated partition or network share |
| **`/root`** | Personal home directory of the `root` superuser | Isolated on `/` so root can log in during single-user mode |
| **`/var`** | Variable data: system logs (`/var/log`), spool queues, databases | Always monitor disk capacity (`df -h`) |
| **`/usr`** | Read-only user software, libraries, and binaries (`/usr/bin`, `/usr/lib`) | `/bin` and `/sbin` symlink here on modern RHEL |
| **`/opt`** | Optional third-party enterprise application suites | Keeps vendor packages isolated in single folders |
| **`/proc`** | Virtual in-memory filesystem exposing running process & kernel state | 0 bytes on disk; dynamic kernel diagnostics |
| **`/sys`** | Virtual in-memory filesystem exposing hardware device models | Used by modern systemd and udev subsystems |
| **`/tmp`** | Temporary scratch space cleared on reboot | World-writable; protected by the Sticky Bit |
| **`/mnt`** | Temporary mount point for administrators mounting manual storage | Clean staging location for disk recovery |

---

## 🧭 Path Resolution Quick Syntax

```text
/etc/httpd/conf/httpd.conf   ──> ABSOLUTE Path (Always starts with leading '/')
conf/httpd.conf              ──> RELATIVE Path (Evaluated from current working directory)
.                            ──> Current Directory pointer
..                           ──> Parent Directory pointer (one level up)
~                            ──> Current user's home directory (/home/username or /root)
```

---

## 🔗 Inodes, Hard Links, and Soft (Symbolic) Links

| Operation | Command Syntax | Inode Behavior | Crossing Partitions? | Linking Directories? | If Target Deleted |
|---|---|---|:---:|:---:|---|
| **View Inode** | `ls -li <file>` | Displays numerical inode address | N/A | N/A | N/A |
| **Create Hard Link** | `ln <target> <link>` | Shares **exact same inode**; increments link count | ❌ NO | ❌ NO | Data preserved (links >= 1) |
| **Create Soft Link** | `ln -s <target> <link>`| Creates **new inode**; points to target pathname | ✅ YES | ✅ YES | ⚠️ Becomes Dangling (Broken) |

```bash
# View file inode and link count
ls -li /opt/report.txt

# Create a hard link
ln /opt/data.txt /backup/data_hardlink.txt

# Create a symbolic (soft) shortcut to a deeply nested directory
ln -s /var/log/httpd /home/student/weblogs
```

---

## 📦 Tape Archiving (`tar`) & Compression Syntax

$$\text{Syntax:}\quad \mathbf{tar}\quad [\mathbf{operations} + \mathbf{compression}\ +\mathbf{f}]\quad \mathbf{archive\_name.tar.gz}\quad \mathbf{targets...}$$

| Task | Command Line Syntax | Operational Breakdown |
|---|---|---|
| **Create Gzip Archive** | `tar -czvf backup.tar.gz /etc` | `-c` (create), `-z` (gzip), `-v` (verbose), `-f` (filename) |
| **Create Bzip2 Archive** | `tar -cjvf backup.tar.bz2 /etc` | `-j` (bzip2 - higher compression ratio, slower speed) |
| **Create XZ Archive** | `tar -cJvf backup.tar.xz /etc` | `-J` (xz - maximum enterprise compression ratio) |
| **Inspect Archive (No Extract)** | `tar -tzvf backup.tar.gz` | `-t` (table of contents): previews files safely |
| **Extract to Current Dir** | `tar -xzvf backup.tar.gz` | `-x` (extract): unpacks into current directory |
| **Extract to Specific Folder** | `tar -xzvf backup.tar.gz -C /tmp/restore/` | `-C` (change directory): unpacks into specified destination |

---

## 🛡️ Pre-Execution Safety Directives

1. **Verify Location First:** Always execute `pwd` before running recursive deletion commands.
2. **Never Run:** `rm -rf /` or `rm -rf /*`
3. **Double-check Trailing Slashes on Symlinks:** To delete a symlink to a folder, execute `rm my_symlink` (omitting the trailing slash `/`). Adding a slash (`rm my_symlink/`) targets the contents of the target directory!
