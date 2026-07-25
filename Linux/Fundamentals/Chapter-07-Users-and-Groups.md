# Chapter 7 – Users and Groups

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand how Linux manages users and groups.
* Differentiate between the root user and regular users.
* Understand User IDs (UID) and Group IDs (GID).
* Learn the purpose of important account files.
* Manage users and groups using common Linux commands.
* Understand the importance of user management in Linux security.

---

# Introduction

Linux is a **multi-user operating system**, meaning multiple users can access the same computer while keeping their files and settings separate.

Every user has:

* A username
* A password
* A unique User ID (UID)
* A primary group
* A home directory
* A default shell

User management is one of the most important aspects of Linux administration because it controls **who can access the system and what they are allowed to do**.

---

# Multi-User Environment

A Linux system allows multiple users to work independently.

Example:

```text
Linux Server
│
├── Alice
│   ├── Documents
│   └── Downloads
│
├── Bob
│   ├── Projects
│   └── Pictures
│
└── Charlie
    ├── Reports
    └── Music
```

Each user has their own files and settings.

---

# What is a User?

A **user** is an account that allows someone to log in to the Linux system.

Every user has:

* Username
* Password
* UID
* Home Directory
* Default Shell

Example:

```text
Username : kashif
Home     : /home/kashif
Shell    : /bin/bash
UID       : 1000
```

---

# Types of Users

Linux generally has three types of users.

## 1. Root User

The **root user** is the administrator of the Linux system.

Characteristics:

* Has complete control over the system.
* Can access all files.
* Can install or remove software.
* Can create and delete users.
* Can modify system configuration.

Prompt:

```text
root@ubuntu:~#
```

The `#` symbol usually indicates the root user.

---

## 2. Regular User

A regular user has limited permissions.

They can:

* Create personal files.
* Edit files they own.
* Install software only if permitted.
* Cannot modify critical system files without elevated privileges.

Prompt:

```text
kashif@ubuntu:~$
```

The `$` symbol usually indicates a normal user.

---

## 3. System Users

System users are created automatically for services and applications.

Examples:

* www-data
* mysql
* nobody
* daemon

These accounts usually cannot log in interactively and are used to run background services securely.

---

# What is a Group?

A **group** is a collection of users who share the same permissions on files and directories.

Instead of assigning permissions to each user individually, administrators can assign permissions to a group.

Example:

```text
Developers
│
├── Ali
├── Ahmed
└── Sara
```

All members inherit the group's permissions.

---

# Why Do We Use Groups?

Groups make permission management easier.

For example:

Instead of giving 20 users access to a shared project folder one by one, place all 20 users in the same group and assign permissions to the group.

---

# User ID (UID)

Every user has a unique **User ID (UID)**.

Examples:

| UID  | User                |
| ---- | ------------------- |
| 0    | root                |
| 1000 | First regular user  |
| 1001 | Second regular user |

Linux uses the UID internally to identify users.

---

# Group ID (GID)

Every group has a unique **Group ID (GID)**.

Example:

```text
Developers

Group ID : 1002
```

---

# Home Directory

Each regular user has a personal home directory.

Example:

```text
/home/kashif
```

This directory stores:

* Documents
* Downloads
* Pictures
* Desktop
* Configuration files

---

# Default Shell

Every user has a default shell.

Example:

```text
/ bin / bash
```

Common shells include:

* Bash
* Zsh
* Fish
* Sh

The shell starts automatically after the user logs in.

---

# Important User Files

## /etc/passwd

Stores basic information about every user.

Example:

```text
kashif:x:1000:1000:Kashif:/home/kashif:/bin/bash
```

Fields:

* Username
* Password placeholder
* UID
* GID
* Description
* Home Directory
* Default Shell

> Modern Linux systems do **not** store passwords in this file.

---

## /etc/shadow

Stores encrypted user passwords.

Example:

```text
root:$6$xxxxxxxxxxxxxxxx
```

Only privileged users (such as root) can access this file.

---

## /etc/group

Stores information about groups.

Example:

```text
developers:x:1001:kashif,ali,ahmed
```

---

# User Management Commands

## whoami

### Purpose

Displays the username of the currently logged-in user.

### Syntax

```bash
whoami
```

Example Output

```text
kashif
```

---

## id

### Purpose

Displays detailed information about the current user.

