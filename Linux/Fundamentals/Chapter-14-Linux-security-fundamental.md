# Chapter 14 – Linux Security Fundamentals

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand the core principles of Linux security.
* Learn how Linux protects users, files, and processes.
* Understand authentication and authorization.
* Apply the Principle of Least Privilege.
* Learn firewall fundamentals.
* Secure remote access using SSH.
* Understand software updates and vulnerability management.
* Follow Linux security best practices.
* Recognize Linux's role in Blue Team and SOC operations.

---

# Introduction

Linux powers millions of systems worldwide, including:

* Web servers
* Cloud platforms
* Enterprise networks
* IoT devices
* Supercomputers
* Security appliances

Because Linux is widely used, it is also a common target for cyberattacks.

Fortunately, Linux includes many built-in security features that help protect systems from unauthorized access, malware, and privilege escalation.

Understanding these security fundamentals is essential for every Linux user, system administrator, and cybersecurity professional.

---

# What is Linux Security?

Linux security is the collection of technologies, configurations, and best practices used to protect:

* Users
* Files
* Processes
* Applications
* Network services
* System resources

The goal is to ensure:

* Confidentiality
* Integrity
* Availability

These three principles are known as the **CIA Triad**.

---

# The CIA Triad

```text
          CIA TRIAD

      Confidentiality
             ▲
            / \
           /   \
          /     \
 Integrity ----- Availability
```

### Confidentiality

Ensures that only authorized users can access data.

Examples:

* File permissions
* Password protection
* Encryption

---

### Integrity

Ensures data cannot be modified without authorization.

Examples:

* Checksums
* Digital signatures
* File permissions
* Version control

---

### Availability

Ensures systems and services remain accessible.

Examples:

* Backups
* Redundant systems
* Monitoring
* High Availability (HA)

---

# Authentication vs Authorization

These terms are often confused.

## Authentication

Authentication verifies **who you are**.

Examples:

* Username and password
* SSH key
* Multi-Factor Authentication (MFA)

Question answered:

> Who are you?

---

## Authorization

Authorization determines **what you are allowed to do**.

Examples:

* File permissions
* User groups
* Sudo privileges

Question answered:

> What are you allowed to access?

---

## Comparison

| Authentication    | Authorization                    |
| ----------------- | -------------------------------- |
| Verifies identity | Grants permissions               |
| Happens first     | Happens after authentication     |
| Example: Login    | Example: Accessing `/etc/shadow` |

---

# Principle of Least Privilege (PoLP)

The **Principle of Least Privilege (PoLP)** means that users and applications should have **only the permissions they need** to perform their tasks.

Example:

* A student can edit their own assignment.
* A teacher can grade assignments.
* Only the administrator can change system settings.

This reduces the impact of accidental mistakes and security breaches.

---

# Root User

The **root** account has complete control over the Linux system.

Root can:

* Modify any file.
* Install software.
* Create or delete users.
* Change permissions.
* Shut down the system.

Because root has unrestricted privileges, it should be used only when necessary.

---

# Sudo

Instead of logging in directly as root, Linux encourages users to use the `sudo` command.

Example:

```bash
sudo apt update
```

Benefits:

* Limits administrative access.
* Records administrative actions in logs.
* Reduces the risk of accidental system changes.

---

# Password Security

Strong passwords are one of the simplest and most effective security controls.

A strong password should:

* Be at least 12 characters long.
* Include uppercase and lowercase letters.
* Include numbers.
* Include special characters.
* Avoid dictionary words.
* Be unique for each account.

Avoid:

```text
password123
admin
12345678
```

---

# Multi-Factor Authentication (MFA)

MFA requires two or more methods of verification.

Common factors:

| Factor             | Example                           |
| ------------------ | --------------------------------- |
| Something you know | Password                          |
| Something you have | Mobile authenticator app          |
| Something you are  | Fingerprint or facial recognition |

Even if a password is compromised, MFA provides an additional layer of protection.

---

# SSH Security

SSH is the preferred method for remote administration.

Best practices include:

* Disable root login.
* Use SSH keys instead of passwords.
* Change the default SSH port only if appropriate for your environment.
* Disable unused accounts.
* Enable logging.
* Keep the SSH server updated.

Example:

```bash
ssh username@192.168.1.100
```

---

# Firewall Basics

A firewall controls incoming and outgoing network traffic.

It acts as a security barrier between trusted and untrusted networks.

```text
Internet
     │
     ▼
 Firewall
     │
     ▼
Linux Server
```

Common firewall tools:

* UFW (Ubuntu Firewall)
* firewalld
* nftables
* iptables (legacy environments)

---

# Command: ufw

## Purpose

UFW (Uncomplicated Firewall) simplifies firewall management on Ubuntu and Debian-based systems.

---

## Check Firewall Status

```bash
sudo ufw status
```

---

## Enable Firewall

```bash
sudo ufw enable
```

---

## Disable Firewall

```bash
sudo ufw disable
```

---

## Allow SSH

```bash
sudo ufw allow ssh
```

---

## Allow HTTP

