# Lab 14 – Blue Team Linux Investigation Challenge

## Scenario

Congratulations! You have completed the Linux Fundamentals training and are now ready for your first independent investigation.

At **03:17 AM**, the Security Operations Center (SOC) receives multiple alerts from a critical Linux server. The monitoring system reports unusual login attempts, high CPU usage, unexpected network connections, and unauthorized modifications to sensitive files.

As the assigned Blue Team Analyst, you have been tasked with investigating the incident, securing the system, and documenting your findings.

Everything you've learned throughout the previous labs will be required to complete this mission.

---

# Mission

Conduct a complete Linux security investigation by identifying suspicious activity, collecting evidence, securing the system, and preparing an incident report.

---

# Story

The night shift at the SOC receives an emergency alert.

One of the organization's Linux servers may have been compromised.

Your incident response manager contacts you immediately.

> *"This is your first real investigation. Trust your training, follow the evidence, and remember—every action you take must preserve the integrity of the investigation. Find out what happened before the attacker disappears."*

The investigation begins now.

---

# Learning Objectives

After completing this lab, you will be able to:

* Apply Linux administration skills in a realistic investigation.
* Collect and preserve digital evidence.
* Analyze user accounts and permissions.
* Investigate running processes and services.
* Examine network activity.
* Analyze system logs.
* Verify system integrity.
* Apply security hardening techniques.
* Document findings in a professional incident report.

---

# Prerequisites

Before starting this challenge, ensure you have completed:

* Lab 01 – Build Your Cyber Lab
* Lab 02 – Linux File System Exploration
* Lab 03 – Shell & Terminal Basics
* Lab 04 – Navigation Commands
* Lab 05 – File & Directory Management
* Lab 06 – Users & Groups
* Lab 07 – File Permissions & Ownership
* Lab 08 – Processes & Services
* Lab 09 – Linux Networking
* Lab 10 – Logging & Monitoring
* Lab 11 – Package Management
* Lab 12 – Bash Scripting
* Lab 13 – Linux Security & Hardening

---

# Clues

> **"The attacker leaves traces—but only careful investigators notice them."**

> **"Every process, every log, and every connection tells part of the story."**

> **"Protect the evidence before making changes to the system."**

---

# Investigation Tasks

Complete the following tasks in the order that best supports your investigation.

### Task 1 – Establish the Investigation Environment

* Record the current system date and time.
* Identify the logged-in user.
* Verify the system hostname.
* Create an investigation workspace to store your notes and evidence.

---

### Task 2 – Investigate User Accounts

Review all local user accounts.

Identify:

* Administrative users
* Recently created users
* Unnecessary or suspicious accounts
* Group memberships

Record your findings.

---

### Task 3 – Examine File Permissions

Inspect sensitive files and directories.

Verify:

* Ownership
* Group ownership
* File permissions

Identify any files with overly permissive access.

---

### Task 4 – Investigate Running Processes

Review active processes.

Identify:

* High CPU usage
* High memory usage
* Unknown processes
* Background services

Document anything unusual.

---

### Task 5 – Examine Network Activity

Review:

* Network interfaces
* IP configuration
* Active network connections
* Listening ports
* Running network services

Determine whether any communication appears suspicious.

---

### Task 6 – Analyze System Logs

Review system logs for:

* Failed login attempts
* Successful logins
* SSH activity
* Sudo usage
* Service failures
* System errors

Build a timeline of significant events.

---

### Task 7 – Verify Software & System Security

Review:

* Installed software
* Available updates
* Running services
* Firewall status

Apply updates or security improvements where appropriate.

---

### Task 8 – Secure the System

Implement appropriate hardening measures.

Examples include:

* Correcting insecure permissions
* Removing unnecessary software
* Disabling unused services
* Updating packages
* Strengthening user access controls

Document every action performed.

---

### Task 9 – Create an Incident Report

Prepare a professional report that includes:

* Executive Summary
* Scope of Investigation
* Evidence Collected
* Timeline of Events
* Findings
* Actions Taken
* Recommendations
* Lessons Learned

---

# Success Criteria

You have successfully completed this challenge if you can:

* Conduct a structured Linux investigation.
* Collect and preserve evidence.
* Identify suspicious system activity.
* Analyze logs and network information.
* Improve the system's security posture.
* Produce a professional incident report.

---

# Hint

This challenge combines everything you learned throughout the Linux Fundamentals course.

Review your previous labs if you need a refresher on:

* File system navigation
* Users and groups
* File permissions
* Processes and services
* Networking
* Logging
* Package management
* Bash scripting
* System hardening

If you need additional guidance, refer to **`Solutions/Lab-14-Solution.md`**.

---

# Blue Team Insight

This challenge reflects the daily responsibilities of a Security Operations Center (SOC) analyst.

A real investigation often requires analysts to:

* Collect evidence without altering it.
* Review user activity.
* Analyze logs.
* Investigate running processes.
* Examine network connections.
* Secure compromised systems.
* Document findings for management and future investigations.

The ability to combine technical skills with structured investigative thinking is what distinguishes an effective Blue Team professional.

---

# Final Challenge

Without using a search engine:

* Build an investigation workspace.
* Audit users and permissions.
* Investigate running processes.
* Review active network connections.
* Analyze authentication logs.
* Verify installed software.
* Perform basic system hardening.
* Produce a complete incident report with recommendations.

---

# Reflection Questions

1. Which investigation step did you find most challenging, and why?
2. Why is preserving evidence important during incident response?
3. How did Linux logs help reconstruct the incident timeline?
4. Which Blue Team skill do you think requires the most practice?
5. If this were a real security incident, what would your next actions be after completing the investigation?

---

# Course Completion

🎉 **Congratulations!**

You have successfully completed all **14 Linux Labs** in the **Blue Team Handbook**.

You have gained practical experience in:

* Linux Fundamentals
* File System Navigation
* Shell & Terminal Usage
* File & Directory Management
* User & Group Administration
* File Permissions & Ownership
* Process & Service Management
* Linux Networking
* Logging & Monitoring
* Package Management
* Bash Scripting
* Linux Security & Hardening
* Blue Team Investigation Techniques

These skills provide a strong foundation for more advanced topics such as:

* Wazuh SIEM
* Security Onion
* Threat Hunting
* Incident Response
* Digital Forensics
* Malware Analysis
* Detection Engineering

---

## What's Next?

Continue your learning journey with the next section of the **Blue Team Handbook**:

➡️ **Windows Fundamentals**

In this section, learn the fundamentals of Microsoft Windows from a Blue Team perspective. Understand how Windows works, manage users and services, navigate the file system, analyze logs, and perform basic security hardening.

---

# Solution

➡ **[View Solution](../Solutions/Lab%2014%20Solution%20%E2%80%93%20Blue%20Team%20Linux%20Investigation%20Challenge.md)**
