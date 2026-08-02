# Lab 02 – Linux File System Exploration

## Scenario

A security incident has been reported on a Linux server. Before you can investigate suspicious files or analyze system logs, you must understand how Linux organizes its files and directories.

As a Junior Blue Team Analyst, your first assignment is to explore the Linux file system and identify where important system files, user data, logs, and applications are stored.

---

# Mission

Become familiar with the Linux file system by exploring its directory structure and locating important system resources.

---

# Story

Your team leader hands you access to a Linux server and says:

> *"A good investigator never gets lost. Before you can hunt attackers, you must know where everything lives."*

Your mission is to explore the system, identify important directories, and understand their purpose.

---

# Learning Objectives

After completing this lab, you will be able to:

* Navigate the Linux file system.
* Identify common Linux directories.
* Understand the purpose of system folders.
* Locate user data and configuration files.
* Explore hidden files and directories.
* Use basic navigation commands confidently.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Kali Linux virtual machine.
* Completed **Lab 01 – Build Your Cyber Lab**.
* Basic familiarity with the terminal.

---

# Clues

> **"Everything has a place. Find the place, and you'll find the answer."**

> **"Hidden files often contain the most valuable secrets."**

> **"Not every directory belongs to the user—some belong to the operating system."**

---

# Your Tasks

Complete the following tasks without relying on a tutorial. Use the Linux commands you have learned in the **Linux Fundamentals** chapters.

### Task 1 – Determine Your Current Location

Find your current working directory.

---

### Task 2 – Explore the Root Directory

Navigate to the root (`/`) directory and list its contents.

Identify important directories such as:

* `/home`
* `/etc`
* `/var`
* `/usr`
* `/bin`
* `/tmp`
* `/opt`
* `/root`

---

### Task 3 – Investigate System Directories

Visit each of the following directories and determine its primary purpose:

* `/etc`
* `/var`
* `/home`
* `/usr`
* `/boot`
* `/dev`
* `/proc`

Record your observations.

---

### Task 4 – Find Hidden Files

Navigate to your home directory and display all hidden files and folders.

Identify at least three hidden files or directories.

---

### Task 5 – Locate Important Files

Use Linux search tools to locate:

* The Bash shell
* The hosts configuration file
* The passwd file
* The sudoers file

---

### Task 6 – Explore User Information

Navigate through your home directory.

Identify folders such as:

* Desktop
* Documents
* Downloads
* Pictures
* Music
* Videos

---

### Task 7 – Document Your Findings

Create a simple report listing:

* The directories you explored.
* Their purpose.
* Any interesting observations.

---

# Success Criteria

You have successfully completed this lab if you can:

* Navigate between directories without assistance.
* Explain the purpose of the major Linux directories.
* Locate important configuration files.
* Display hidden files.
* Search for files using Linux commands.
* Create a short report of your findings.

---

# Hint

If you get stuck, ask yourself:

* Which command displays your current directory?
* Which command changes directories?
* How do you list hidden files?
* Which command searches for files?

If you still need assistance, refer to the **Lab 02 Solution Guide**.

---

# Blue Team Insight

Understanding the Linux file system is essential for security analysts.

During an investigation, you may need to:

* Examine configuration files in `/etc`
* Analyze logs in `/var/log`
* Review user files in `/home`
* Inspect running process information in `/proc`
* Verify installed applications in `/usr`

Knowing where information is stored helps analysts investigate incidents more efficiently.

---

# Challenge

Without using a search engine:

1. Find the location of the `bash` executable.
2. Locate the `shadow` file.
3. Determine where system log files are stored.
4. Find one hidden configuration file in your home directory.
5. Identify which directory contains temporary files.

---

# Reflection Questions

1. Why is the Linux file system organized into separate directories?
2. Which directories are most important during a security investigation?
3. Why are hidden files commonly used for configuration?
4. How can understanding the Linux file system improve incident response?

---

# Key Takeaways

After completing this lab, you should be able to:

* Navigate the Linux file system confidently.
* Understand the purpose of common Linux directories.
* Locate important system and user files.
* Use Linux navigation and search commands effectively.
* Build a strong foundation for future Blue Team investigations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-02-Solution.md`**.

---

## Next Lab

Continue to **Lab 03 – Shell & Terminal Basics**, where you will learn how to interact with Linux more efficiently using the Bash shell and essential terminal features.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2002%20Solution%20%E2%80%93%20Linux%20File%20System%20Exploration.md)**
