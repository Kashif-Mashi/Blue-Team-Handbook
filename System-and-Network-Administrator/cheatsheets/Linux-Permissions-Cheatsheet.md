# Linux Permissions and Access Control Cheatsheet

> **Operational Quick Reference for System Administrators & BSIT Students**  
> Companion detailed notes: [04-File-Permissions.md](../03-Linux-Fundamentals/04-File-Permissions.md)

---

## 🧮 Octal to Binary and Symbolic Conversion Matrix

| Octal Digit | Binary Bits | Symbolic String | Operational Meaning on Files | Operational Meaning on Directories |
|:---:|:---:|:---:|---|---|
| **`7`** | `111` (`4+2+1`) | `rwx` | Read, Write, and Execute | Read, Create/Delete files, and Enter (`cd`) |
| **`6`** | `110` (`4+2+0`) | `rw-` | Read and Write (Standard data files) | Read and Create/Delete (Cannot `cd`!) |
| **`5`** | `101` (`4+0+1`) | `r-x` | Read and Execute (Standard scripts) | Read and Enter (`cd`) (Cannot create/delete) |
| **`4`** | `100` (`4+0+0`) | `r--` | Read-only | List directory table only (Cannot `cd`!) |
| **`3`** | `011` (`0+2+1`) | `-wx` | Write and Execute (Blind append) | Create/Delete files and Enter (Cannot list `ls`)|
| **`2`** | `010` (`0+2+0`) | `-w-` | Write-only | Create/Delete files only (Cannot `cd`!) |
| **`1`** | `001` (`0+0+1`) | `--x` | Execute-only | Enter directory only (Cannot view contents) |
| **`0`** | `000` (`0+0+0`) | `---` | Zero access | Zero access (Completely forbidden) |

---

## 🎯 Common Enterprise Permission Standards

| Octal Mode | Symbolic String | User Owner (u) | Group Owner (g) | Others (o) | Enterprise Use Case |
|:---:|:---:|:---:|:---:|:---:|---|
| **`755`** | `rwxr-xr-x` | Read, Write, Exec | Read, Exec | Read, Exec | Executable shell scripts, shared directories |
| **`644`** | `rw-r--r--` | Read, Write | Read-only | Read-only | Standard configuration files, web HTML files |
| **`600`** | `rw-------` | Read, Write | Zero access | Zero access | Private SSH keys (`~/.ssh/id_rsa`), certificates |
| **`700`** | `rwx------` | Read, Write, Enter| Zero access | Zero access | User home directories, `/root` |
| **`750`** | `rwxr-x---` | Read, Write, Enter| Read, Enter | Zero access | Departmental shared folders (Zero access to others)|
| **`777`** | `rwxrwxrwx` | Full access | Full access | Full access | 🚨 **CRITICAL SECURITY RISK: NEVER USE!** |

---

## 🔧 Command Syntax: `chmod`, `chown`, and `chgrp`

### Numeric chmod:
```bash
# Set script to 755 (Owner full, group/others read and execute)
chmod 755 deploy.sh

# Protect private cryptographic key
chmod 600 ~/.ssh/id_rsa
```

### Symbolic chmod:
$$\text{Syntax:}\quad \mathbf{chmod}\quad [\mathbf{u},\mathbf{g},\mathbf{o},\mathbf{a}]\quad [+-=]\quad [\mathbf{r},\mathbf{w},\mathbf{x}]\quad \mathbf{file}$$

```bash
# Add execute permission to user owner only
chmod u+x script.py

# Remove write access from group and others
chmod go-w shared.txt

# Grant read access to everyone (all)
chmod a+r notice.txt
```

### Changing Ownership (Root Only):
```bash
# Change user owner to student
chown student /opt/file.txt

# Change user owner AND group owner simultaneously
chown student:developers /opt/file.txt

# Recursively change ownership on entire directory tree
chown -R student:developers /var/www/html
```

---

## 🛡️ Default Permissions & Umask Calculation

$$\text{Final File Permissions} = \mathbf{666} - \mathbf{umask}\qquad\mid\qquad \text{Final Directory Permissions} = \mathbf{777} - \mathbf{umask}$$

| Umask Value | New Regular File Permissions | New Directory Permissions | Environment Description |
|:---:|:---:|:---:|---|
| **`022`** | `644` (`rw-r--r--`) | `755` (`rwxr-xr-x`) | Standard RHEL default for all users |
| **`027`** | `640` (`rw-r-----`) | `750` (`rwxr-x---`) | Hardened enterprise security baseline |
| **`077`** | `600` (`rw-------`) | `700` (`rwx------`) | High security confidential workspaces |

---

## 👑 Special Permission Bits: SUID, SGID, and Sticky Bit

| Special Bit | Octal Value | Symbolic Flag | Target: Files | Target: Directories | Configuration Syntax |
|---|:---:|:---:|---|---|---|
| **SUID** | `4000` | `s` in user (`rws`) | Executes with privileges of **file owner (root)** | No operational effect | `chmod u+s <file>` or `chmod 4755 <file>` |
| **SGID** | `2000` | `s` in group (`rws`)| Executes with privileges of **group owner** | **New files inherit parent directory's group!** | `chmod g+s <dir>` or `chmod 2775 <dir>` |
| **Sticky Bit** | `1000` | `t` in others (`rwt`)| No operational effect | **Users can only delete files they personally own!** | `chmod +t <dir>` or `chmod 1777 <dir>` |
