# Lab 02 — File System Investigation
---

# 🎯 Objectives

After completing this lab, you will be able to:

- Explore the Windows file system using File Explorer.
- Identify important Windows directories.
- Differentiate between files and folders.
- Understand file paths and directory hierarchy.
- View hidden files and file extensions.
- Examine file properties and metadata.
- Use Command Prompt to investigate the file system.
- Understand basic Blue Team file investigation techniques.

---

# 📖 Scenario

You have joined the Security Operations Center (SOC) as a Tier 1 Analyst.

A user reports that several unknown files have appeared on their computer. Before beginning a security investigation, you need to understand how Windows organizes files and where important data is stored.

Your task is to explore the Windows file system and collect basic information about files, folders, and metadata.

---

# 🛠 Requirements

- Windows 10 or Windows 11
- Administrator or Standard User Account
- Command Prompt
- File Explorer

---

# Lab Tasks

## Task 1 — Explore Windows Drives

1. Open **File Explorer**.
2. Select **This PC**.
3. Identify all available drives.

Record:

| Drive | File System | Purpose |
|--------|-------------|---------|
| C: | | |
| D: | | |
| Other | | |

---

## Task 2 — Explore Important Windows Directories

Navigate to the following folders:

```text
C:\Windows
```

```text
C:\Users
```

```text
C:\Program Files
```

```text
C:\Program Files (x86)
```

```text
C:\ProgramData
```

Observe the contents of each directory and identify its purpose.

---

## Task 3 — Display Hidden Items

In File Explorer:

View → Show → Hidden Items

Observe which hidden folders become visible.

Examples may include:

- AppData
- ProgramData
- Desktop.ini

---

## Task 4 — Show File Extensions

Enable file name extensions.

View → Show → File Name Extensions

Observe the extensions of different files.

Examples:

- .txt
- .pdf
- .jpg
- .exe
- .zip

---

## Task 5 — Investigate File Properties

Create a text file named:

```text
Investigation.txt
```

Right-click the file and select **Properties**.

Record the following information:

- File Name
- File Type
- File Size
- Location
- Created Time
- Modified Time
- Accessed Time

---

## Task 6 — Explore the Directory Structure

Open Command Prompt.

Run:

```cmd
tree C:\Users /F
```

Observe how Windows displays folders and files in a hierarchical structure.

---

## Task 7 — Display User Profile

Run:

```cmd
echo %USERPROFILE%
```

Example Output:

```text
C:\Users\John
```

Record your user profile path.

---

## Task 8 — Identify File Attributes

Navigate to your Desktop in Command Prompt.

Run:

```cmd
attrib
```

Observe file attributes.

Common attributes include:

| Attribute | Meaning |
|-----------|---------|
| H | Hidden |
| S | System |
| R | Read Only |
| A | Archive |

---

## Task 9 — Investigate Drive Information

Run:

```cmd
fsutil fsinfo drives
```

Example:

```text
Drives: C:\ D:\
```

Record all available drives.

---

## Task 10 — Investigate Alternate Data Streams (ADS)

Create a text file.

```cmd
echo Hello > test.txt
```

Create a hidden stream.

```cmd
echo Secret > test.txt:hidden.txt
```

View ADS.

```cmd
dir /r
```

Observe the hidden stream associated with the file.

> ⚠ **Note:** Alternate Data Streams (ADS) are supported only on NTFS volumes.

---

# Blue Team Investigation

Imagine a suspicious file named:

```text
invoice.pdf.exe
```

Investigate the file by answering the following questions:

- Is the extension visible?
- What is the actual file type?
- Where is the file located?
- Who owns the file?
- What are its timestamps?
- Does it contain an Alternate Data Stream?
- Would you trust this file?

Document your observations.

---

# Expected Learning Outcomes

After completing this lab, you should be able to:

- Navigate the Windows file system.
- Identify important Windows directories.
- Distinguish between files and folders.
- Display hidden files and extensions.
- View file metadata.
- Use Command Prompt for basic file system investigation.
- Recognize the importance of metadata and ADS during security investigations.

---

# Cleanup

Delete any files created during this lab, including:

```text
Investigation.txt
```

```text
test.txt
```

If you created an Alternate Data Stream, deleting the parent file will also remove the hidden stream.

---

# References

- Microsoft Learn — File Systems
- Microsoft Learn — File Explorer
- Microsoft Learn — NTFS Technical Documentation

---

# ✅ Solution

A complete walkthrough for this lab, including commands, screenshots, expected output, explanations, and investigation notes, is available in the **Solutions** directory.

📂 **Solution Path**

```text
Solutions/
└── Lab 02 - File System Investigation.md
```

> **Tip:** Complete the investigation yourself before reviewing the solution. Comparing your findings with the walkthrough will help reinforce your understanding of the Windows File System and basic Blue Team investigation techniques.