# Chapter 5 – Navigation Commands

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand how Linux organizes directories.
* Navigate through the Linux file system confidently.
* Understand the difference between absolute and relative paths.
* Use common navigation commands.
* Display hidden files and detailed directory information.
* Understand tab completion.
* Interpret command output.

---

# Introduction

One of the first skills every Linux user must learn is **navigation**.

Before creating files, editing configuration files, analyzing logs, or installing software, you must know **where you are** and **how to move** through the Linux file system.

Linux navigation is performed using commands instead of clicking folders like in Windows.

Once mastered, command-line navigation is often faster and more efficient than using a graphical interface.

---

# Understanding the Linux Directory Structure

Linux stores every file and directory under a single root directory (`/`).

Example:

```text
/
├── home
│   └── kashif
│       ├── Documents
│       ├── Downloads
│       └── Desktop
├── etc
├── var
├── tmp
└── usr
```

To work with files, you move through this directory tree.

---

# Current Working Directory

The **Current Working Directory (CWD)** is the directory you are currently using.

Every command you execute runs from the current directory unless another location is specified.

Example:

```text
Current Directory

/home/kashif/Documents
```

---

# Absolute Path vs Relative Path

Understanding paths is essential.

## Absolute Path

An absolute path always starts from the root directory (`/`).

Example:

```text
/home/kashif/Documents/report.txt
```

Characteristics:

* Starts with `/`
* Always points to the same location
* Works regardless of your current directory

---

## Relative Path

A relative path starts from your current working directory.

Suppose your current directory is:

```text
/home/kashif
```

To access the Documents folder:

```text
Documents
```

or

```text
Documents/report.txt
```

No leading `/` is used.

---

## Comparison

| Absolute Path        | Relative Path                      |
| -------------------- | ---------------------------------- |
| Starts from `/`      | Starts from the current directory  |
| Always the same      | Depends on where you currently are |
| Easier to understand | Shorter and quicker to type        |

---

# Special Directory Symbols

Linux uses special symbols to represent locations.

| Symbol | Meaning           |
| ------ | ----------------- |
| `.`    | Current directory |
| `..`   | Parent directory  |
| `~`    | Home directory    |
| `/`    | Root directory    |

Example:

```text
.
```

means

Current directory.

Example:

```text
..
```

means

Move one directory up.

Example:

```text
~
```

means

Your home directory.

---

# Command: pwd

## Purpose

Displays the current working directory.

---

## Syntax

```bash
pwd
```

---

## Example

```bash
pwd
```

Output

```text
/home/kashif/Documents
```

---

## Explanation

Whenever you are unsure where you are in the Linux file system, use `pwd`.

---

## Common Uses

* Confirm your location.
* Before creating files.
* Before deleting files.
* During scripting.
---

# Command: ls

## Purpose

Displays the contents of a directory.

---

## Syntax

```bash
ls
```

---

## Example

```bash
ls
```

Output

```text
Desktop
Documents
Downloads
Music
Pictures
```

---

## Explanation

The command lists all visible files and folders inside the current directory.

---

## Useful Options

### ls -l

Shows detailed information.

```bash
ls -l
```

Example Output

```text
drwxr-xr-x 2 kashif users 4096 Jul 20 Documents
```

Displays:

* Permissions
* Owner
* Group
* File Size
* Modification Date
* File Name

---

### ls -a

Displays hidden files.

```bash
ls -a
```

Example

```text
.
..
.bashrc
.profile
Documents
Downloads
```

Files beginning with a dot (`.`) are hidden.

---

### ls -la

Displays both hidden files and detailed information.

```bash
ls -la
```

---

### ls -lh

Displays file sizes in a human-readable format.

```bash
ls -lh
```

Example

```text
1.2K
15M
2.5G
```
# Command: cd

## Purpose

Changes the current directory.

---

## Syntax

```bash
cd directory_name
```

---

## Example

Move into Documents.

```bash
cd Documents
```

---

Move to the home directory.

```bash
cd
```

or

```bash
cd ~
```

---

Move to the parent directory.

```bash
cd ..
```

---

Move to the root directory.

```bash
cd /
```

---

Move using an absolute path.

```bash
cd /var/log
```

---

Move using a relative path.

```bash
cd Documents/Projects
```
---

# Command: tree

## Purpose

Displays directories in a tree-like structure.

---

## Syntax

```bash
tree
```

Example Output

```text
.
├── Documents
├── Downloads
├── Pictures
└── Videos
```

This command makes it easier to visualize directory structures.

> **Note:** The `tree` command may not be installed by default on all Linux distributions. You can install it using your distribution's package manager.

---

# Tab Completion

Linux supports automatic command completion.

Example

Instead of typing

```text
Documents
```

Type

```text
Doc
```

Then press:

```text
TAB
```

The shell automatically completes the directory name if it is unique.

Benefits:

* Faster typing
* Fewer mistakes
* Better productivity

---

# Command History

Linux remembers previously executed commands.

Use:

```bash
history
```

to display the command history.

You can also use the:

* ↑ Up Arrow
* ↓ Down Arrow

to navigate through previously entered commands.

---

# Blue Team Perspective

Navigation commands are used constantly during security investigations.

Examples:

* Navigating to `/var/log` to examine system logs.
* Moving to `/etc` to review configuration files.
* Accessing a user's home directory to inspect suspicious files.
* Exploring `/tmp` to identify temporary files left by malware.

Knowing how to navigate efficiently reduces investigation time and helps analysts avoid mistakes.

---

# Common Mistakes

* Confusing `/` (root directory) with `~` (home directory).
* Forgetting whether a path is absolute or relative.
* Running commands in the wrong directory.
* Assuming hidden files do not exist because `ls` does not display them by default.

---

# Best Practices

* Use `pwd` frequently to confirm your location.
* Prefer absolute paths when performing administrative tasks.
* Use `ls -la` when troubleshooting.
* Take advantage of tab completion to reduce typing errors.
* Verify your current directory before modifying or deleting files.

---

# Chapter Summary

In this chapter, you learned:

* What the current working directory is.
* The difference between absolute and relative paths.
* The purpose of special directory symbols.
* How to use `pwd`, `ls`, `cd`, `tree`, and `history`.
* How to use tab completion.
* Why navigation is important for Linux administration and security investigations.

---

# Interview Questions

1. What is the current working directory?
2. What is the difference between an absolute path and a relative path?
3. What does the `pwd` command do?
4. What is the purpose of the `cd` command?
5. What is the difference between `ls` and `ls -la`?
6. What does `cd ..` do?
7. What does the `~` symbol represent?
8. Why are hidden files important?
9. What is tab completion?
10. Why should administrators use absolute paths?

---

# References

* The Linux Documentation Project — https://tldp.org/
* GNU Core Utilities Manual — https://www.gnu.org/software/coreutils/
* Ubuntu Documentation — https://help.ubuntu.com/

---

