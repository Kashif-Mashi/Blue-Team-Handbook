# Lab 05 — Windows Users & Groups Management

## Scenario

A company's Internal Security Audit flagged anomalous administrative activity on workstation `DESKTOP-TRIAGE` over the weekend. The SOC suspects an insider threat—or a remote attacker who gained access—has created a backdoor account to maintain persistence. 

As a Tier 1 SOC Analyst, your supervisor has instructed you to perform a rapid identity audit. You must examine the local user database, hunt down the rogue account, audit group memberships to see if the attacker elevated privileges, and review the host's security policies to prevent brute-force attacks in the future.

---

# Mission

Use CMD and PowerShell to audit local user accounts, identify built-in vs. custom identities via Security Identifiers (SIDs), expose unauthorized administrative privilege escalation, and harden the system's account lockout policy.

---

# Story

Your Lead Analyst messages you:

> *"Attackers don't always use malware. Sometimes they just create a new admin account named `BackupAdmin` or `Helpdesk` and walk right through the front door. I need you to pull every user on that box, check their group memberships, and find out if someone planted a backdoor."*

Your mission is to find the rogue account, figure out if they made themselves a local administrator, and lock down the host's password policies.

---

# Learning Objectives

After completing this lab, you will be able to:

* Create, audit, and manage local user accounts using CMD and PowerShell.
* Inspect user Security Identifiers (SIDs) to differentiate built-in accounts from standard users.
* Audit local security groups and manage group memberships.
* Configure and test local account lockout and password policies.
* Track critical security events (Event ID 4720: User Creation) within Windows Event Viewer.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 06 (Windows Users & Groups).

---

# Clues

> **"Adversaries try to blend in. A backdoor account might be named `SysUpdater` or `TempContractor`. Check the creation dates and SIDs."**

> **"Creating an account is only step one. Check the `Administrators` group—if the rogue account is in there, the system is fully compromised."**

---

# Your Tasks

Complete the following tasks to conduct the identity audit.

### Task 1 — Simulate the Compromise
Before you hunt, you must plant the backdoor. Open Command Prompt as Administrator and simulate the attacker by creating a hidden backdoor account:
`net user TempContractor ComplexP@ss2026! /add`

Next, simulate the attacker elevating privileges by adding the account to the local Administrators group:
`net localgroup Administrators TempContractor /add`

---

### Task 2 — Audit Local Accounts (CMD)
Assume your investigation begins now. List all local user accounts on the host using the simplest CMD tool available: `net user`.
Do you see the `TempContractor` account?

---

### Task 3 — Audit Account Details (PowerShell)
CMD is basic. Let's get more detail using PowerShell.
Use `Get-LocalUser | Select-Object Name, Enabled, LastLogon, Description` to inspect the status of every user on the system.

---

### Task 4 — Inspect SIDs and RIDs
Attackers can rename accounts, but they cannot change SIDs.
Run `wmic useraccount get name,sid` to extract SIDs for all local accounts. Identify the SID ending in `-500` (The built-in Administrator account). Compare it to the SID of your rogue `TempContractor` account.

---

### Task 5 — Audit Administrative Privilege Escalation
You need to know if the rogue account has elevated privileges.
Run `net localgroup Administrators` or `Get-LocalGroupMember -Group "Administrators"`.
Is the `TempContractor` account listed? If so, the attacker has full SYSTEM control.

---

### Task 6 — Track the Origin (Event Logs)
Open **Event Viewer** (`eventvwr.msc`). Navigate to `Windows Logs -> Security`.
Filter the log for **Event ID 4720** (A user account was created). 
Can you find the exact time the `TempContractor` account was created, and which user account created it?

---

### Task 7 — Review Password Policies
You notice the host might be vulnerable to brute force attacks.
Run `net accounts` to view the current lockout threshold, duration, and password requirements.

---

### Task 8 — Harden the System
The current lockout policy is weak. Let's harden it.
1. Set the account lockout threshold to 5 failed attempts: `net accounts /lockoutthreshold:5`
2. Set the lockout duration to 30 minutes: `net accounts /lockoutduration:30`

Verify your changes by running `net accounts` again.

---

### Task 9 — Remediate the Threat
The investigation is complete. It's time to eradicate the backdoor.
Remove the user `TempContractor` from the system entirely.
`net user TempContractor /delete`

---

# Success Criteria

You have successfully completed this lab if you can:

* Enumerate all users and groups on a Windows host using CLI.
* Identify the RID 500 built-in Administrator account by its SID.
* Prove a user has administrative privileges by auditing the local Administrators group.
* Harden a Windows machine against brute force attacks by configuring the `net accounts` lockout policy.
* Find evidence of account creation in the Security Event Log.

---

# 💙 Blue Team Insight

Adding backdoor accounts is a classic persistence technique. Monitoring **Event ID 4720 (User Created)** and **Event ID 4732 (Member Added to Local Group)** allows the SOC to detect unexpected account creation instantly. If an alert fires for Event ID 4732 involving the `Administrators` or `Remote Desktop Users` group, incident responders must immediately investigate who initiated the change.

---

# Key Takeaways

After completing this lab, you should be able to:

* Manage Windows identities and group memberships programmatically.
* Understand the forensic value of SIDs over Usernames.
* Configure base-level security guardrails (Account Lockout Policies) using native OS tools.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2005%20Solution.md)**
