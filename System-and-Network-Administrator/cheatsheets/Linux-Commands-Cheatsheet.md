# Essential Linux Commands Cheatsheet

> **Operational Quick Reference for System Administrators & BSIT Students**  
> Companion detailed notes: [02-Common-Linux-Commands.md](../03-Linux-Fundamentals/02-Common-Linux-Commands.md)

---

## 🧭 Navigation & Directory Inspection

| Command Syntax | Operational Purpose & Key Details | Example Usage |
|---|---|---|
| `pwd` | Print current absolute working directory path | `pwd` |
| `cd <path>` | Change working directory (relative or absolute) | `cd /var/log/httpd` |
| `cd ..` | Move up one level to parent directory | `cd ..` |
| `cd ~` or `cd` | Jump directly to active user's personal home directory | `cd` |
| `cd -` | Toggle back to the immediately preceding working directory | `cd -` |
| `ls -l` | Detailed long listing (permissions, owner, group, size, date) | `ls -l /etc` |
| `ls -la` | List ALL files including hidden files (starting with `.`) | `ls -la ~` |
| `ls -lh` | Human-readable file sizes (KB, MB, GB instead of raw bytes)| `ls -lh /var/log` |
| `ls -lt` | Sort files chronologically by modification time (newest first)| `ls -lt /tmp` |
| `ls -lR` | Recursively list subdirectories and all contained files | `ls -lR /opt` |

---

## 📄 File Reading & Live Monitoring

| Command Syntax | Operational Purpose & Key Details | Example Usage |
|---|---|---|
| `cat <file>` | Print entire file content directly to screen | `cat /etc/resolv.conf` |
| `cat -n <file>` | Print file contents with line numbering | `cat -n /etc/hosts` |
| `less <file>` | Interactive scrollable pager (press `q` to quit, `/` to search) | `less /var/log/messages` |
| `head -n <N> <file>` | Display first N lines of a file (defaults to 10 lines) | `head -n 20 /etc/passwd` |
| `tail -n <N> <file>` | Display last N lines of a file (defaults to 10 lines) | `tail -n 25 /var/log/secure` |
| `tail -f <file>` | **Follow mode**: Live stream new log lines as they appear | `tail -f /var/log/httpd/access_log` |

---

## ⚡ Stream Redirection & Pipelines

| Syntax Operator | Stream Name | Operational Behavior |
|:---:|---|---|
| `command > file` | Overwrite STDOUT | Creates or **completely overwrites** file with standard output |
| `command >> file` | Append STDOUT | Creates or **appends** standard output to the end of file |
| `command 2> file` | Redirect STDERR | Diverts only error messages to file; output prints to screen |
| `command 2> /dev/null` | Discard Errors | Silences error messages (e.g. Permission Denied) into the bit bucket |
| `command &> file` | Both Streams | Redirects both STDOUT and STDERR into the same file |
| `cmd1 \| cmd2` | Pipeline | Channels STDOUT of `cmd1` directly into STDIN of `cmd2` |
| `echo $?` | Exit Status | Prints return code of previous command (`0` = success, non-zero = error) |

---

## 🔍 Text Searching & File Locating

| Command Syntax | Operational Purpose & Key Details | Example Usage |
|---|---|---|
| `grep "pattern" <file>` | Search for lines matching text string | `grep "Failed" /var/log/secure` |
| `grep -i "pattern"` | Case-insensitive text search (matches `error`, `ERROR`) | `grep -i "error" /var/log/messages` |
| `grep -v "pattern"` | Invert match: print lines that do NOT match pattern | `grep -v "^#" /etc/httpd/conf/httpd.conf` |
| `grep -n "pattern"` | Print line numbers alongside matching lines | `grep -n "Listen" /etc/httpd/conf/httpd.conf` |
| `grep -c "pattern"` | Print count of matching lines only | `grep -c "192.168.1" access.log` |
| `find <dir> -name "<pat>"`| Search directory hierarchy for matching filenames | `find /etc -name "*.conf"` |
| `find <dir> -type f -size +<N>`| Locate files larger than specified size | `find /var -type f -size +100M` |
| `wc -l <file>` | Count total number of lines in file or stream | `wc -l /etc/passwd` |

---

## 🖥️ System, Memory & Process Diagnostics

| Command Syntax | Operational Purpose & Key Details | Example Usage |
|---|---|---|
| `uname -a` | Print kernel version, architecture, and system hostname | `uname -a` |
| `uname -r` | Print active running Linux kernel release | `uname -r` |
| `uptime` | Display uptime duration, logged-in users, and load averages | `uptime` |
| `free -m` (or `-h`) | Display physical RAM and swap allocation (Inspect `available`!)| `free -m` |
| `df -h` | Display mounted filesystem disk space usage in human units | `df -h` |
| `ps aux` | Static snapshot of all running processes (BSD style) | `ps aux \| grep httpd` |
| `ps -ef` | Static snapshot of all running processes (System V style) | `ps -ef` |
| `top` | Dynamic real-time interactive process and CPU monitor | `top` (Press `M`=RAM, `P`=CPU, `q`=Quit) |
| `kill -9 <PID>` | Force terminate an unresponsive process by Process ID | `kill -9 4120` |
| `pkill <name>` | Terminate processes matching command name | `pkill httpd` |

---

## 📁 File & Directory Operations

| Command Syntax | Operational Purpose & Key Details | Safety Warning / Notes |
|---|---|---|
| `touch <file>` | Create empty file or update timestamps | Safe operation |
| `mkdir <dir>` | Create a new directory | Fails if parent directory missing |
| `mkdir -p <dir>` | Create directory and all required parent directories | Recommended enterprise practice |
| `cp <src> <dst>` | Copy file from source to destination | Overwrites destination silently |
| `cp -r <src> <dst>`| Recursively copy directory tree and contents | Mandatory for directories |
| `cp -p <src> <dst>`| Preserve original timestamps, ownership, and permissions | Recommended for configuration backups |
| `mv <src> <dst>` | Move or rename file or directory | Fast pointer update on same filesystem |
| `rm <file>` | Delete file permanently | **No Recycle Bin! Deletion is permanent** |
| `rm -rf <dir>` | Recursively and forcefully delete directory and all contents | ⚠️ **DESTRUCTIVE:** Double-check target path! |
