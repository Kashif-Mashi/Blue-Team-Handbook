# Chapter 8 – Linux File Permissions and Ownership

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand how Linux secures files and directories.
* Explain file ownership and permissions.
* Read Linux permission notation.
* Modify permissions using symbolic and numeric methods.
* Change file ownership and groups.
* Understand special permissions such as SUID, SGID, and Sticky Bit.
* Learn about the `umask` command.
* Apply Linux permissions to improve system security.

---

# Introduction

Linux is designed with security in mind. Every file and directory has a set of permissions that determine:

* Who can read it.
* Who can modify it.
* Who can execute it.

Without permissions, any user could access or modify another user's files, making the system insecure.

Linux uses a permission system based on **ownership** and **access rights**.

---

# Why Are Permissions Important?

Imagine a university computer lab.

Students should only be able to edit **their own assignments**, while teachers should be able to review all submissions.

Similarly, in Linux:

* Users should access only the files they need.
* Sensitive files should be protected.
* Administrative files should only be modified by authorized users.

Permissions enforce these security rules.

---

# File Ownership

Every file and directory has two owners:

* **User (Owner)** – The user who owns the file.
* **Group** – A group of users who share access.

Example:

```text
report.txt

Owner : kashif
Group : students
```

---

# Viewing File Permissions

Use the `ls -l` command.

```bash
ls -l
```

Example Output:

```text
-rw-r--r-- 1 kashif students 2048 Jul 25 report.txt

---

# Understanding Permission Notation

Let's break down the output:

```text
-rw-r--r--
```

```text
- rw- r-- r--
│ │   │   │
│ │   │   └── Others
│ │   └────── Group
│ └────────── Owner
└──────────── File Type
```

---

# File Type

The first character represents the file type.

| Symbol | Meaning          |
| ------ | ---------------- |
| `-`    | Regular File     |
| `d`    | Directory        |
| `l`    | Symbolic Link    |
| `c`    | Character Device |
| `b`    | Block Device     |

Example:

```text
drwxr-xr-x
```

The `d` indicates a directory.

---

# Permission Categories

Linux divides permissions into three categories.

| Category | Description                           |
| -------- | ------------------------------------- |
| Owner    | User who owns the file                |
| Group    | Users belonging to the assigned group |
| Others   | Everyone else                         |

Example:

```text
-rwxr-x---
```

| Owner | Group | Others |
| ----- | ----- | ------ |
| rwx   | r-x   | ---    |

---

# Permission Types

Linux has three basic permissions.

| Permission | Symbol | Value |
| ---------- | ------ | ----- |
| Read       | r      | 4     |
| Write      | w      | 2     |
| Execute    | x      | 1     |

---

# Read Permission (r)

Read permission allows a user to view the contents of a file.

For directories, it allows listing the directory contents.

Example:

```text
-r--------
```

---

# Write Permission (w)

Write permission allows modifying a file.

For directories, it allows creating, deleting, or renaming files inside the directory (when combined with appropriate directory permissions).

Example:

```text
-rw-------
```

---

# Execute Permission (x)

Execute permission allows a file to be run as a program or script.

For directories, it allows entering the directory using the `cd` command.

Example:

```text
-rwx------
```

---

# Numeric Permission Values

Linux combines permission values using addition.

| Permission | Calculation | Value |
| ---------- | ----------- | ----- |
| ---        | 0           | 0     |
| --x        | 1           | 1     |
| -w-        | 2           | 2     |
| -wx        | 2+1         | 3     |
| r--        | 4           | 4     |
| r-x        | 4+1         | 5     |
| rw-        | 4+2         | 6     |
| rwx        | 4+2+1       | 7     |

---

# Common Permission Values

| Numeric | Symbolic  | Meaning                                    |
| ------- | --------- | ------------------------------------------ |
| 777     | rwxrwxrwx | Full access for everyone                   |
| 755     | rwxr-xr-x | Owner full access, others read and execute |
| 700     | rwx------ | Only owner has access                      |
| 644     | rw-r--r-- | Owner can edit, others can only read       |
| 600     | rw------- | Private file                               |

---

# Command: chmod

## Purpose

Changes file or directory permissions.

---

## Syntax

```bash
chmod [options] mode filename
```

---

# Symbolic Mode

Grant execute permission to the owner.

```bash
chmod u+x script.sh
```

Remove write permission from the group.

```bash
chmod g-w report.txt
```

Grant read permission to others.

```bash
chmod o+r notes.txt
```

---

## Symbol Meaning

| Symbol | Meaning      |
| ------ | ------------ |
| u      | User (Owner) |
| g      | Group        |
| o      | Others       |
| a      | All Users    |

Operators:

| Symbol | Meaning           |
| ------ | ----------------- |
| +      | Add Permission    |
| -      | Remove Permission |
| =      | Assign Exactly    |

---

# Numeric Mode

Example:

```bash
chmod 755 script.sh
```

Explanation:

```text
7 = rwx
5 = r-x
5 = r-x
```

Another example:

```bash
chmod 644 report.txt
```

Result:

```text
Owner  : Read + Write
Group  : Read
Others : Read
---

