# Lab 06 – Users & Groups

## Scenario

A new Security Operations Center (SOC) has been established, and several analysts have joined the team. To protect sensitive investigation data, each analyst requires an individual account while sharing access to a common investigation group.

As the Linux System Administrator, your responsibility is to create user accounts, organize them into groups, and verify that the correct users have the appropriate level of access.

---

# Mission

Learn how to create, manage, and secure Linux user accounts and groups by configuring a team environment for your Blue Team.

---

# Story

The SOC is expanding, and your manager assigns you a new task.

> *"Our analysts need their own accounts, but they must collaborate securely. Build the team, assign the right members, and ensure everyone has the correct access before the next investigation begins."*

Your mission is to configure the user accounts and groups required for the Security Operations Center.

---

# Learning Objectives

After completing this lab, you will be able to:

* Understand Linux users and groups.
* Create user accounts.
* Create and manage groups.
* Add and remove users from groups.
* Change user passwords.
* Verify user and group memberships.
* Understand the principle of least privilege.

---

# Prerequisites

Before starting this lab, ensure you have completed:

* Lab 01 – Build Your Cyber Lab
* Lab 02 – Linux File System Exploration
* Lab 03 – Shell & Terminal Basics
* Lab 04 – Navigation Commands
* Lab 05 – File & Directory Management

---

# Clues

> **"Every investigator deserves an identity."**

> **"A secure team begins with proper access control."**

> **"The right people should have the right permissions—nothing more, nothing less."**

---

# Your Tasks

Complete the following tasks using Linux user and group management commands.

### Task 1 – Review Existing Accounts

Identify the users currently available on your Linux system.

Observe:

* System accounts
* User accounts
* Default administrative account

---

### Task 2 – Create New Analyst Accounts

Create two new user accounts representing SOC analysts.

Assign secure passwords to each account.

Verify that the accounts were created successfully.

---

### Task 3 – Create a Security Team

Create a new Linux group for your Blue Team.

Use a meaningful name that represents your security team.

---

### Task 4 – Assign Analysts to the Team

Add both analyst accounts to the newly created group.

Verify that each analyst is now a member of the security team.

---

### Task 5 – Verify User Information

Review information about each user, including:

* User ID (UID)
* Group ID (GID)
* Group memberships
* Home directory

---

### Task 6 – Test User Access

Switch to one of the newly created user accounts.

Confirm that:

* Login is successful.
* Home directory exists.
* User information is displayed correctly.

Return to your administrator account after testing.

---

### Task 7 – Remove an Analyst from the Team

Simulate an employee leaving the organization.

Remove one analyst from the security group while keeping the account active.

Verify that the group membership has changed.

---

### Task 8 – Document Your Work

Create a short report containing:

* Users created
* Groups created
* User-to-group assignments
* Verification results

---

# Success Criteria

You have successfully completed this lab if you can:

* Create Linux users.
* Create Linux groups.
* Add users to groups.
* Remove users from groups.
* Verify account information.
* Successfully switch between user accounts.

---

# Hint

Ask yourself:

* Which command creates a user?
* Which command creates a group?
* How do you add a user to an existing group?
* How can you verify a user's group membership?
* How do you switch to another user account?

If you need assistance, refer to **`Solutions/Lab-06-Solution.md`**.

---

# Blue Team Insight

Identity and Access Management (IAM) is a fundamental part of cybersecurity.

Blue Team analysts regularly:

* Create accounts for new employees.
* Disable accounts belonging to former employees.
* Manage security groups.
* Audit user permissions.
* Investigate unauthorized account activity.

Proper user management helps prevent unauthorized access and supports the **Principle of Least Privilege**, ensuring users have only the permissions necessary to perform their job.

---

# Challenge

Without using a search engine:

1. Create two new analyst accounts.
2. Create a group named **soc-team**.
3. Add both analysts to the group.
4. Verify that both users belong to the group.
5. Switch to one analyst account and confirm access.
6. Remove one analyst from the group while leaving the account intact.
7. Document the changes you made.

---

# Reflection Questions

1. Why should every user have an individual account?
2. What is the purpose of Linux groups?
3. How does the Principle of Least Privilege improve security?
4. Why is it important to regularly review user accounts and group memberships?

---

# Key Takeaways

After completing this lab, you should be able to:

* Create and manage Linux users.
* Organize users into groups.
* Verify account information.
* Manage user memberships securely.
* Apply user and group management practices in Blue Team and SOC environments.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-06-Solution.md`**.

---

## Next Lab

Continue to **Lab 07 – File Permissions & Ownership**, where you will learn how to control access to files and directories using Linux permissions, ownership, and access control principles.
