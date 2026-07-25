# Lab 01 – Build Your Cyber Lab

## Scenario

Every cybersecurity professional needs a reliable environment to learn, test, and investigate without affecting production systems. Before you can defend networks, analyze malware, or investigate incidents, you must build your own secure cyber lab.

Your first mission is to install and configure **Kali Linux** inside **Oracle VirtualBox**. This virtual machine will serve as your primary workstation throughout the Linux Labs and future Blue Team exercises.

---

# Mission

Become a Cyber Lab Engineer.

Prepare a stable and secure Kali Linux virtual machine that will be used in all upcoming labs.

---

# Story

You've just joined the Blue Team as a Junior Security Analyst.

On your first day, your team leader gives you a brand-new workstation and says:

> *"Every great defender starts with a properly configured lab. Build yours carefully—every investigation, every incident, and every challenge begins here."*

Your task is to prepare the investigation environment before your first security assignment arrives.

---

# Your Objectives

By the end of this lab, you will be able to:

* Install Oracle VirtualBox
* Download the latest Kali Linux ISO
* Create a new virtual machine
* Configure CPU, RAM, storage, and networking
* Install Kali Linux
* Update the operating system
* Install VirtualBox Guest Additions
* Create a VM snapshot for recovery

---

# Prerequisites

Before starting, ensure you have:

* Windows 10/11 Host Machine
* Oracle VirtualBox
* Kali Linux ISO (Latest Stable Release)
* Minimum 40 GB Free Disk Space
* At least 8 GB RAM on the host system
* Stable Internet Connection

---

# Clues

> "A weak foundation creates unstable systems."

> "Your laboratory should be isolated, but never disconnected from learning."

> "Always create a recovery point before making major changes."

---

# Your Tasks

Without following copy-and-paste commands blindly, complete the following objectives:

### Task 1 – Install Oracle VirtualBox

Download and install Oracle VirtualBox on your host machine.

Verify that VirtualBox launches successfully.

---

### Task 2 – Download Kali Linux

Visit the official Kali Linux website.

Download the latest **64-bit Installer ISO**.

Verify the file has downloaded successfully.

---

### Task 3 – Create the Virtual Machine

Create a new virtual machine using the downloaded ISO.

Configure:

* VM Name
* Operating System
* Memory Allocation
* CPU Allocation
* Virtual Hard Disk
* Boot Order

---

### Task 4 – Install Kali Linux

Complete the installation process.

Configure:

* Username
* Password
* Hostname
* Time Zone
* Keyboard Layout
* Disk Partitioning

---

### Task 5 – Configure Networking

Configure your virtual machine networking.

Recommended:

* Adapter 1 → NAT
* Adapter 2 → Host-Only Adapter (Optional)

Verify internet connectivity after installation.

---

### Task 6 – Update Kali Linux

Update the operating system to the latest packages.

Confirm there are no pending updates.

---

### Task 7 – Install Guest Additions

Improve usability by enabling:

* Full-screen mode
* Clipboard sharing
* Drag and Drop
* Better display resolution

---

### Task 8 – Create a Snapshot

Before continuing to future labs:

Create a VirtualBox snapshot named:

```text id="m7rfx3"
Fresh Kali Installation
```

This allows you to restore your environment if something breaks later.

---

# Success Criteria

Your mission is complete when:

* Kali Linux boots successfully.
* Internet connectivity is working.
* System packages are fully updated.
* Guest Additions are installed.
* Clipboard sharing works.
* Screen resolution adjusts correctly.
* A VM snapshot has been created.

---

# Blue Team Insight

Security analysts rarely work directly on their host operating system.

Virtual machines provide:

* Safe malware analysis environments
* Isolated testing platforms
* Easy recovery through snapshots
* Multiple operating systems on one computer
* Reproducible lab environments

A well-maintained virtual lab is an essential part of every SOC analyst's toolkit.

---

# Challenge

Without using a tutorial:

* Change the desktop wallpaper.
* Change the hostname.
* Create a new user account.
* Install one additional package of your choice.
* Reboot the system and verify everything still works.

---

# Reflection Questions

1. Why are virtual machines preferred over installing Kali directly on a host computer?
2. What is the difference between a NAT adapter and a Host-Only adapter?
3. Why should you create a snapshot before making significant system changes?
4. How can virtual machines improve cybersecurity learning and incident response practice?

---

# Key Takeaways

After completing this lab, you have:

* Built your first cybersecurity lab environment.
* Installed and configured Kali Linux.
* Prepared a reusable virtual machine for future exercises.
* Established a stable foundation for the remaining Linux Labs and Blue Team Handbook.

---

## Next Lab

**Lab 02 – Linux File System Exploration**

In the next lab, you will begin exploring the Linux directory structure and learn how files and folders are organized within the operating system.
