# Chapter 6 – File and Directory Management

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand the difference between files and directories.
* Create files and directories.
* Copy, move, rename, and delete files and directories.
* View and inspect file contents.
* Search for files efficiently.
* Understand file metadata.
* Apply file management skills in everyday Linux administration and cybersecurity tasks.

---

# Introduction

Everything in Linux revolves around **files** and **directories**.

Whether you are editing configuration files, reviewing logs, installing software, or analyzing malware, you will constantly work with files and folders.

Linux provides powerful commands to manage these resources quickly and efficiently.

---

# What is a File?

A **file** is a collection of data stored on a storage device.

Examples include:

* Documents
* Images
* Videos
* Configuration files
* Log files
* Programs
* Scripts

Example:

```text
report.pdf
notes.txt
script.sh
```

---

# What is a Directory?

A **directory** (also called a folder) is a container used to organize files and other directories.

Example:

```text
Documents/
├── Assignment.docx
├── Notes.pdf
└── Images/
```

Directories make it easier to organize and locate information.

---

# File Management Workflow

```text
Create
   │
   ▼
Edit
   │
   ▼
Copy
   │
   ▼
Move / Rename
   │
   ▼
Delete
```

This is the typical lifecycle of a file in Linux.

---

# Command: mkdir

## Purpose

Creates a new directory.

---

## Syntax

```bash
mkdir directory_name
```

---

## Example

```bash
mkdir LinuxNotes
```

Creates a directory named **LinuxNotes**.

---

## Create Multiple Directories

```bash
mkdir Docs Images Videos
```

Creates three directories.

---

## Create Parent Directories

```bash
mkdir -p Projects/Linux/Chapter1
```

The `-p` option creates all missing parent directories automatically.

---

# Command: touch

## Purpose

Creates an empty file.

---

## Syntax

```bash
touch filename
```

---

## Example

```bash
touch notes.txt
```

Creates an empty file called **notes.txt**.

---

## Create Multiple Files

```bash
touch chapter1.md chapter2.md chapter3.md
```
---

# Command: cp

## Purpose

Copies files or directories.

---

## Syntax

```bash
cp source destination
```

---

## Example

```bash
cp notes.txt backup.txt
```

Creates a copy named **backup.txt**.

---

## Copy a Directory

```bash
cp -r LinuxNotes Backup
```

The `-r` (recursive) option copies the directory and all of its contents.

---

## Useful Options

| Option | Description                  |
| ------ | ---------------------------- |
| `-r`   | Copy directories recursively |
| `-v`   | Display copied files         |
| `-i`   | Ask before overwriting files |

---

# Command: mv

## Purpose

Moves or renames files and directories.

---

## Syntax

```bash
mv source destination
```

---

## Rename a File

```bash
mv notes.txt linux_notes.txt
```

---

## Move a File

```bash
mv report.pdf Documents/
```

Moves the file into the **Documents** directory.

---

## Move a Directory

```bash
mv LinuxNotes Documents/
```
---

# Command: rm

## Purpose

Deletes files and directories.

---

## Syntax

```bash
rm filename
```

---

## Example

```bash
rm notes.txt
```

Deletes the file permanently.

> **Warning:** Files deleted with `rm` are not moved to a recycle bin.

---

## Delete Multiple Files

```bash
rm file1.txt file2.txt file3.txt
```

---

## Delete a Directory

```bash
rm -r LinuxNotes
```

The `-r` option removes directories recursively.

---

## Force Delete

```bash
rm -rf LinuxNotes
```

Options:

* `-r` → Recursive deletion
* `-f` → Force deletion without confirmation

⚠️ **Be extremely careful with `rm -rf`.** It can permanently remove large portions of the file system if used incorrectly.
---

# Command: rmdir

## Purpose

Deletes an empty directory.

---

## Syntax

```bash
rmdir directory_name
```

---

## Example

```bash
rmdir EmptyFolder
```

If the directory contains files, the command will fail.

---

# Command: cat

## Purpose

Displays the contents of a text file.

---

## Syntax

```bash
cat filename
```

---

## Example

```bash
cat notes.txt
```

