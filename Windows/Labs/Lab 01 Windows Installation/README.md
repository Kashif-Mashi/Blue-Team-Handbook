# Lab 01 — Windows Installation

> **Difficulty:** Beginner  
> **Estimated Time:** 45–60 Minutes

---

# 🎯 Objectives

By completing this lab, you will be able to:

- Understand Windows installation requirements.
- Create a bootable Windows installation media (optional).
- Install Windows 10 or Windows 11 in a virtual machine.
- Complete the Out-of-Box Experience (OOBE).
- Configure the initial user account.
- Verify a successful installation.

---

# 📖 Scenario

Your organization has received a new workstation that needs to be prepared for a security analyst.

Before performing investigations or installing security tools, Windows must be installed and configured correctly.

As a Blue Team analyst, understanding the Windows installation process helps you deploy, rebuild, and troubleshoot enterprise endpoints.

---

# 🛠️ Lab Requirements

- Oracle VirtualBox or VMware Workstation
- Windows 10/11 ISO
- Minimum 4 GB RAM (8 GB Recommended)
- 50 GB Virtual Disk
- Internet Connection (Optional)

> **Note:** If Windows is already installed on your computer and you cannot create a virtual machine due to hardware or storage limitations, you may review the installation process using Microsoft's documentation or proceed to the next lab.

---

# Task 1 — Download Windows ISO

Download the official Windows ISO from Microsoft.

Official Website:

https://www.microsoft.com/software-download/

---

## Verify

Confirm that the ISO file has been downloaded successfully.

---

# Task 2 — Create a Virtual Machine

Create a new virtual machine.

Recommended Configuration

| Setting | Value |
|----------|-------|
| Operating System | Windows 11 (64-bit) |
| RAM | 4096 MB or Higher |
| CPU | 2 Cores or More |
| Storage | 50 GB (Dynamic) |
| Network | NAT |


---

# Task 3 — Mount the Windows ISO

Open the VM settings.

Attach the Windows ISO to the virtual optical drive.

Start the virtual machine.

---

# Task 4 — Begin Windows Installation

Choose:

- Language
- Time & Currency
- Keyboard Layout

Click **Next**.

Click **Install Now**.

---

# Task 5 — Select Windows Edition

Choose the appropriate Windows edition.

Examples:

- Windows 11 Home
- Windows 11 Pro

Accept the license agreement.

Click **Next**.

---

# Task 6 — Partition the Virtual Disk

Select

**Custom: Install Windows only (Advanced)**

Choose the unallocated virtual disk.

Click **Next**.

Windows will automatically create the required partitions.
---

# Task 7 — Wait for Installation

Windows copies files and installs the operating system.

The virtual machine will restart automatically several times.

---

# Task 8 — Complete Initial Setup (OOBE)

Configure:

- Country
- Keyboard Layout
- Device Name (Optional)
- User Account
- Password
- Privacy Settings

---

# Task 9 — Verify Installation

After logging in, verify:

- Desktop loads successfully.
- Start Menu opens.
- File Explorer works.
- Settings application opens.

Run:

```cmd
winver
```

Confirm the Windows edition and version.

---

# Challenge Questions

1. What is an ISO file?

2. Why is a virtual machine useful for cybersecurity labs?

3. Which installation option creates Windows on a new disk?

4. Which Windows edition did you install?

5. Which command displays the Windows version?

6. What is the purpose of the Out-of-Box Experience (OOBE)?

7. Why should security professionals practice Windows installation?

---

# Lab Summary

In this lab, you learned how to:

- Obtain the Windows installation media.
- Create a virtual machine.
- Install Windows.
- Complete the initial setup.
- Verify the installation.

This lab prepares the Windows environment for the remaining Windows Fundamentals exercises.

---

# Cleanup

No cleanup is required.

The virtual machine will be used in future labs.

---
---

# ✅ Solution

A complete step-by-step solution for this lab, including commands, screenshots, explanations, and challenge answers, is available in the **Solutions** directory.

📂 **Solution Path:**

```text
Solutions/Lab 01 - Windows Installation.md
```

> **Tip:** Attempt the lab on your own before reviewing the solution. Use the solution to verify your work, understand the expected output, and compare your results.
---

# Next Lab

➡ **Lab 02 — Windows File System Investigation**

---

# Related Chapter

📖 Chapter 02 — Windows Installation & Initial Configuration

---

# References

- Microsoft Learn
- Microsoft Windows Documentation
- Oracle VirtualBox Documentation
- VMware Documentation