### Syntax

```bash
id
```

Example Output

```text
uid=1000(kashif)
gid=1000(kashif)
groups=1000(kashif),27(sudo)
```

Displays:

* UID
* GID
* Group Membership

📸 **Screenshot Placeholder**

*Insert a screenshot showing the output of `id`.*

---

## groups

### Purpose

Displays the groups a user belongs to.

### Syntax

```bash
groups
```

Example Output

```text
kashif sudo docker
```

---

## users

### Purpose

Displays users currently logged into the system.

### Syntax

```bash
users
```

---

## passwd

### Purpose

Changes a user's password.

### Syntax

```bash
passwd
```

Example

```bash
passwd
```

Linux asks for:

* Current password
* New password
* Password confirmation

---

# Administrative Commands

These commands usually require **root** or **sudo** privileges.

---

## useradd

### Purpose

Creates a new user.

### Syntax

```bash
sudo useradd username
```

Example

```bash
sudo useradd ali
```

---

## passwd username

Sets the password for the newly created user.

```bash
sudo passwd ali
```

---

## usermod

### Purpose

Modifies an existing user.

Example:

```bash
sudo usermod -aG sudo ali
```

The options mean:

* `-a` → Append
* `-G` → Secondary Group

Adds **ali** to the **sudo** group.

---

## userdel

### Purpose

Deletes a user account.

Example

```bash
sudo userdel ali
```

Delete the user and their home directory.

```bash
sudo userdel -r ali
```

---

# Group Management Commands

## groupadd

Creates a new group.

```bash
sudo groupadd developers
```

---

## groupdel

Deletes a group.

```bash
sudo groupdel developers
```

---

## groupmod

Renames a group.

```bash
sudo groupmod -n security developers
```

---

# sudo

## What is sudo?

`sudo` stands for **SuperUser DO**.

It allows a regular user to execute commands with administrator privileges.

Example:

```bash
sudo apt update
```

The system asks for your password before executing the command.

---

# Why Use sudo Instead of Logging in as Root?

Using `sudo` is safer because:

* Administrative actions are logged.
* Users receive elevated privileges only when needed.
* Reduces the risk of accidental system damage.
* Supports the principle of least privilege.

---

# User and Group Relationship

```text
                  Linux System
                        │
        ┌───────────────┴───────────────┐
        │                               │
     Users                           Groups
        │                               │
   ┌────┴────┐                    ┌─────┴─────┐
   │         │                    │           │
 Kashif     Ali              Developers     sudo
        │                          │
        └──────────────┬───────────┘
                       │
               Shared Permissions
```

---

# Blue Team Perspective

User accounts are one of the first things investigators examine after a security incident.

Common investigation tasks include:

* Identifying recently created accounts.
* Checking for unauthorized users in the `sudo` group.
* Reviewing login activity.
* Examining password changes.
* Looking for suspicious service accounts.

Attackers often create new user accounts or add existing accounts to privileged groups to maintain persistent access.

---

# Common Mistakes

* Logging in as the root user for daily work.
* Giving every user `sudo` privileges.
* Using weak passwords.
* Forgetting to remove unused accounts.
* Leaving default accounts enabled.

---

# Best Practices

* Use strong passwords.
* Follow the Principle of Least Privilege.
* Use `sudo` instead of logging in as root.
* Remove inactive user accounts.
* Regularly review group memberships.
* Monitor administrative actions.

---

# Chapter Summary

In this chapter, you learned:

* What users and groups are.
* The difference between root, regular, and system users.
* What UID and GID represent.
* The purpose of `/etc/passwd`, `/etc/shadow`, and `/etc/group`.
* How to manage users and groups.
* Why proper user management is important for Linux security.

---

# Interview Questions

1. What is a user in Linux?
2. What is the difference between the root user and a regular user?
3. What is a system user?
4. What is a group in Linux?
5. What is the purpose of UID and GID?
6. What information is stored in `/etc/passwd`?
7. Why is `/etc/shadow` protected?
8. What does the `id` command display?
9. What is the purpose of `sudo`?
10. Why should administrators follow the Principle of Least Privilege?

---

# References

* GNU Core Utilities Manual — https://www.gnu.org/software/coreutils/
* Linux man pages — https://man7.org/linux/man-pages/
* Ubuntu Documentation — https://help.ubuntu.com/

---
