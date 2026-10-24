# Linux File Management Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [03-File-Management.md](../03-Linux-Fundamentals/03-File-Management.md) | [Cheatsheets Index](README.md)

---

## 📁 File and Directory Manipulation

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `touch <file>` | Create empty file / update timestamp | `touch config.yaml` | [Modifies Metadata] Creates empty file if absent; refreshes timestamp if present. |
| `mkdir <dir>` | Create new directory | `mkdir /opt/scripts` | [Modifies Filesystem] Creates a single directory in current or specified path. |
| `mkdir -p <path>` | Create parent directories recursively | `mkdir -p /opt/app/data/logs` | [Modifies Filesystem] Creates any missing parent folders in the path safely. |
| `cp <src> <dst>` | Copy a single file | `cp /etc/hosts ~/hosts.bak` | [Modifies Filesystem] Overwrites destination if target already exists. |
| `cp -r <src> <dst>` | Copy directory recursively | `cp -r /var/log/httpd /backup/` | [Modifies Filesystem] Mandatory flag (`-r`) when copying directories. |
| `cp -p <src> <dst>` | Copy preserving attributes | `cp -p /etc/fstab /etc/fstab.bak`| [Modifies Filesystem] Preserves file owner, group, permissions, and timestamps. |
| `cp -i <src> <dst>` | Copy with interactive prompt | `cp -i file1.txt file2.txt` | [Modifies Filesystem] Prompts before overwriting existing destination files. |
| `mv <src> <dst>` | Move or rename file/folder | `mv old.conf new.conf` | [Modifies Filesystem] Renames if in same folder; moves if path differs. |
| `rmdir <dir>` | Remove empty directory | `rmdir /tmp/scratch` | `⚠️ DESTRUCTIVE` Fails safely if directory contains any files or folders. |
| `rm -i <file>` | Remove file with prompt | `rm -i obsolete.txt` | `⚠️ DESTRUCTIVE` Prompts for interactive confirmation before unlinking. |
| `rm -f <file>` | Force remove without prompt | `rm -f temp.pid` | `⚠️ DESTRUCTIVE` Suppresses confirmation prompts and missing-file errors. |
| `rm -r <dir>` | Recursively remove directory | `rm -r /tmp/old_build/` | `⚠️ DESTRUCTIVE` Deletes directory and all contained files/subfolders. |
| `rm -rf <dir>` | Force recursive delete | `rm -rf /tmp/test_dir/` | `🚨 CRITICAL RISK` Irrevocably purges target tree. Never run `rm -rf /` or with unquoted spaces! |

---

## 🔗 Hard Links and Symbolic (Soft) Links

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `ln <target> <link>` | Create a Hard Link | `ln data.db data_hard.db` | [Modifies Filesystem] Shares same inode (`ls -i`); cannot span filesystems or point to directories. |
| `ln -s <target> <link>`| Create a Symbolic Link | `ln -s /etc/nginx/nginx.conf ~/conf` | [Modifies Filesystem] Creates a pointer to target path; can cross filesystems and link directories. |
| `ls -li <file>` | Inspect inode number | `ls -li /etc/hosts` | [Read-Only] `-i` displays the numerical inode identifier in the left column. |
| `readlink <symlink>` | Resolve symlink target | `readlink /bin` | [Read-Only] Prints the real destination path that the symlink points to. |

---

## 🌲 Filesystem Hierarchy Standard (FHS) Quick Index

| Directory | Administrative Role & Typical Contents | Read/Write Policy |
|---|---|:---:|
| `/` | Root directory; top of the unified Linux filesystem tree. | Root only |
| `/etc` | Host configuration files (`/etc/passwd`, `/etc/fstab`, `/etc/ssh/`). | Root only |
| `/bin` & `/sbin` | Essential user binaries (`/bin`) and system administration binaries (`/sbin`). | Root only |
| `/var` | Variable runtime data, daemons, and logs (`/var/log/`, `/var/www/`, `/var/spool/`). | Root & Daemons |
| `/home` | User personal directories (`/home/username/`). | Respective User |
| `/root` | Superuser root personal home folder (independent of `/home/`). | Root only |
| `/tmp` | Temporary scratch space; sticky bit enforced (`1777`). | World-Writable |
| `/dev` | Physical and virtual hardware device nodes (`/dev/sda`, `/dev/null`). | Kernel Managed |
| `/proc` & `/sys` | Virtual in-memory filesystems exposing kernel state and running processes. | Virtual Kernel |
| `/opt` | Optional third-party commercial application installations. | Root / App User |
| `/mnt` & `/media` | Mount points for temporary manual filesystems (`/mnt`) and automounted USBs (`/media`). | Root only |
