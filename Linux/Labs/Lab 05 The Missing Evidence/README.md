# Lab 05 – File & Directory Management

## Scenario

The Security Operations Center (SOC) has received several files collected from a compromised Linux server. Before the investigation begins, the evidence must be properly organized, backed up, and protected to maintain its integrity.

As a Blue Team Analyst, your responsibility is to manage the investigation workspace efficiently and ensure that critical evidence is stored correctly.

---

# Mission

Learn how to create, organize, copy, move, rename, and remove files and directories while maintaining a structured investigation environment.

---

# Story

A ransomware attack has affected one of your organization's Linux servers. During the initial response, dozens of log files, reports, and suspicious documents have been recovered.

Your team leader says:

> *"An investigator who cannot organize evidence will lose the investigation. Every file has value, but only if you know where it belongs."*

Your mission is to build and organize a secure evidence repository for the investigation.

---

# Learning Objectives

After completing this lab, you will be able to:

* Create files and directories.
* Organize data using folders.
* Copy and move files safely.
* Rename files and directories.
* Delete unnecessary files and folders.
* View and inspect file contents.
* Understand best practices for evidence management.

---

# Prerequisites

Before starting this lab, ensure you have completed:

* Lab 01 – Build Your Cyber Lab
* Lab 02 – Linux File System Exploration
* Lab 03 – Shell & Terminal Basics
* Lab 04 – Navigation Commands

---

# Clues

> **"Every investigation begins with organized evidence."**

> **"Never destroy evidence until you're certain it is no longer needed."**

> **"A copied file is a backup. A moved file changes its location."**

---

# Your Tasks

Complete the following tasks using Linux file and directory management commands.

### Task 1 – Create an Investigation Workspace

Create a workspace for your investigation.

Inside the workspace, create separate directories for:

* Evidence
* Reports
* Backups
* Notes

---

### Task 2 – Create Investigation Files

Create several empty files that represent:

* Incident Report
* Evidence Log
* Malware Notes
* Network Findings

---

### Task 3 – Record Investigation Notes

Add information to each file describing its purpose.

Review the contents to verify that the information was saved correctly.

---

### Task 4 – Copy Critical Evidence

Create a backup copy of your evidence files.

Store the backups in a dedicated backup directory.

Verify that both the original and backup files exist.

---

### Task 5 – Move Investigation Files

Reorganize your workspace by moving files into their appropriate directories.

Ensure each file is stored in the correct location.

---

### Task 6 – Rename Files

Rename investigation files using clear and meaningful names.

Confirm that the new names accurately reflect their contents.

---

### Task 7 – Remove Unnecessary Files

Delete temporary or unnecessary files created during the investigation.

Remove any empty directories that are no longer required.

---

### Task 8 – Verify the Investigation Workspace

Inspect your directory structure.

Ensure:

* Files are correctly organized.
* Backup copies exist.
* No unnecessary files remain.

---

# Success Criteria

You have successfully completed this lab if you can:

* Create directories and files.
* Copy important files safely.
* Move files between directories.
* Rename files correctly.
* Delete unwanted files without affecting important evidence.
* Maintain an organized investigation workspace.

---

# Hint

Think carefully before performing each task.

Ask yourself:

* Which command creates a directory?
* Which command creates an empty file?
* How do you copy a file without removing the original?
* Which command moves or renames a file?
* How can you safely delete files or empty directories?
* Which command displays the contents of a text file?

If you need assistance, refer to **`Solutions/Lab-05-Solution.md`**.

---

# Blue Team Insight

Proper file management is essential during incident response.

Blue Team analysts regularly:

* Organize forensic evidence.
* Create backup copies before analysis.
* Preserve original files for forensic integrity.
* Maintain investigation notes.
* Remove temporary working files after investigations.

Poor file management can result in lost evidence, inaccurate findings, or compromised investigations.

---

# Challenge

Without using a search engine:

1. Create a directory named **Incident-2026**.
2. Create three investigation files inside it.
3. Make a complete backup of the directory.
4. Rename one of the evidence files.
5. Move the renamed file into a **Reports** directory.
6. Delete an empty directory without affecting any investigation files.

---

# Reflection Questions

1. What is the difference between copying and moving a file?
2. Why should investigators create backups before editing evidence?
3. When should files be deleted during an investigation?
4. How does proper file organization improve incident response?

---

# Key Takeaways

After completing this lab, you should be able to:

* Manage files and directories confidently.
* Organize investigation data efficiently.
* Create backups before making changes.
* Maintain a structured workspace for incident response.
* Apply Linux file management skills in real-world Blue Team investigations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-05-Solution.md`**.

---

## Next Lab

Continue to **Lab 06 – Users & Groups**, where you will learn how to create users, manage groups, and control access to Linux systems using account management tools.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2005%20Solution%20%E2%80%93%20File%20%26%20Directory%20Management.md)**
