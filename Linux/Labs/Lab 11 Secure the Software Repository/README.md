# Lab 11 – Package Management

## Scenario

A recently disclosed vulnerability affects several software packages installed on your Linux server. The SOC has instructed all system administrators to verify installed software, apply the latest security updates, remove unnecessary packages, and ensure the system remains secure.

As a Blue Team Analyst, your responsibility is to maintain the system by managing software packages and reducing the attack surface.

---

# Mission

Learn how to install, update, upgrade, verify, and remove software packages while maintaining a secure and stable Linux environment.

---

# Story

A new Common Vulnerabilities and Exposures (CVE) advisory has been published for software running on your Linux server.

Your team leader says:

> *"Keeping software updated is one of the simplest and most effective security controls. An unpatched system is an easy target for attackers. Verify what is installed, apply the necessary updates, and remove anything that is no longer required."*

Your mission is to secure the system through proper package management.

---

# Learning Objectives

After completing this lab, you will be able to:

* Understand Linux package management.
* Update package repositories.
* Upgrade installed software.
* Install new packages.
* Remove unnecessary software.
* Verify installed packages.
* Understand the importance of software updates.

---

# Prerequisites

Before starting this lab, ensure you have completed:

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

---

# Clues

> **"Every outdated package is a potential vulnerability."**

> **"Install only what you need—remove what you don't."**

> **"A secure system begins with regular updates."**

---

# Your Tasks

Complete the following tasks using Linux package management tools.

### Task 1 – Inspect Installed Packages

Review the software currently installed on your system.

Identify:

* Recently installed packages
* Security-related tools
* Essential system packages

Document your observations.

---

### Task 2 – Update Package Repositories

Refresh the local package repository information.

Verify that the repository update completes successfully.

---

### Task 3 – Upgrade Installed Software

Check for available software updates.

Upgrade all installed packages to their latest available versions.

Record the number of updated packages.

---

### Task 4 – Install a New Package

Install a useful utility that is not currently available on your system.

Verify that the installation completed successfully.

---

### Task 5 – Verify Package Information

Inspect information about an installed package.

Determine:

* Version
* Description
* Installation status
* Dependencies

---

### Task 6 – Remove Unnecessary Software

Select a non-essential package.

Remove it from the system while ensuring that critical dependencies are not affected.

---

### Task 7 – Clean the System

Remove unnecessary package files and cached data.

Verify that unused packages have been cleaned from the system.

---

### Task 8 – Create a Maintenance Report

Prepare a report containing:

* Packages updated
* Software installed
* Software removed
* System improvements
* Recommendations for future maintenance

---

# Success Criteria

You have successfully completed this lab if you can:

* Update package repositories.
* Upgrade installed software.
* Install new packages.
* Remove unnecessary packages.
* Verify package information.
* Clean unused package data.

---

# Hint

Before viewing the solution, consider:

* Which command updates package repositories?
* How do you upgrade installed software?
* Which command installs a new package?
* How can you verify package details?
* Which command removes unused packages?

If you need assistance, refer to **`Solutions/Lab-11-Solution.md`**.

---

# Blue Team Insight

Keeping software up to date is a critical security practice.

Blue Team analysts and system administrators regularly:

* Apply security patches.
* Remove vulnerable software.
* Verify package integrity.
* Reduce the system's attack surface.
* Ensure systems comply with organizational security policies.

Many successful cyberattacks exploit known vulnerabilities that already have available security updates.

---

# Challenge

Without using a search engine:

1. Update your package repositories.
2. Upgrade all available software packages.
3. Install a new networking or security utility.
4. Verify its version and installation status.
5. Remove a non-essential package.
6. Clean the package cache and unused dependencies.
7. Document every action you performed.

---

# Reflection Questions

1. Why should systems be updated regularly?
2. What risks are associated with outdated software?
3. Why is it important to remove unnecessary packages?
4. How does package management contribute to system security?

---

# Key Takeaways

After completing this lab, you should be able to:

* Manage software packages confidently.
* Keep Linux systems updated and secure.
* Verify installed software.
* Remove unnecessary applications.
* Apply package management best practices in Blue Team operations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, troubleshooting tips, and screenshots are available in **`Solutions/Lab-11-Solution.md`**.

---

## Next Lab

Continue to **Lab 12 – Bash Scripting**, where you will learn how to automate repetitive administrative tasks and create simple scripts to improve efficiency during Linux administration and security operations.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2011%20Solution%20%E2%80%93%20Package%20Management.md)**
