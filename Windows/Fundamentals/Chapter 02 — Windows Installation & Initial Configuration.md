# Chapter 02 — Windows Installation & Initial Configuration

---

# 📖 Overview

Before using Windows for daily tasks or cybersecurity operations, the operating system must be properly installed and configured. The initial configuration determines how Windows operates, how users access the system, and how security features are applied.

This chapter introduces the Windows installation process, the Out-of-Box Experience (OOBE), user account creation, Windows Update, and essential system configuration.

> **Note**
>
> A complete step-by-step Windows installation guide is available in the **Security Operations** repository. This chapter focuses on understanding the installation process and the basic configuration performed after Windows is installed.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Understand the Windows installation process.
- Explain the purpose of the Out-of-Box Experience (OOBE).
- Create and configure user accounts.
- Understand the importance of Windows Update.
- Perform basic Windows configuration.
- Prepare a Windows system for future labs.

---

# Windows Installation

Installing Windows is the process of copying the operating system files to a storage device and preparing the computer to boot into Windows.

During installation, Windows creates the required system partitions, installs the operating system files, configures the boot loader, and prepares the computer for its first startup.

The basic installation process consists of:

1. Boot from Windows installation media.
2. Select language and regional settings.
3. Choose the Windows edition.
4. Accept the license agreement.
5. Select or create a storage partition.
6. Install Windows.
7. Restart the computer.
8. Complete the Out-of-Box Experience (OOBE).

---

# Windows Installation Process

```text
Boot Installation Media
          │
          ▼
Windows Setup
          │
          ▼
Select Language
          │
          ▼
Choose Windows Edition
          │
          ▼
Accept License
          │
          ▼
Partition Disk
          │
          ▼
Install Windows
          │
          ▼
Restart Computer
          │
          ▼
Out-of-Box Experience (OOBE)
          │
          ▼
Windows Desktop
```

---

# Out-of-Box Experience (OOBE)

The **Out-of-Box Experience (OOBE)** is the first-time setup wizard that appears immediately after Windows installation.

Its purpose is to configure the operating system before it is used.

During OOBE, Windows asks for several configuration options including:

- Country or Region
- Keyboard Layout
- Internet Connection
- Device Name
- Microsoft Account or Local Account
- Password
- Privacy Settings

After these steps are completed, Windows prepares the desktop and finishes the initial setup.

---

# User Accounts

A user account allows a person to log in and use the computer.

Every action performed in Windows is associated with a user account.

There are two common types of accounts.

## Local Account

A Local Account is created and stored only on the current computer.

Characteristics:

- Does not require an Internet connection.
- Data remains on the local device.
- Suitable for standalone systems and lab environments.

---

## Microsoft Account

A Microsoft Account is connected to Microsoft's online services.

Benefits include:

- Cloud synchronization
- Microsoft Store access
- OneDrive integration
- Password recovery
- Device synchronization

---

# Administrator vs Standard User

Windows provides different permission levels.

| Account Type | Description |
|--------------|-------------|
| Administrator | Full control over the system, including installing software, changing settings, and managing users. |
| Standard User | Limited permissions for everyday activities. Administrative approval is required for system-level changes. |

For security reasons, it is recommended to use a **Standard User** account for daily work and an **Administrator** account only when elevated privileges are required.

---

# Windows Updates

Windows Update keeps the operating system secure, stable, and up to date.

Microsoft regularly releases updates to:

- Fix security vulnerabilities
- Improve system performance
- Resolve software bugs
- Add new features
- Improve hardware compatibility

Keeping Windows updated is one of the simplest and most effective security practices.

---

# Types of Windows Updates

| Update Type | Purpose |
|-------------|---------|
| Security Updates | Fix security vulnerabilities |
| Quality Updates | Improve reliability and stability |
| Feature Updates | Introduce new Windows features |
| Driver Updates | Improve hardware compatibility |
| Defender Updates | Update malware definitions |

---

# Basic Windows Configuration

After installation, several basic configuration tasks should be completed.

## Verify Windows Activation

Confirm that Windows has been activated successfully.

---

## Install Windows Updates

Download and install all available updates before using the system.

---

## Configure Time and Region

Verify that the correct:

- Time Zone
- Date
- Language
- Region

have been configured.

---

## Configure Windows Security

Ensure the following features are enabled:

- Microsoft Defender
- Windows Firewall
- User Account Control (UAC)

---

## Rename the Computer (Optional)

Assign a meaningful computer name.

Example:

```text
SOC-PC01
```

Using descriptive computer names makes device management easier in enterprise environments.

---

## Create Additional User Accounts

If multiple people use the computer, create separate user accounts for each person.

This improves accountability and security.

---

# Best Practices

- Install Windows from an official Microsoft source.
- Keep Windows Update enabled.
- Use strong passwords.
- Enable Microsoft Defender.
- Leave Windows Firewall enabled.
- Create separate user accounts.
- Install only trusted software.
- Regularly back up important files.

---

# Important Notes

> Windows should always be updated before installing additional applications or security tools.

> Avoid using the Administrator account for daily activities whenever possible.

> Never disable Windows Defender or the Firewall unless required for troubleshooting in a controlled environment.

---

# Summary

In this chapter, you learned:

- The Windows installation process.
- The purpose of the Out-of-Box Experience (OOBE).
- The difference between Local and Microsoft accounts.
- Administrator and Standard User accounts.
- The importance of Windows Update.
- Basic Windows configuration tasks.
- Security best practices after installation.

These initial configuration steps prepare the operating system for the remaining Windows Fundamentals chapters and labs.

---

# Key Takeaways

- Windows installation prepares the operating system for first use.
- OOBE performs the initial system configuration.
- Every user should have their own account.
- Windows Update is essential for system security.
- Basic configuration improves security and usability.
- Proper setup creates a stable foundation for future administration and Blue Team operations.

---

# Next Chapter

➡ **Chapter 03 — Windows File System & File Explorer**