# Common Linux Commands and CLI Operations

> **Module:** System and Network Administrator (SNA) — 03 Linux Fundamentals  
> **Topic Level:** Core Command-Line Mechanics  
> **Previous Reference:** [01-Introduction-to-RHEL.md](01-Introduction-to-RHEL.md) | **Next:** [03-File-Management.md](03-File-Management.md)

---

## 🎯 Learning Objectives

By the end of this note, you will be able to:

- Deconstruct the anatomy of a Linux command: **Executable**, **Options (flags)**, and **Arguments**.
- Navigate the filesystem confidently using `pwd`, `cd`, and `ls` with essential flags.
- Master standard streams (**stdin 0**, **stdout 1**, **stderr 2**) and file redirection (`>`, `>>`, `2>`).
- Construct multi-stage command pipelines using the pipe (`|`) operator.
- Process, filter, and summarize text files using `cat`, `head`, `tail`, `sort`, `uniq`, `wc`, and `grep`.
- Prevent common command mistakes and dangerous terminal habits.

---

## 1. Introduction and Context

The graphical user interface (GUI) is convenient for desktop workstations, but enterprise servers are deployed "headless" without a GUI to conserve RAM, CPU cycles, and reduce the attack surface. For a System and Network Administrator, the **Bourne Again Shell (BASH)** is the primary operational cockpit.

Every task—from diagnosing service failures to configuring network interfaces and managing accounts—is executed by typing commands at the prompt. Understanding command execution semantics, output streams, and text manipulation pipelines is the single most critical practical skill for an administrator.

```mermaid
flowchart TD
    subgraph Execution["Command Execution & Pipeline Flow"]
        direction TB
        INPUT["Standard Input (stdin / fd 0)<br/>Keyboard or Piped Stream"] --> CMD["Command Process<br/>(e.g., grep / sort / wc)"]
        CMD -->|Standard Output (stdout / fd 1)| STDOUT["Terminal Screen OR File Redirect (> / >>)"]
        CMD -->|Standard Error (stderr / fd 2)| STDERR["Terminal Screen OR Error Log (2>)"]
        STDOUT -.->|Pipe Operator (|)| NEXTCMD["Subsequent Command Process"]
    end

    style Execution fill:#1e293b,stroke:#3b82f6,color:#fff
    style INPUT fill:#0f172a,stroke:#38bdf8,color:#fff
    style CMD fill:#0f172a,stroke:#f59e0b,color:#fff
    style STDOUT fill:#0f172a,stroke:#10b981,color:#fff
    style STDERR fill:#0f172a,stroke:#ef4444,color:#fff
    style NEXTCMD fill:#0f172a,stroke:#8b5cf6,color:#fff
```

---

## 2. Definitions of Important Terminology

| Term | Definition |
|---|---|
| **Shell** | The command-line interpreter that reads instructions typed by the user, translates them into system calls, and requests the Linux kernel to execute them. |
| **Command Anatomy** | The structural breakdown: `command -options argument(s)` (e.g., `ls -l /var/log`). |
| **Option / Switch / Flag** | A modifier passed to a command (typically prefixed with `-` for short options or `--` for long options) that changes its execution behavior. |
| **Standard Streams** | The three default I/O channels opened for every Linux process: `stdin` (file descriptor 0), `stdout` (descriptor 1), and `stderr` (descriptor 2). |
| **Pipeline (`|`)** | A Unix mechanism that redirects the `stdout` of one command directly into the `stdin` of another command in memory without writing temporary files to disk. |
| **Filter** | A program that accepts text input, performs a transformation (sorting, pattern matching, counting), and emits the result to standard output. |

---

## 3. Core Command Categories and Syntax

### 3.1 Directory Navigation & Inspection

```bash
# Display the Present Working Directory (full absolute path)
pwd

# Change current working directory to a specific path
cd /var/log

# Return to the current user's home directory (~ or $HOME)
cd
cd ~

# Move up one level to the parent directory
cd ..

# Toggle back to the previous working directory (OLDPWD)
cd -
```

### The `ls` Command (List Storage Artifacts)
```bash
# Basic listing (names only)
ls

# Long listing format: permissions, hard links, owner, group, file size, timestamp, name
ls -l

# Show all files, including hidden dotfiles (.bashrc, .ssh)
ls -la

# Long listing with human-readable file sizes (K, M, G instead of raw bytes)
ls -lh

# List directory metadata itself rather than listing its contents
ls -ld /etc/

# Sort files by modification time, newest first
ls -lt

# Sort files by modification time in reverse order (oldest first, useful for spotting new logs)
ls -ltr
```

---

### 3.2 File Viewing and Display

