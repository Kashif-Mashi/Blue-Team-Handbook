# Lab 07 – File Permissions & Ownership

## Scenario

During an ongoing security investigation, sensitive evidence has been collected from a compromised Linux server. The evidence contains confidential information that must be protected from unauthorized access.

As the Linux Security Administrator, your responsibility is to configure file permissions and ownership so that only authorized investigators can access the evidence.

---

# Mission

Learn how to manage Linux file permissions and ownership to protect sensitive data and enforce the Principle of Least Privilege.

---

# Story

The Digital Forensics team has finished collecting evidence from a compromised server and hands it over to you.

Your team leader says:

> *"Evidence is only valuable if its integrity is preserved. One incorrect permission can expose confidential information or destroy an investigation. Secure the evidence before anyone else accesses it."*

Your mission is to secure the investigation files using proper Linux permissions and ownership.

---

# Learning Objectives

After completing this lab, you will be able to:

* Understand Linux permission types.
* View file permissions.
* Modify file permissions.
* Change file ownership.
* Change group ownership.
* Verify permission changes.
* Apply the Principle of Least Privilege.

---

# Prerequisites

Before starting this lab, ensure you have completed:

* Lab 01 – Build Your Cyber Lab
* Lab 02 – Linux File System Exploration
* Lab 03 – Shell & Terminal Basics
* Lab 04 – Navigation Commands
* Lab 05 – File & Directory Management
* Lab 06 – Users & Groups

---

# Clues

> **"Not everyone should have access to the evidence."**

> **"Ownership determines responsibility."**

> **"Grant only the permissions required—nothing more."**

---

# Your Tasks

Complete the following tasks using Linux permission and ownership management commands.

### Task 1 – Inspect Existing Permissions

Choose several files from your investigation workspace.

Record:

* File owner
* Group owner
* Current permissions

---

### Task 2 – Secure Investigation Files

Modify the permissions so that:

* The owner has full access.
* Team members have limited access.
* Unauthorized users cannot access the files.

Verify the changes.

---

### Task 3 – Protect Sensitive Directories

Apply appropriate permissions to the investigation directories.

Ensure unauthorized users cannot browse or modify the contents.

---

### Task 4 – Change File Ownership

Transfer ownership of one investigation file to another authorized analyst.

Verify that the ownership change was successful.

---

### Task 5 – Update Group Ownership

Assign the investigation files to your security team group.

Confirm that the correct group now owns the files.

---

### Task 6 – Test Access

Switch to another user account.

Verify which files can be accessed and which are restricted.

Return to your administrator account after testing.

---

### Task 7 – Review Effective Permissions

Inspect the final permissions of all investigation files.

Confirm they meet your organization's security requirements.

---

### Task 8 – Document Your Findings

Create a report containing:

* Original permissions
* Updated permissions
* Ownership changes
* Security improvements

---

# Success Criteria

You have successfully completed this lab if you can:

* View Linux file permissions.
* Modify permissions correctly.
* Change file ownership.
* Change group ownership.
* Verify access restrictions.
* Explain why each permission was applied.

---

# Hint

Consider the following questions:

* Which command displays file permissions?
* How can permissions be modified?
* Which command changes file ownership?
* How do you change a file's group?
* How can you verify your changes?

If you need additional guidance, refer to **`Solutions/Lab-07-Solution.md`**.

---

# Blue Team Insight

File permissions are one of the most important security controls in Linux.

Blue Team analysts regularly:

* Protect sensitive investigation data.
* Restrict unauthorized access.
* Secure configuration files.
* Prevent accidental modification of evidence.
* Audit file ownership during incident response.

Incorrect permissions can expose confidential information, allow privilege escalation, or compromise the integrity of forensic evidence.

---

# Challenge

Without using a search engine:

1. Secure an evidence file so that only its owner can modify it.
2. Allow members of the security team to read—but not modify—the file.
3. Prevent all other users from accessing the file.
4. Transfer ownership of one file to another analyst.
5. Change the file's group ownership to your security team.
6. Verify the final permissions and ownership.

---

# Reflection Questions

1. Why is the Principle of Least Privilege important?
2. What is the difference between file ownership and file permissions?
3. How can incorrect permissions affect a security investigation?
4. Why should Blue Team analysts regularly audit file permissions?

---

# Key Takeaways

After completing this lab, you should be able to:

* Understand Linux file permissions.
* Manage file and group ownership.
* Protect sensitive investigation data.
* Verify access controls.
* Apply Linux permission management in real-world Blue Team environments.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-07-Solution.md`**.

---

## Next Lab

Continue to **Lab 08 – Processes & Services**, where you will learn how to monitor running processes, manage system services, and identify suspicious activity on a Linux system.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2007%20Solution%20%E2%80%93%20File%20Permissions%20%26%20Ownership.md)**
