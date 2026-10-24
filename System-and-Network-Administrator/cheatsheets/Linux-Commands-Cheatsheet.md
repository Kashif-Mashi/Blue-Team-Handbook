# Linux Commands and CLI Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [02-Common-Linux-Commands.md](../03-Linux-Fundamentals/02-Common-Linux-Commands.md) | [Cheatsheets Index](README.md)

---

## 🧭 Navigation & Directory Inspection

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `pwd` | Print working directory | `pwd` | [Read-Only] Prints the full absolute path from `/`. |
| `cd <path>` | Change directory | `cd /var/log` | [Read-Only] Changes the shell's active working directory. |
| `cd` or `cd ~` | Return to home directory | `cd` | [Read-Only] Jumps to current user's home folder (`$HOME`). |
| `cd ..` | Move up one directory | `cd ..` | [Read-Only] Traverses to the immediate parent directory. |
| `cd -` | Toggle previous directory | `cd -` | [Read-Only] Returns to `$OLDPWD`. |
| `ls` | List files and folders | `ls` | [Read-Only] Basic directory listing. |
| `ls -l` | Long format listing | `ls -l /etc` | [Read-Only] Shows permissions, links, owner, group, size, and timestamp. |
| `ls -la` | List all including hidden | `ls -la ~` | [Read-Only] Reveals dotfiles (`.bashrc`, `.ssh`). |
| `ls -lh` | Human-readable file sizes | `ls -lh /var/log` | [Read-Only] Formats byte counts into K, M, G units. |
| `ls -ld <dir>` | Inspect directory metadata | `ls -ld /tmp` | [Read-Only] Shows permissions of directory itself rather than contents. |
| `ls -ltr` | Reverse time sort | `ls -ltr /var/log` | [Read-Only] Newest modified files appear at the very bottom. |

---

## 📄 File Display & Log Viewing

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `cat <file>` | Display entire file | `cat /etc/resolv.conf` | [Read-Only] ⚠️ Avoid on large files; dumps everything to terminal. |
| `tac <file>` | Display file in reverse | `tac file.txt` | [Read-Only] Prints bottom line first to top line last. |
| `head -n <N> <file>` | Display first N lines | `head -n 20 /etc/passwd` | [Read-Only] Defaults to 10 lines if `-n` is omitted. |
| `tail -n <N> <file>` | Display last N lines | `tail -n 50 /var/log/messages`| [Read-Only] Inspects most recent log entries. |
| `tail -f <file>` | Follow live log output | `tail -f /var/log/secure` | [Read-Only] Continuously streams new appends. Exit with `Ctrl+C`. |
| `less <file>` | Interactive file pager | `less /var/log/dmesg` | [Read-Only] Navigate with arrows, search with `/pattern`, quit with `q`. |

---

## 🔀 Redirection & Standard Streams

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `> <file>` | Overwrite stdout to file | `hostname > host.txt` | `⚠️ DESTRUCTIVE` Completely wipes existing file contents before writing. |
| `>> <file>` | Append stdout to file | `date >> uptime.log` | [Modifies File] Preserves existing content; appends to the bottom. |
| `2> <file>` | Redirect stderr only | `find /etc -name "*.conf" 2> /dev/null` | [Modifies File] Captures or suppresses permission denied errors. |
| `&> <file>` | Redirect stdout AND stderr | `command &> run.log` | `⚠️ DESTRUCTIVE` BASH syntax to redirect both streams simultaneously. |
| `cmd1 \| cmd2` | Pipe output to input | `cat /etc/passwd \| wc -l` | [In-Memory] Streams stdout of `cmd1` directly into stdin of `cmd2`. |

---

## 🔍 Text Processing & Data Filtering

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `grep "<pattern>" <file>`| Search for text string | `grep "root" /etc/passwd` | [Read-Only] Case-sensitive by default. |
| `grep -i "<pattern>"` | Case-insensitive search | `grep -i "failed" /var/log/secure`| [Read-Only] Matches lowercase and uppercase variations. |
| `grep -v "<pattern>"` | Invert match | `grep -v "^#" /etc/sudoers` | [Read-Only] Displays lines that DO NOT match pattern. |
| `grep -E "<regex>"` | Extended regex search | `grep -E "404\|500" access.log` | [Read-Only] Supports ERE operators (`\|`, `+`, `?`) natively. |
| `sort <file>` | Sort lines alphabetically | `sort names.txt` | [Read-Only] Default alphabetical sorting. |
| `sort -n` | Sort numerically | `sort -n numbers.txt` | [Read-Only] Treats input values as numbers rather than characters. |
| `sort -r` | Reverse sort order | `sort -nr scores.txt` | [Read-Only] Sorts largest numbers first. |
| `uniq` | Remove adjacent duplicates| `sort list.txt \| uniq` | [Read-Only] ⚠️ Input MUST be sorted first; ignores non-adjacent duplicates. |
| `uniq -c` | Count unique frequencies | `sort list.txt \| uniq -c` | [Read-Only] Prefixes each entry with its occurrence count. |
| `wc -l <file>` | Count total lines | `wc -l /etc/passwd` | [Read-Only] Counts newline characters in file or stream. |
| `cut -d: -f1,7 <file>` | Extract specific columns | `cut -d: -f1,7 /etc/passwd` | [Read-Only] `-d` sets delimiter (`:`), `-f` chooses field indices. |
