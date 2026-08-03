# Lab 03 — CMD & PowerShell Investigation

## Scenario

A high-priority alert has been triggered for workstation `DESKTOP-TRIAGE`. An unverified command-line process was launched by an endpoint user. Shortly after, the user reported that their graphical user interface (GUI) locked up and became completely unresponsive, a common precursor to a ransomware attack.

As a SOC Analyst, you cannot rely on File Explorer or Task Manager. You only have a remote Command Line Interface (CLI) session. Your job is to perform rapid host triage, discover active malicious connections, and locate the rogue processes before the ransomware begins encrypting the disk.

---

# Mission

Utilize native Windows CMD and PowerShell commands to enumerate the system, inspect active processes, trace network connections, and collect volatile diagnostic data for your triage report.

---

# Story

Your Incident Response Manager opens a remote shell for you and says:

> *"We're flying blind here. The GUI is gone. If this is ransomware staging, we only have minutes. Use the terminal to find out what processes are running, what they are talking to on the network, and dump the host details into a triage file immediately."*

Your mission is to execute a rapid triage using only `cmd.exe` and `powershell.exe`.

---

# Learning Objectives

After completing this lab, you will be able to:

* Perform system enumeration using native CMD and PowerShell utilities.
* Analyze running processes and identify active network connections.
* Collect volatile diagnostic data using CLI redirection and piping (`>`, `>>`, `|`).
* Query Windows event logs for suspicious command execution indicators.
* Write a basic PowerShell automation script for rapid host triage.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 04 (CMD) and Chapter 05 (PowerShell Fundamentals).

---

# Clues

> **"A process doesn't act alone; if it's staging malware, it's talking to a Command and Control (C2) server. Look for `ESTABLISHED` connections."**

> **"Piping output allows you to filter the noise. Combine commands to extract exactly what you need."**

---

# Your Tasks

Complete the following tasks to triage the host using only CLI tools.

### Task 1 — Initialize and Verify Context
Open Command Prompt as Administrator. Before taking any action, verify your exact security privileges and identity by running `whoami /all`. 
Record your account SID and any `Se*` privileges assigned to you.

---

### Task 2 — Snapshot the Host (CMD)
You need to record the exact state of the system hardware and OS.
Run `systeminfo` and redirect (`>`) the detailed system output to `C:\Users\Public\HostInfo.txt`.

---

### Task 3 — Uncover Active Processes (CMD)
The malware is hiding in a running process.
Use `tasklist /svc` to view all running processes along with their associated background services. Can you spot anything unusual?

---

### Task 4 — Trace Network Callbacks (CMD)
Malware must communicate. Execute `netstat -ano`.
The output is too noisy! Pipe (`|`) the output into `findstr` to display **only** network connections with the state `ESTABLISHED`.
Note the Process ID (PID) of any external connections.

---

### Task 5 — Identify Network Interfaces
You need the local IP address for the incident report.
Use `ipconfig /all` to record the IPv4 address, subnet mask, default gateway, and DNS servers of your active adapter.

---

### Task 6 — Transition to PowerShell
The CMD tools are limited. Launch an elevated PowerShell session by typing `powershell.exe` in your terminal.
Verify your execution policy using `Get-ExecutionPolicy -List`.

---

### Task 7 — PowerShell Process Hunting
Use PowerShell pipeline filtering to find resource-heavy processes.
Run `Get-Process | Where-Object { $_.WorkingSet -gt 50MB }`.
Identify the top three memory-consuming processes.

---

### Task 8 — Extract Custom Process Attributes
Export the `ProcessName`, `Id`, and `Path` of all active processes to a CSV file at `C:\Users\Public\ProcessReport.csv` using the `Select-Object` and `Export-Csv` cmdlets.

---

### Task 9 — Query Event Logs
You need to know what launched recently.
Use `Get-WinEvent` to query the `Security` log for recent process creation events (Event ID 4688) or look for errors in the `System` log.

---

### Task 10 — Automate the Triage
Instead of running these commands manually next time, write a basic `.ps1` script (or a PowerShell one-liner) that collects the host computer name, logged-in user, and active `ESTABLISHED` network connections, appending all of it into `C:\Users\Public\Triage.txt`.

---

# Success Criteria

You have successfully completed this lab if you can:

* Navigate and execute triage commands in a GUI-less environment.
* Successfully redirect CMD output to text files.
* Filter network states using `findstr` or `Where-Object`.
* Transition seamlessly from CMD to PowerShell.
* Programmatically extract specific object properties using PowerShell pipelines.

---

# 💙 Blue Team Insight

Command Line Auditing is a core component of SOC monitoring. Adversaries frequently execute host discovery commands (`systeminfo`, `whoami`, `netstat`) within seconds of gaining initial access. 
By matching `netstat -ano` PIDs to `tasklist` processes, analysts can trace unauthorized network callbacks directly back to the specific malicious binaries executing on disk.

---

# Key Takeaways

After completing this lab, you should be able to:

* Confidently perform host reconnaissance via CLI.
* Manage output redirection to preserve volatile data.
* Utilize the object-oriented power of PowerShell to filter, sort, and export investigation data.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2003%20Solution.md)**
