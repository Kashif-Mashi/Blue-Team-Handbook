# Chapter 13 – Bash Scripting Basics

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand what Bash scripting is.
* Learn why automation is important in Linux.
* Create and execute Bash scripts.
* Use variables, comments, and user input.
* Apply conditional statements and loops.
* Create reusable functions.
* Pass command-line arguments to scripts.
* Understand exit codes.
* Follow scripting best practices for system administration and cybersecurity.

---

# Introduction

Imagine performing the same task every day:

* Creating backup folders.
* Checking disk usage.
* Monitoring log files.
* Updating the system.
* Creating user accounts.
* Collecting system information.

Typing the same commands repeatedly is time-consuming and increases the chance of mistakes.

Linux solves this problem with **Bash scripting**.

A Bash script is simply a text file containing Linux commands that are executed automatically in sequence.

Automation is one of the most valuable skills for Linux administrators, DevOps engineers, SOC analysts, and cybersecurity professionals.

---

# What is Bash?

**Bash (Bourne Again SHell)** is the default command-line interpreter on most Linux distributions.

It allows users to:

* Execute commands.
* Manage files.
* Run programs.
* Automate repetitive tasks.
* Write scripts.

---

# What is a Bash Script?

A **Bash script** is a plain text file that contains one or more Linux commands.

Instead of typing commands one by one, you save them in a file and execute the file.

Example:

```text
backup.sh
```

---

# Why Use Bash Scripts?

Bash scripting provides several advantages:

* Saves time.
* Reduces manual errors.
* Automates repetitive tasks.
* Improves consistency.
* Simplifies system administration.
* Helps manage multiple systems efficiently.

---

# Bash Script Workflow

```text
Write Script
      │
      ▼
Save File (.sh)
      │
      ▼
Make Executable
      │
      ▼
Run Script
      │
      ▼
Linux Executes Commands
```

---

# Creating Your First Script

Create a file using your preferred text editor.

Example:

```bash
nano hello.sh
```

Add the following content:

```bash
#!/bin/bash

echo "Hello, Linux!"
```

Save the file.

---

# The Shebang (`#!`)

The first line of most Bash scripts is:

```bash
#!/bin/bash
```

This is called the **Shebang**.

It tells Linux which interpreter should execute the script.

Common examples:

| Shebang               | Purpose                                    |
| --------------------- | ------------------------------------------ |
| `#!/bin/bash`         | Run using Bash                             |
| `#!/bin/sh`           | Run using the Bourne Shell                 |
| `#!/usr/bin/env bash` | Locate Bash using the system's environment |

---

# Making a Script Executable

Before running a script directly, give it execute permission.

```bash
chmod +x hello.sh
```

Run the script:

```bash
./hello.sh
```

Example Output:

```text
Hello, Linux!
```

📸 **Screenshot Placeholder**

*Insert a screenshot showing the creation and execution of `hello.sh`.*

---

# Comments

Comments are ignored by Bash and are used to explain code.

Single-line comment:

```bash
# This is a comment
```

Example:

```bash
#!/bin/bash

# Display a welcome message
echo "Welcome"
```

Comments make scripts easier to understand and maintain.

---

# Variables

Variables store values that can be reused throughout a script.

Syntax:

```bash
variable_name=value
```

Example:

```bash
#!/bin/bash

name="Kashif"

echo $name
```

Output:

```text
Kashif
```

---

# Rules for Variable Names

* Begin with a letter or underscore.
* Do not start with a number.
* Do not include spaces.
* Variable names are case-sensitive.

Valid:

```text
username
user_name
AGE
```

Invalid:

```text
1name
user name
```

---

# User Input

The `read` command accepts input from the user.

Example:

```bash
#!/bin/bash

echo "Enter your name:"
read name

echo "Welcome $name"
```

Example Output:

```text
Enter your name:
Kashif

Welcome Kashif
```

---

# Command-Line Arguments

Arguments allow users to provide information when running a script.

Example:

```bash
./hello.sh Kashif
```

Script:

```bash
#!/bin/bash

echo "Hello $1"
```

Output:

```text
Hello Kashif
```

Common argument variables:

| Variable | Description         |
| -------- | ------------------- |
| `$0`     | Script name         |
| `$1`     | First argument      |
| `$2`     | Second argument     |
| `$#`     | Number of arguments |
| `$@`     | All arguments       |

---

# Conditional Statements

Conditional statements allow a script to make decisions.

Syntax:

```bash
if condition
then
    commands
fi
```

Example:

```bash
#!/bin/bash

age=20

if [ $age -ge 18 ]
then
    echo "Adult"
fi
```

Output:

```text
Adult
```

---

# if...else Statement

