# Linux Permissions and Ownership Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [04-File-Permissions.md](../03-Linux-Fundamentals/04-File-Permissions.md) | [Cheatsheets Index](README.md)

---

## 🔢 Octal Permission Calculation Matrix

Each triad (User, Group, Others) is calculated by summing the active bits: **Read = 4**, **Write = 2**, **Execute = 1**.

| Octal Value | Binary | Symbolic | Meaning on Regular Files | Meaning on Directories |
|:---:|:---:|:---:|---|---|
| **0** | `000` | `---` | Zero access | Cannot enter, list, or access files |
| **1** | `001` | `--x` | Execute as program / script | Enter directory (`cd`), but cannot list filenames |
| **2** | `010` | `-w-` | Modify / write to file | Add, rename, or delete files inside directory |
| **3** | `011` | `-wx` | Write and Execute | Enter directory and create/delete files inside |
| **4** | `100` | `r--` | Read / view file contents | Read directory list (`ls`), but cannot access inodes |
| **5** | `101` | `r-x` | Read and Execute | Standard directory traversal and file listing (`ls`, `cd`) |
| **6** | `110` | `rw-` | Read and Write | Read and modify directory table (rarely used alone) |
| **7** | `111` | `rwx` | Full read, write, and execute | Full directory administration and entry |

---

## 🛠️ Modifying Permissions (`chmod`)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `chmod 644 <file>` | Standard file preset | `chmod 644 /etc/resolv.conf` | [Modifies Perms] User: `rw-` (6), Group: `r--` (4), Others: `r--` (4). |
| `chmod 755 <file/dir>` | Standard script/dir preset | `chmod 755 /opt/backup.sh` | [Modifies Perms] User: `rwx` (7), Group: `r-x` (5), Others: `r-x` (5). |
| `chmod 600 <file>` | Private file preset | `chmod 600 ~/.ssh/id_rsa` | [Modifies Perms] Owner read/write only. Mandatory for SSH private keys! |
| `chmod 700 <dir>` | Private directory preset | `chmod 700 ~/.ssh` | [Modifies Perms] Only user owner can enter or access files inside. |
| `chmod -R <mode> <dir>`| Recursive permission change | `chmod -R 750 /opt/secure/` | [Modifies Perms] Applies permissions to directory and all nested contents. |
| `chmod u+x <file>` | Add execute for owner | `chmod u+x deploy.sh` | [Symbolic] Adds `x` to User class (`u`) only. |
| `chmod go-w <file>` | Remove write from group/others| `chmod go-w config.php` | [Symbolic] Strips `w` from Group (`g`) and Others (`o`). |
| `chmod a+r <file>` | Add read for all users | `chmod a+r notice.txt` | [Symbolic] Grants read to User, Group, and Others simultaneously. |

> 🚨 **CRITICAL WARNING AGAINST `chmod 777`:**  
> Running `chmod 777 <target>` grants **all three permission classes (Owner, Group, and Others/World) unrestricted Read, Write, and Execute access**. Any local user or compromised service process on the system can overwrite, corrupt, or delete the file. Never use `777` to resolve permission errors; configure proper group membership and apply `644`, `755`, or `750` instead.

---

## 👤 Modifying Ownership (`chown` & `chgrp`)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `chown <user> <file>` | Change user owner | `chown student /opt/notes.txt` | [Root Only] Transfers file ownership to another user. |
| `chown <user>:<group>` | Change user AND group | `chown apache:apache /var/www/` | [Root Only] Simultaneously reassigns owner and owning group. |
| `chown :<group> <file>`| Change group owner only | `chown :developers /var/code` | [Root / Owner] Group can also be altered via `chgrp developers <file>`.|
| `chown -R <user>:<group>`| Recursive ownership change | `chown -R mysql:mysql /var/lib/mysql`| [Root Only] Reassigns ownership down through all subfolders. |

---

## 🔒 Special Permissions (SUID, SGID, Sticky Bit)

| Special Bit | Octal Prefix | Symbolic Indicator | Operational Function | Example Command |
|:---:|:---:|:---:|---|---|
| **SUID** | `4000` | `s` in user (`-rwsr-xr-x`) | Process executes with privileges of the file owner (e.g., `/usr/bin/passwd`). | `chmod 4755 <binary>` |
| **SGID (Files)** | `2000` | `s` in group (`-rwxr-sr-x`)| Process executes with privileges of the file's group. | `chmod 2755 <binary>` |
| **SGID (Dirs)** | `2000` | `s` in group (`drwxr-sr-x`)| **Team Collaboration**: New files created inside inherit the directory's owning group. | `chmod 2775 /var/projects` |
| **Sticky Bit** | `1000` | `t` in others (`drwxrwxrwt`)| **Shared Deletion Restriction**: Only file owner or root can delete files in folder (e.g., `/tmp`). | `chmod 1777 /tmp` |

---

## 🎭 Umask (Default Creation Mask) Calculation

| Baseline | Minus Umask `022` (Standard) | Resulting Permission | Minus Umask `077` (Strict) | Resulting Strict Permission |
|---|---|---|---|---|
| **Files Baseline:** `666` | `666 - 022` | **`644` (`rw-r--r--`)** | `666 - 077` | **`600` (`rw-------`)** |
| **Dirs Baseline:** `777` | `777 - 022` | **`755` (`rwxr-xr-x`)** | `777 - 077` | **`700` (`rwx------`)** |

```bash
# Display active shell umask
umask

# Enforce strict private creation mask for current session
umask 077
```