| Command | Behavior | Typical Administrative Use Case |
|---|---|---|
| `cat <file>` | Concatenates and dumps entire file contents to screen | Small configuration files (`/etc/resolv.conf`) |
| `tac <file>` | Dumps file contents in reverse order (bottom line first) | Reviewing chronological logs in reverse |
| `head -n <N> <file>` | Displays first N lines (default: 10) | Inspecting headers or top records of CSVs |
| `tail -n <N> <file>` | Displays last N lines (default: 10) | Checking the most recent log events |
| `tail -f <file>` | Follows the file in real-time as new lines are appended | Live troubleshooting daemon activity |
| `less <file>` | Interactive pager allowing scrolling up/down with search (`/`) | Large configuration files, manuals, system logs |

---

### 3.3 Redirection and Stream Management

```bash
# Overwrite standard output to a file (creates file if not present, replaces if present)
cat /etc/redhat-release > ~/os_info.txt

# Append standard output to the end of a file (preserves existing contents)
date >> ~/os_info.txt

# Redirect standard error (fd 2) to a separate log file
find /etc -name "*.conf" 2> /tmp/errors.log

# Suppress errors by redirecting stderr to the bit-bucket (/dev/null)
find /etc -name "*.conf" 2> /dev/null

# Redirect both standard output and standard error to the same destination
command > /tmp/all_output.log 2>&1
# Or in modern BASH syntax:
command &> /tmp/all_output.log
```

---

### 3.4 Text Filtering and Data Wrangling

#### 1. `grep` (Global Regular Expression Print)
```bash
# Search for case-sensitive match
grep "root" /etc/passwd

# Search case-insensitively (-i)
grep -i "error" /var/log/messages

# Invert match (-v): display lines that DO NOT match pattern
grep -v "^#" /etc/httpd/conf/httpd.conf | grep -v "^$"

# Display line numbers (-n)
grep -n "Failed password" /var/log/secure

# Recursive search through directory tree (-r)
grep -r "192.168.1.100" /etc/sysconfig/
```

#### 2. `sort` & `uniq`
```bash
# Sort lines alphabetically
sort names.txt

# Sort lines numerically (-n)
sort -n numbers.txt

# Sort in reverse order (-r)
sort -nr scores.txt

# Filter out duplicate ADJACENT lines (Note: input must be sorted first!)
sort list.txt | uniq

# Count occurrences of unique items (-c)
cut -d: -f7 /etc/passwd | sort | uniq -c
```

#### 3. `wc` (Word Count)
```bash
# Print line count, word count, and byte count
wc /etc/passwd

# Count lines only (-l)
cat /etc/passwd | wc -l

# Count words only (-w)
wc -w document.txt
```

---

## 4. Multi-Stage Pipeline Example

Suppose you need to find the top three login shells used on a server:

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -nr | head -n 3
```

**Step-by-Step Breakdown:**
1. `cut -d: -f7 /etc/passwd` extracts the 7th field (shell path) from each line of `/etc/passwd`.
2. `| sort` sorts the shells so identical entries become adjacent.
3. `| uniq -c` collapses duplicates and prefixes each line with its frequency count.
4. `| sort -nr` sorts the results numerically in descending order (highest count first).
5. `| head -n 3` displays the top 3 most common login shells on the system.

---

## 5. Common Operational Pitfalls

- **Confusing `>` with `>>`**:
  - `>` truncates and overwrites the target file immediately. Running `echo "test" > /etc/resolv.conf` wipes your entire DNS configuration.
  - Always use `>>` when appending data to existing system configuration files.
- **Forgetting that `uniq` requires sorted input**:
  - `uniq` only removes duplicate entries if they appear consecutively. If duplicates are separated by other lines, `uniq` ignores them. Always pipe through `sort` before `uniq`.
- **Viewing huge log files with `cat`**:
  - Running `cat /var/log/messages` on a multi-gigabyte production server dumps millions of lines to the terminal, exhausting terminal buffers and locking up remote sessions. Use `less` or `tail -n 100` instead.

---

## 6. Security Considerations

1. **Information Leakage in Command Arguments**: Command arguments (e.g., passing passwords like `mysql -u root -pSecret123`) are visible to all users on the system via the `ps aux` process table and are recorded in `~/.bash_history`. Never supply passwords on the command line.
2. **History Scrubbing**: When working with sensitive variables, prefix commands with a leading space (if `HISTCONTROL=ignorespace` is enabled) or run `history -c` to clear the in-memory session history when necessary.

---

## 7. Summary & Next Steps

Command-line efficiency relies on understanding standard streams, navigation tools, and combining specialized text utilities with pipes. Mastering these primitives prepares you for filesystem management, permission audits, and user administration.

- **Next Chapter:** Explore the Linux directory tree and file operations in [03-File-Management.md](03-File-Management.md).
- **Security Permissions:** Learn how access controls protect files in [04-File-Permissions.md](04-File-Permissions.md).
- **Quick Reference:** Keep [../cheatsheets/Linux-Commands-Cheatsheet.md](../cheatsheets/Linux-Commands-Cheatsheet.md) open for instant terminal lookups.