```bash
sudo ufw allow 80/tcp
```

---

## Deny a Port

```bash
sudo ufw deny 23
```

Example Output:

```text
Rule added
```

📸 **Screenshot Placeholder**

*Insert a screenshot showing the output of `sudo ufw status`.*

---

# Software Updates

Keeping software updated is one of the most effective ways to improve security.

Updates provide:

* Security patches
* Bug fixes
* Performance improvements
* Vulnerability mitigation

Example:

```bash
sudo apt update

sudo apt upgrade
```

---

# File Permissions

Incorrect file permissions can expose sensitive information.

Review permissions regularly using:

```bash
ls -l
```

Modify permissions when needed:

```bash
chmod
```

Change ownership:

```bash
chown
```

---

# Security Logging

Logs help detect suspicious activity.

Common logs include:

* Authentication logs
* SSH logs
* System logs
* Application logs

Useful commands:

```bash
journalctl
```

```bash
tail -f /var/log/auth.log
```

---

# Malware Protection

Although Linux experiences less traditional malware than some other operating systems, it is not immune.

Potential threats include:

* Rootkits
* Cryptominers
* Backdoors
* Web shells
* Malicious scripts

Security measures include:

* Regular updates.
* File integrity monitoring.
* Antivirus tools where appropriate.
* Log analysis.
* Least privilege.

---

# Backup Strategy

Backups protect against:

* Hardware failure
* Accidental deletion
* Malware
* Ransomware
* Data corruption

A common recommendation is the **3-2-1 Backup Rule**:

* Keep **3** copies of your data.
* Store them on **2** different types of media.
* Keep **1** copy off-site or offline.

---

# Linux Security Workflow

```text
User Login
     │
     ▼
Authentication
     │
     ▼
Authorization
     │
     ▼
Permission Check
     │
     ▼
Access Granted
     │
     ▼
Activity Logged
     │
     ▼
Monitoring & Alerts
```

---

# Linux in Blue Team Operations

Linux plays a major role in defensive security.

Common Linux-based security platforms include:

* Wazuh
* Suricata
* Zeek
* Security Onion
* Splunk Forwarder
* Elastic Agent

Blue Team professionals use Linux to:

* Monitor security events.
* Collect and analyze logs.
* Detect intrusions.
* Perform malware analysis.
* Respond to incidents.
* Automate security tasks with Bash and Python.

---

# Common Mistakes

* Logging in directly as root.
* Using weak or reused passwords.
* Leaving unnecessary services enabled.
* Ignoring security updates.
* Disabling the firewall without a valid reason.
* Granting excessive file permissions.
* Failing to review logs regularly.

---

# Best Practices

* Apply the Principle of Least Privilege.
* Keep the operating system and applications updated.
* Use strong passwords and enable MFA where available.
* Use SSH keys instead of passwords.
* Enable and configure a firewall.
* Monitor logs for suspicious activity.
* Remove unused accounts and software.
* Back up important data regularly.
* Audit permissions periodically.
* Document system changes.

---

# Chapter Summary

In this chapter, you learned:

* The core principles of Linux security.
* The CIA Triad.
* Authentication vs. authorization.
* The Principle of Least Privilege.
* Root and `sudo`.
* Password security and MFA.
* Firewall fundamentals with UFW.
* The importance of software updates.
* Logging, backups, and security best practices.
* The role of Linux in Blue Team operations.

---

# Interview Questions

1. What is the CIA Triad?
2. What is the difference between authentication and authorization?
3. What is the Principle of Least Privilege?
4. Why should administrators avoid logging in directly as the root user?
5. What is the purpose of the `sudo` command?
6. Why is Multi-Factor Authentication important?
7. What is the role of a firewall?
8. What does the `ufw status` command display?
9. Why are regular software updates critical for security?
10. How is Linux used in Security Operations Centers (SOCs)?

---

# References

* Ubuntu Security Documentation — https://ubuntu.com/security
* Linux man pages — https://man7.org/linux/man-pages/
* NIST Cybersecurity Framework — https://www.nist.gov/cyberframework
* CIS Benchmarks — https://www.cisecurity.org/cis-benchmarks
* OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/

---

# Congratulations!

You have completed the **Linux Fundamentals** section of the **Blue Team Handbook**.

### What You Have Learned

Throughout these 14 chapters, you built a strong foundation in Linux, including:

* Linux architecture and distributions
* Installation and system setup
* File system hierarchy
* Shell and terminal usage
* Navigation and file management
* Users, groups, and permissions
* Process and service management
* Networking fundamentals
* Logging and monitoring
* Package management
* Bash scripting
* Linux security fundamentals

These concepts form the foundation for advanced topics such as:

* Linux Hardening
* Wazuh SIEM Administration
* Security Onion
* Splunk
* Incident Response
* Digital Forensics
* Threat Hunting
* Malware Analysis
* Cloud Security
* SOC Operations

Continue practicing in virtual machines and lab environments. Consistent hands-on experience is the key to becoming proficient in Linux and succeeding in Blue Team roles.
