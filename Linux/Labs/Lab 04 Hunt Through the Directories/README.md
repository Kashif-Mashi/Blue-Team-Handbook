# Lab 04 – Navigation Commands

## Scenario

An employee accidentally deleted an important incident report. Your Blue Team has recovered the server, but no one remembers where the report was stored.

As the assigned Security Analyst, your job is to navigate the Linux file system efficiently, locate important files, and verify their locations before the investigation continues.

---

# Mission

Master Linux navigation commands to quickly move through the file system and locate important files and directories.

---

# Story

The Incident Response team has recovered a compromised Linux server.

Before they begin analyzing logs, they need someone who can quickly navigate the system and locate critical files.

Your team leader says:

> *"A slow investigator misses evidence. Learn to move through Linux efficiently, and you'll always stay one step ahead of an attacker."*

Your mission is to explore the system and locate important resources using Linux navigation commands.

---

# Learning Objectives

After completing this lab, you will be able to:

* Navigate between directories confidently.
* Understand absolute and relative paths.
* Move to parent and home directories.
* Switch between previously visited directories.
* Locate files and directories.
* Verify your current working directory.

---

# Prerequisites

Before starting this lab, ensure you have completed:

* Lab 01 – Build Your Cyber Lab
* Lab 02 – Linux File System Exploration
* Lab 03 – Shell & Terminal Basics

---

# Clues

> **"Every file has an address—find the address, and you'll find the evidence."**

> **"The quickest path isn't always the shortest; sometimes it's the one you already know."**

> **"Knowing where you are is just as important as knowing where you're going."**

---

# Your Tasks

Complete the following tasks using Linux navigation commands.

### Task 1 – Verify Your Current Location

Determine your current working directory before performing any navigation.

---

### Task 2 – Explore Your Home Directory

Navigate to your home directory and identify the default folders created for your user account.

---

### Task 3 – Navigate the File System

Move between the following directories:

* Home directory
* Root directory
* `/etc`
* `/var`
* `/usr`
* `/tmp`

Observe how the directory structure changes as you move.

---

### Task 4 – Practice Relative and Absolute Paths

Navigate to the same destination using:

* Relative paths
* Absolute paths

Compare the two approaches.

---

### Task 5 – Return to Previous Directories

Move between recently visited directories without typing the full path each time.

---

### Task 6 – Locate Important Files

Find the location of:

* `passwd`
* `hosts`
* `shadow`
* `bash`

Record the full path for each file.

---

### Task 7 – Search for Directories

Locate directories commonly used during security investigations, including:

* Log directory
* User home directories
* Temporary directory

---

### Task 8 – Document Your Investigation

Create a report that includes:

* Directories visited
* Files located
* Navigation methods used
* Observations made during the investigation

---

# Success Criteria

You have successfully completed this lab if you can:

* Move confidently between directories.
* Explain the difference between absolute and relative paths.
* Navigate without relying on the graphical interface.
* Locate important Linux files.
* Record accurate file paths.

---

# Hint

Think about the following questions before looking for the solution:

* Which command displays your current directory?
* How do you move to another directory?
* How can you return to your previous location?
* Which command searches for files and directories?

If you need assistance, refer to **`Solutions/Lab-04-Solution.md`**.

---

# Blue Team Insight

During incident response, analysts often need to locate:

* Configuration files
* Authentication files
* Log files
* User directories
* Malware samples
* Backup files

Efficient navigation allows analysts to collect evidence quickly and reduce investigation time.

---

# Challenge

Without using a search engine:

1. Navigate from your home directory to `/etc` using an absolute path.
2. Return to your home directory using the shortest possible command.
3. Move back to the previous directory.
4. Locate the `shadow` file.
5. Find the directory where Linux stores system logs.
6. Identify your current working directory at every stage of the exercise.

---

# Reflection Questions

1. What is the difference between an absolute path and a relative path?
2. Why is efficient navigation important during a security investigation?
3. Which Linux directories are accessed most frequently by Blue Team analysts?
4. How can navigation mistakes impact an investigation?

---

# Key Takeaways

After completing this lab, you should be able to:

* Navigate the Linux file system efficiently.
* Understand absolute and relative paths.
* Locate important files and directories.
* Move confidently between different locations in the system.
* Apply navigation skills during security investigations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-04-Solution.md`**.

---

## Next Lab

Continue to **Lab 05 – File & Directory Management**, where you will learn how to create, organize, copy, move, rename, and remove files and directories safely using Linux commands.
