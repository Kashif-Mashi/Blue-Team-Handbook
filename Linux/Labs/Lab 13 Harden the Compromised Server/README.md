# Lab 13 – Linux Security & Hardening

## Scenario

During a routine security assessment, your SOC discovers that a Linux server has several security weaknesses. Although no compromise has been detected, the server is vulnerable due to weak configurations, unnecessary services, outdated software, and poor access controls.

As a Blue Team Analyst, your task is to harden the system by applying Linux security best practices and reducing its attack surface before attackers can exploit these weaknesses.

---

# Mission

Perform a security hardening assessment and strengthen the Linux system by applying security best practices.

---

# Story

Your organization has deployed a new Linux server that will soon host critical business applications.

Before the server is moved into production, your manager gives you one final assignment.

> *"A secure system isn't built after an attack—it's built before one. Your job is to identify weaknesses, reduce the attack surface, and ensure this server is ready to defend itself."*

Your mission is to secure the server following Linux security best practices.

---

# Learning Objectives

After completing this lab, you will be able to:

* Assess the security posture of a Linux system.
* Apply Linux hardening techniques.
* Secure user accounts.
* Configure password policies.
* Review file permissions.
* Manage unnecessary services.
* Configure the firewall.
* Verify system security after hardening.

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
* Lab 11 – Package Management
* Lab 12 – Bash Scripting

---

# Clues

> **"The strongest defense is preparation."**

> **"Every unnecessary service is another opportunity for an attacker."**

> **"Reduce what attackers can access before they ever arrive."**

---

# Your Tasks

Complete the following tasks to improve the security of your Linux system.

### Task 1 – Review User Accounts

Inspect all user accounts on the system.

Identify:

* Inactive accounts
* Unnecessary accounts
* Administrative accounts

Document your observations.

---

### Task 2 – Review Password Security

Evaluate password settings.

Ensure that:

* Strong passwords are being used.
* Password expiration policies are configured appropriately.
* Default passwords have been changed.

---

### Task 3 – Audit File Permissions

Review important system files and directories.

Identify files with overly permissive access and correct them where appropriate.

---

### Task 4 – Secure Running Services

Review all active services.

Identify:

* Unnecessary services
* Disabled services
* Services that should start automatically

Stop or disable services that are not required in your lab environment.

---

### Task 5 – Configure the Firewall

Review the firewall configuration.

Ensure that:

* Only required services are allowed.
* Unnecessary ports are blocked.
* Firewall rules are active and functioning correctly.

---

### Task 6 – Verify System Updates

Confirm that the operating system and installed packages are fully updated.

Record any remaining updates or security recommendations.

---

### Task 7 – Perform a Basic Security Audit

Review the system for common security issues, including:

* Open ports
* Running services
* User permissions
* Software updates
* Firewall configuration

Document any findings.

---

### Task 8 – Prepare a Security Hardening Report

Create a report containing:

* Security weaknesses identified
* Hardening measures applied
* Verification results
* Remaining recommendations

---

# Success Criteria

You have successfully completed this lab if you can:

* Identify security weaknesses.
* Improve account security.
* Audit file permissions.
* Disable unnecessary services.
* Configure the firewall.
* Verify system updates.
* Document the hardening process.

---

# Hint

Before viewing the solution, ask yourself:

* Which users actually require access to the system?
* Are any services running that are not needed?
* Are important files properly protected?
* Is the firewall configured correctly?
* Is the system fully patched?

If you need assistance, refer to **`Solutions/Lab-13-Solution.md`**.

---

# Blue Team Insight

System hardening is a proactive security practice that reduces the likelihood of successful attacks.

Blue Team professionals routinely:

* Remove unnecessary software.
* Disable unused services.
* Enforce strong authentication.
* Secure file permissions.
* Apply security patches.
* Monitor firewall rules.
* Conduct regular security audits.

A hardened system is significantly more resilient against common attack techniques and forms the foundation of a secure enterprise environment.

---

# Challenge

Without using a search engine:

1. Identify all administrative user accounts.
2. Disable one unnecessary service in your lab environment.
3. Review and improve permissions on a sensitive system file.
4. Verify that the firewall allows only required network traffic.
5. Confirm that your system is fully updated.
6. Create a security hardening checklist based on your findings.

---

# Reflection Questions

1. What is Linux system hardening?
2. Why should unnecessary services be disabled?
3. How does a firewall contribute to system security?
4. Why are regular security audits important?
5. Which hardening measure do you consider most effective, and why?

---

# Key Takeaways

After completing this lab, you should be able to:

* Assess the security posture of a Linux system.
* Apply essential Linux hardening techniques.
* Reduce the system's attack surface.
* Strengthen authentication and access controls.
* Perform a basic security audit.
* Prepare a Linux server for secure operation.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, troubleshooting tips, and screenshots are available in **`Solutions/Lab-13-Solution.md`**.

---

## Next Lab

Continue to **Lab 14 – Blue Team Linux Challenge**, where you will apply everything learned throughout the Linux Fundamentals course by investigating and securing a simulated Linux system in a comprehensive, real-world scenario.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2013%20Solution%20%E2%80%93%20Linux%20Security%20%26%20Hardening.md)**
