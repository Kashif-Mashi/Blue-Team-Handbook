# Lab 04 — File Permissions & Access Control

## Scenario

A severe data exposure incident occurred overnight at a financial organization. Highly sensitive HR payroll documents stored in `C:\Confidential` were accessed and leaked by an unauthorized employee. 

As a Systems Auditor and Incident Responder, your job is to investigate the current NTFS Access Control Lists (ACLs) on the breached folder, determine how the unauthorized access occurred due to inherited permission misconfigurations, and re-secure the directory.

---

# Mission

Use command-line utilities (`icacls` and `takeown`) and PowerShell (`Get-Acl`, `Set-Acl`) to inspect NTFS permissions, identify security flaws, break inheritance on the sensitive directory, and enforce strict, explicit access controls.

---

# Story

The CISO calls you into an emergency meeting and explains:

> *"Someone without clearance got into the `C:\Confidential` drive and leaked the Payroll records. We think the folder was misconfigured when it was created and inherited default permissions that gave the `Users` group access. Find the flaw, prove it, and lock that folder down immediately before anything else is stolen."*

Your mission is to recreate the breach conditions, identify the flawed ACLs, and implement a hardened NTFS baseline.

---

# Learning Objectives

After completing this lab, you will be able to:

* Inspect NTFS permissions using `icacls` and `Get-Acl`.
* Differentiate between explicit permissions and inherited permissions.
* Modify Discretionary Access Control Lists (DACLs) via the command line.
* Enforce folder access restrictions and block permission inheritance.
* Audit and transfer file ownership using `takeown` and PowerShell.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 03 (File System) and Chapter 07 (NTFS Permissions).

---

# Clues

> **"Folders created at the root of `C:\` inherit default permissions, often granting the `Users` group read and execute rights. Attackers look for this specific oversight."**

> **"When locking down a folder, you must disable inheritance FIRST, otherwise parent permissions will keep flowing down and overriding your restrictions."**

---

# Your Tasks

Complete the following tasks to investigate and remediate the NTFS access controls.

### Task 1 — Recreate the Incident Environment
To investigate, you must recreate the scene.
Open Command Prompt as Administrator. Create the sensitive directory `C:\Confidential` and a test file `C:\Confidential\Payroll.txt`.

---

### Task 2 — Inspect Initial Vulnerabilities
Run `icacls C:\Confidential\Payroll.txt`. 
Analyze the output. Are permissions inherited `(I)` from the parent folder? Does the standard `Users` group have Read/Execute `(RX)` access?

---

### Task 3 — The PowerShell Perspective
Use PowerShell to get a detailed view of the access rules.
Run `Get-Acl C:\Confidential\Payroll.txt | Format-List`. Note who the current Owner of the file is.

---

### Task 4 — Simulate the Insider Threat
Create a standard local user account named `SuspectUser` with a secure password using the `net user` command.

---

### Task 5 — Prove Unauthorized Access
Without changing any permissions yourself, use the `runas` command or switch users to attempt to read `C:\Confidential\Payroll.txt` as `SuspectUser`. 
Does the user have access? (Yes, due to the inherited `Users` group permission discovered in Task 2).

---

### Task 6 — Stop the Bleeding (Disable Inheritance)
It's time to lock down the folder. You must break the permission inheritance chain.
Use `icacls C:\Confidential /inheritance:d` to convert the inherited permissions into explicit permissions so you can safely modify them.

---

### Task 7 — Evict the Unauthorized
Now that inheritance is disabled, strip access rights from the local `Users` group entirely.
Use `icacls C:\Confidential /remove Users`.

---

### Task 8 — Enforce Strict Access Controls
Grant the `Administrators` group Full Control `(F)` over `C:\Confidential` recursively. Ensure you use the proper flags `(OI)(CI)` so the permissions propagate to all files and subfolders inside.
`icacls C:\Confidential /grant Administrators:(OI)(CI)F /T`

---

### Task 9 — Reclaim File Ownership
During an incident, malware or rogue admins may change file ownership to lock out responders. You must prove you can take it back.
Use `takeown /F C:\Confidential\Payroll.txt /A` to transfer file ownership to the local Administrators group.

---

### Task 10 — Verify the Remediation
Verify your work. Run `icacls C:\Confidential`. 
The `Users` group should be completely missing from the DACL, and inheritance should be marked as disabled.

---

### Task 11 — Clean up the Environment
Delete the `C:\Confidential` directory and remove the `SuspectUser` account using `net user SuspectUser /delete`.

---

# Success Criteria

You have successfully completed this lab if you can:

* Read and interpret `icacls` permission outputs, identifying inherited `(I)` vs explicit permissions.
* Successfully disable NTFS inheritance on a directory.
* Apply exact `icacls` grants using Object Inherit `(OI)` and Container Inherit `(CI)` flags.
* Reclaim ownership of a locked file using `takeown`.

---

# 💙 Blue Team Insight

Privilege Escalation via Weak ACLs is a primary tactic for attackers. They hunt for weak directory permissions on system services (e.g., write access to service executables or unquoted service paths). If they can overwrite a binary that runs as `SYSTEM`, they gain complete control of the host.
Always remember: Folders created manually under `C:\` inherit `Users:(RX)` rights by default. Sensitive data MUST have inheritance disabled and explicit DACLs applied immediately upon creation.

---

# Key Takeaways

After completing this lab, you should be able to:

* Identify security flaws caused by default NTFS inheritance.
* Manipulate Discretionary Access Control Lists via CLI.
* Apply strict Access Control baselines during Incident Response.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2004%20Solution.md)**