# Command: chown

## Purpose

Changes the owner of a file or directory.

---

## Syntax

```bash
sudo chown owner filename
```

Example:

```bash
sudo chown ali report.txt
```

Changes the owner of `report.txt` to **ali**.

---

## Change Owner and Group

```bash
sudo chown ali:developers report.txt
```

Changes both the owner and group.

---

# Command: chgrp

## Purpose

Changes the group ownership of a file or directory.

---

## Syntax

```bash
sudo chgrp developers report.txt
```

---

# Command: umask

## Purpose

Controls the default permissions assigned to newly created files and directories.

---

## View Current umask

```bash
umask
```

Example Output:

```text
0022
```

---

## How umask Works

Default permissions:

Files:

```text
666
```

Directories:

```text
777
```

If the umask is:

```text
022
```

Then:

Files become:

```text
644
```

Directories become:

```text
755
```

This prevents new files from being writable by everyone.

---

# Special Permissions

Linux supports three special permission bits.

* SUID
* SGID
* Sticky Bit

These provide additional security and functionality.

---

# SUID (Set User ID)

When SUID is set on an executable file, the program runs with the permissions of the file owner instead of the user executing it.

Example:

```bash
ls -l /usr/bin/passwd
```

Output:

```text
-rwsr-xr-x
```

The `s` in the owner's execute position indicates SUID.

This allows users to change their passwords even though the password database is owned by root.

---

# SGID (Set Group ID)

When SGID is set:

* On a file, the program runs with the permissions of the file's group.
* On a directory, new files created inside inherit the directory's group ownership.

Example:

```text
drwxr-sr-x
```

---

# Sticky Bit

The Sticky Bit is commonly used on shared directories.

Example:

```text
drwxrwxrwt
```

A common example is:

```text
/tmp
```

In a Sticky Bit directory:

* Everyone can create files.
* Users can only delete their own files (unless they are the owner or root).

---

# Permission Flow

```text
               User Requests Access
                       │
                       ▼
             Is User the Owner?
                 │         │
               Yes         No
               │           │
               ▼           ▼
      Check Owner      Check Group
      Permissions      Membership
               │           │
               └─────┬─────┘
                     ▼
              Check Others
                     │
                     ▼
            Grant or Deny Access
```

---

# Blue Team Perspective

Incorrect file permissions are one of the most common causes of security incidents.

Examples include:

* World-writable configuration files.
* Scripts with unnecessary SUID permissions.
* Sensitive files readable by all users.
* Shared directories without the Sticky Bit.

During incident response, analysts often review file permissions to identify privilege escalation opportunities or unauthorized changes.

---

# Common Mistakes

* Using `chmod 777` on important files.
* Running applications with unnecessary SUID permissions.
* Giving write access to everyone.
* Forgetting to review permissions after copying files.
* Changing ownership accidentally with `chown`.

---

# Best Practices

* Follow the Principle of Least Privilege.
* Avoid using `777` unless absolutely necessary.
* Review file permissions regularly.
* Limit SUID and SGID usage.
* Use `sudo` carefully when modifying permissions.
* Protect sensitive files with restrictive permissions.

---

# Chapter Summary

In this chapter, you learned:

* How Linux controls access using permissions.
* The meaning of read, write, and execute permissions.
* How to interpret symbolic and numeric permissions.
* How to use `chmod`, `chown`, `chgrp`, and `umask`.
* The purpose of SUID, SGID, and Sticky Bit.
* Best practices for securing Linux files and directories.

---

# Interview Questions

1. What are Linux file permissions?
2. What do the symbols `r`, `w`, and `x` represent?
3. What is the difference between file owner and group?
4. What does the `chmod` command do?
5. Explain the difference between symbolic and numeric permissions.
6. What does `chmod 755` mean?
7. What is the purpose of the `chown` command?
8. What does the Sticky Bit do?
9. When should SUID be used?
10. Why is `chmod 777` considered a security risk?

---

# References

* GNU Core Utilities Manual — https://www.gnu.org/software/coreutils/
* Linux man pages — https://man7.org/linux/man-pages/
* Ubuntu Documentation — https://help.ubuntu.com/

---

