# Chapter 3 – Linux File System Hierarchy (FHS)

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand the Linux File System Hierarchy (FHS).
* Navigate important Linux directories.
* Identify where configuration files, logs, applications, and user data are stored.
* Explain why the file system structure is important for system administration and cybersecurity.

---

# What is the Linux File System?

A file system is the method an operating system uses to organize, store, and retrieve files on storage devices.

Unlike Windows, which uses drive letters such as **C:\**, **D:\**, and **E:\**, Linux organizes everything under a single directory tree.

Everything starts from one directory called the **Root Directory**.

---

# The Root Directory (/)

The root directory is represented by a single forward slash:

```text
/
```

It is the highest directory in Linux. Every file and directory exists somewhere beneath it.

> **Note:** The root directory (`/`) is different from the **root user**. The root directory is the top-level folder, while the root user is the administrator account.

---

# Linux File System Hierarchy

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root

├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

# Important Directories

## /bin

Contains essential command-line programs required for normal system operation.

Examples:

* ls
* cp
* mv
* cat
* pwd

---

## /boot

Contains files required to start (boot) the operating system.

Examples:

* Linux Kernel
* GRUB Bootloader
* Boot Configuration Files

---

## /dev

Stores device files.

Linux treats hardware devices as files.

Examples:

* Hard drives
* USB devices
* Keyboard
* Mouse
* Terminal devices

---

## /etc

Contains system-wide configuration files.

Examples:

* User configuration
* Network settings
* SSH configuration
* DNS configuration
* Service configuration

Examples of important files:

* `/etc/passwd`
* `/etc/shadow`
* `/etc/hosts`
* `/etc/hostname`

---

## /home

Contains personal directories for regular users.

Example:

```text
/home/alice
/home/bob
```

Each user stores documents, downloads, and personal files here.

---

## /lib

Contains shared libraries required by programs.

Libraries are reusable pieces of code that applications depend on.

---

## /media

Automatically mounts removable storage devices.

Examples:

* USB Drives
* External Hard Drives
* DVDs

---

## /mnt

Used for manually mounting storage devices or network shares.

System administrators commonly use this directory for temporary mounts.

---

## /opt

Contains optional third-party software.

Examples:

* Commercial applications
* Security tools
* Custom software

---

## /proc

A virtual file system that provides information about the running system.

It contains information about:

* CPU
* Memory
* Running Processes
* Kernel Parameters

The files are generated dynamically and do not exist permanently on disk.

---

## /root

The home directory of the **root (administrator)** user.

Do not confuse it with the root directory (`/`).

---

## /run

Stores temporary runtime information.

Examples:

* Process IDs (PID files)
* Service status
* Runtime sockets

The contents are cleared after reboot.

---

## /sbin

Contains essential system administration commands.

Examples:

* reboot
* shutdown
* fsck
* ip

These commands are typically used by system administrators.

---

## /srv

Stores data used by network services.

Examples:

* FTP
* HTTP
* Web Applications

---

## /sys

Provides information about hardware and kernel devices.

Like `/proc`, it is a virtual file system.

---

## /tmp

Stores temporary files.

Applications create temporary files here during execution.

Most systems automatically delete its contents after reboot.

---

## /usr

Contains user applications, documentation, and libraries.

Subdirectories include:

* `/usr/bin`
* `/usr/lib`
* `/usr/share`

Most installed software resides here.

---

## /var

Stores files that change frequently.

Examples:

* System logs
* Mail
* Databases
* Print queues
* Cache

One of the most important directories for system administrators and SOC analysts.

---

# Blue Team Perspective

Several directories are especially valuable during investigations.

| Directory | Why It Matters                    |
| --------- | --------------------------------- |
| /var/log  | System and application logs       |
| /etc      | Configuration changes             |
| /home     | User files and potential malware  |
| /tmp      | Temporary files used by malware   |
| /proc     | Running process information       |
| /root     | Administrator activity            |
| /var/www  | Web server content (if installed) |

Attackers often leave evidence in these locations, making them essential during incident response and forensic analysis.

---

# Practical Lab

### Objective

Explore the Linux file system.

### Commands

```bash
pwd
ls /
ls /home
ls /etc
ls /var
ls /tmp
cd /
cd /home
cd /etc
```

### Exercise

1. List the contents of the root directory.
2. Find your user directory inside `/home`.
3. Explore the `/etc` directory.
4. Locate the `/var/log` directory.
5. Return to your home directory.

---

# Key Takeaways

* Linux uses a single directory tree that begins with the root directory (`/`).
* Every file and folder exists beneath the root directory.
* Configuration files are mainly stored in `/etc`.
* User files are stored in `/home`.
* System logs are commonly stored in `/var/log`.
* Temporary files are stored in `/tmp`.
* Understanding the file system hierarchy is essential for Linux administration and cybersecurity.

---

# Interview Questions

1. What is the Linux File System Hierarchy (FHS)?
2. What is the purpose of the root directory (`/`)?
3. What is stored in `/etc`?
4. What is the difference between `/home` and `/root`?
5. Why is `/var/log` important for SOC analysts?
6. What is the purpose of the `/proc` directory?
7. Where are temporary files stored in Linux?
8. What types of files are stored in `/boot`?

---



---

# Next Chapter

➡ **[Chapter-04-Shell-and-Terminal-Basics](./Chapter-04-Shell-and-Terminal-Basics.md)**