Displays the entire file.

---

## Combine Files

```bash
cat file1.txt file2.txt
```

Displays both files one after another.
---

# Command: less

## Purpose

Views large files one page at a time.

---

## Syntax

```bash
less filename
```

---

## Example

```bash
less /var/log/syslog
```

Useful for reading long log files without loading the entire file at once.

Navigation:

* Space → Next page
* b → Previous page
* q → Quit

---

# Command: head

## Purpose

Displays the beginning of a file.

---

## Syntax

```bash
head filename
```

---

## Example

```bash
head notes.txt
```

Displays the first 10 lines by default.

---

## Display First Five Lines

```bash
head -5 notes.txt
```

---

# Command: tail

## Purpose

Displays the end of a file.

---

## Syntax

```bash
tail filename
```

---

## Example

```bash
tail notes.txt
```

Displays the last 10 lines.

---

## Monitor a File in Real Time

```bash
tail -f /var/log/auth.log
```

The `-f` option continuously displays new content as it is added.

This is especially useful for monitoring log files.
---

# Command: file

## Purpose

Identifies the type of a file.

---

## Syntax

```bash
file filename
```

---

## Example

```bash
file report.pdf
```

Example Output

```text
report.pdf: PDF document
```

Useful when a file has no extension or its extension is misleading.

---

# Command: stat

## Purpose

Displays detailed information about a file or directory.

---

## Syntax

```bash
stat filename
```

---

## Example

```bash
stat notes.txt
```

Information displayed includes:

* File size
* Permissions
* Owner
* Group
* Last access time
* Last modification time
* Creation information (if supported)

---

# Command: find

## Purpose

Searches for files and directories.

---

## Syntax

```bash
find location criteria
```

---

## Find a File

```bash
find /home -name notes.txt
```

---

## Find All PDF Files

```bash
find . -name "*.pdf"
```

---

## Find Directories

```bash
find . -type d
```

---

## Find Files

```bash
find . -type f
```
---

# Command: locate

## Purpose

Searches for files using a prebuilt database.

---

## Syntax

```bash
locate filename
```

---

## Example

```bash
locate passwd
```

Unlike `find`, `locate` is much faster because it searches an indexed database.

> **Note:** The database must be updated periodically using the `updatedb` command (usually run automatically by the system).

---

# Blue Team Perspective

File management skills are essential during security investigations.

Common tasks include:

* Examining suspicious files.
* Searching for malware.
* Reviewing configuration files.
* Monitoring log files.
* Copying forensic evidence.
* Preserving important artifacts before analysis.

Commands such as `find`, `file`, `stat`, `cat`, `less`, and `tail` are frequently used by SOC analysts and incident responders.

---

# Common Mistakes

* Using `rm -rf` without verifying the target.
* Confusing `mv` (move) with `cp` (copy).
* Editing or deleting files while in the wrong directory.
* Using `cat` to open very large log files instead of `less`.
* Forgetting to use `-r` when copying directories.

---

# Best Practices

* Verify your current directory before modifying files.
* Use `cp` to create backups before editing important files.
* Use `less` for large files instead of `cat`.
* Double-check commands that delete data.
* Use descriptive file and directory names.

---

# Chapter Summary

In this chapter, you learned:

* The difference between files and directories.
* How to create, copy, move, rename, and delete files.
* How to inspect file contents.
* How to search for files.
* How to identify file types and view metadata.
* Best practices for managing files safely.

---

# Interview Questions

1. What is the difference between a file and a directory?
2. What does the `mkdir` command do?
3. What is the purpose of the `touch` command?
4. What is the difference between `cp` and `mv`?
5. When should you use `less` instead of `cat`?
6. What does the `tail -f` command do?
7. What information does the `stat` command provide?
8. What is the difference between `find` and `locate`?
9. Why is `rm -rf` considered dangerous?
10. Which command is used to determine a file's type?

---

# References

* GNU Core Utilities Manual — https://www.gnu.org/software/coreutils/
* The Linux Documentation Project — https://tldp.org/
* Ubuntu Documentation — https://help.ubuntu.com/

---
