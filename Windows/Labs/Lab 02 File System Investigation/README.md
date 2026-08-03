# Lab 02 — File System Investigation

## Scenario

A user in the marketing department reports that their computer has been acting strangely after clicking a link in a suspicious email. They mentioned downloading an "invoice," but the file disappeared shortly after.

As a Junior SOC Analyst, your first assignment is to investigate the local Windows file system. Before you can properly hunt for advanced malware, you must understand how Windows organizes data, where payloads are typically staged, and how to uncover hidden files left behind by attackers.

---

# Mission

Explore the Windows file system, identify critical OS directories, expose hidden files and extensions, and uncover where the suspicious payload might be hiding using both File Explorer and Command Prompt.

---

# Story

Your Shift Lead assigns you the ticket and says:

> *"Attackers love to hide in plain sight. They rely on default Windows settings to conceal their tools. Your job is to strip away those defaults, expose the file system, and find out exactly what this user downloaded."*

Your mission is to explore the system, understand directory structures, and configure the OS to reveal its hidden secrets.

---

# Learning Objectives

After completing this lab, you will be able to:

* Navigate the Windows file system using File Explorer and CMD.
* Identify the purpose of critical Windows directories.
* Configure Windows to display hidden files and file extensions.
* Examine file metadata (Timestamps, Ownership).
* Understand and investigate Alternate Data Streams (ADS).
* Apply basic Blue Team file investigation techniques.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 virtual machine.
* Completed **Lab 01 – Windows Installation**.
* Basic familiarity with the Windows desktop.

---

# Clues

> **"Malware often pretends to be a normal document. If you can't see the extension, you can't trust the file."**

> **"Attackers hide their tools where normal users never look: `AppData`, `ProgramData`, and Alternate Data Streams."**

---

# Your Tasks

Complete the following tasks to investigate the file system.

### Task 1 — Map the Terrain
Open **File Explorer** and select **This PC**. Identify all available drives on your system. Record the drive letters and their primary file systems (e.g., NTFS).

---

### Task 2 — Inspect Critical OS Directories
Navigate to the root of your primary drive (usually `C:\`). Visit the following directories and determine their primary purpose:
* `C:\Windows`
* `C:\Users`
* `C:\Program Files`
* `C:\ProgramData` (Note: You may not see this one yet!)

---

### Task 3 — Expose the Unseen
Attackers rely on hidden files. Configure File Explorer to display **Hidden Items**.
*(Hint: Look under the View tab)*
Once enabled, navigate back to the `C:\` drive. What new directories can you see?

---

### Task 4 — Unmask the Extensions
The user claimed they downloaded an "invoice". Configure File Explorer to **Show File Name Extensions**.
Why is this critical for a SOC analyst when investigating a file named `invoice.pdf.exe`?

---

### Task 5 — Extract the Metadata
Create a text file on your Desktop named `Evidence.txt`. Right-click it and view its **Properties**.
Record the Created, Modified, and Accessed timestamps. How could an attacker manipulate these?

---

### Task 6 — Command Line Reconnaissance
Open **Command Prompt**. Use the `tree` command to visualize the hierarchical structure of your user profile (`C:\Users\<YourName>`).
Use the `echo %USERPROFILE%` command to confirm your exact location.

---

### Task 7 — Investigate File Attributes
In Command Prompt, navigate to your Desktop and run the `attrib` command.
Identify any files with the `H` (Hidden) or `S` (System) attributes.

---

### Task 8 — Uncover Alternate Data Streams (ADS)
Attackers sometimes hide malicious code *inside* legitimate files using ADS.
1. In CMD, create a normal file: `echo "Clean Data" > safe.txt`
2. Hide a payload inside it: `echo "Malicious Payload" > safe.txt:hidden.txt`
3. Use the `dir /r` command to reveal the hidden stream.

---

# Success Criteria

You have successfully completed this lab if you can:

* Explain the purpose of `C:\Windows`, `C:\Users`, and `C:\ProgramData`.
* Instantly recognize executable files masquerading as documents.
* Expose hidden files and metadata using File Explorer properties.
* Navigate and inspect file attributes via Command Prompt.
* Demonstrate how Alternate Data Streams can conceal data.

---

# 💙 Blue Team Insight

Understanding the Windows file system is the foundation of digital forensics.
During an incident, analysts immediately check specific directories:
* `C:\Users\<User>\AppData\Local\Temp` (Common malware staging)
* `C:\ProgramData` (Hidden persistence mechanisms)
* `C:\Windows\System32` (Legitimate binaries hijacked by attackers)
If you don't know what *normal* looks like, you will never spot the *abnormal*.

---

# Key Takeaways

After completing this lab, you should be able to:

* Configure Windows for forensic visibility (show extensions, show hidden files).
* Understand the hierarchical nature of Windows storage.
* Differentiate between standard file data and metadata/ADS.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2002-File%20System%20Investigation.md)**