Example:

```bash
#!/bin/bash

age=16

if [ $age -ge 18 ]
then
    echo "Adult"
else
    echo "Minor"
fi
```

---

# Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `-eq`    | Equal                 |
| `-ne`    | Not Equal             |
| `-gt`    | Greater Than          |
| `-lt`    | Less Than             |
| `-ge`    | Greater Than or Equal |
| `-le`    | Less Than or Equal    |

---

# Loops

Loops repeat commands automatically.

---

## for Loop

Example:

```bash
#!/bin/bash

for i in 1 2 3 4 5
do
    echo $i
done
```

Output:

```text
1
2
3
4
5
```

---

## while Loop

Example:

```bash
#!/bin/bash

count=1

while [ $count -le 5 ]
do
    echo $count
    count=$((count+1))
done
```

---

# Functions

Functions allow code to be reused.

Example:

```bash
#!/bin/bash

greet() {
    echo "Welcome to Linux"
}

greet
```

Functions improve readability and reduce duplicate code.

---

# Exit Codes

Every Linux command returns an **exit code**.

Common values:

| Exit Code | Meaning          |
| --------- | ---------------- |
| `0`       | Success          |
| Non-zero  | Error or failure |

Check the exit status of the previous command:

```bash
echo $?
```

Example:

```bash
mkdir TestFolder

echo $?
```

Output:

```text
0
```

---

# Common Bash Operators

| Operator | Purpose         |
| -------- | --------------- |
| `=`      | Assign a value  |
| `==`     | Compare strings |
| `!=`     | Not equal       |
| `&&`     | Logical AND     |
| `\|\|`   | Logical OR      |
| `!`      | Logical NOT     |

---

# Useful Bash Commands

| Command    | Purpose                       |
| ---------- | ----------------------------- |
| `echo`     | Display text                  |
| `read`     | Read user input               |
| `date`     | Display current date and time |
| `pwd`      | Print current directory       |
| `whoami`   | Display current user          |
| `hostname` | Display system hostname       |

---

# Sample Bash Script

```bash
#!/bin/bash

echo "===== System Information ====="

echo "User:"
whoami

echo

echo "Hostname:"
hostname

echo

echo "Current Directory:"
pwd

echo

echo "Date:"
date
```

Example Output:

```text
===== System Information =====

User:
kashif

Hostname:
ubuntu

Current Directory:
/home/kashif

Date:
Sat Jul 25 11:30:00 PKT 2026
```

📸 **Screenshot Placeholder**

*Insert a screenshot showing the execution of the system information script.*

---

# Bash Scripting Workflow

```text
Write Script
      │
      ▼
Test Script
      │
      ▼
Fix Errors
      │
      ▼
Run Successfully
      │
      ▼
Automate Tasks
```

---

# Blue Team Perspective

Bash scripting is widely used by SOC analysts, system administrators, and incident responders.

Common automation tasks include:

* Collecting system information.
* Searching log files for Indicators of Compromise (IoCs).
* Monitoring disk usage.
* Checking running processes.
* Monitoring network connections.
* Creating backups.
* Collecting forensic artifacts.
* Automating routine security checks.

Automation reduces response time and improves consistency during security operations.

---

# Common Mistakes

* Forgetting the Shebang line.
* Running scripts without execute permission.
* Using spaces around the `=` operator when assigning variables.
* Not testing scripts before using them on production systems.
* Ignoring exit codes after running important commands.

---

# Best Practices

* Keep scripts simple and readable.
* Use meaningful variable names.
* Add comments to explain complex logic.
* Test scripts in a safe environment before deployment.
* Check exit codes and handle errors appropriately.
* Follow the Principle of Least Privilege when executing scripts.

---

# Chapter Summary

In this chapter, you learned:

* What Bash scripting is.
* Why automation is important.
* How to create and execute Bash scripts.
* How to use variables, comments, user input, and command-line arguments.
* How to use conditional statements, loops, and functions.
* How to work with exit codes.
* Best practices for writing reliable Bash scripts.

---

# Interview Questions

1. What is Bash?
2. What is a Bash script?
3. What is the purpose of the Shebang (`#!`)?
4. How do you make a script executable?
5. What is the difference between `read` and command-line arguments?
6. What are exit codes in Linux?
7. What does `$1` represent in a Bash script?
8. What is the purpose of a function?
9. What is the difference between a `for` loop and a `while` loop?
10. Why is Bash scripting valuable for system administrators and SOC analysts?

---

# References

* GNU Bash Manual — https://www.gnu.org/software/bash/manual/
* Linux Documentation Project — https://tldp.org/
* Ubuntu Documentation — https://help.ubuntu.com/

---


