# Chapter 9 – Processes and Services

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand what a process is in Linux.
* Differentiate between programs, processes, and services.
* Learn the lifecycle and states of a process.
* Understand Process IDs (PID) and Parent Process IDs (PPID).
* Monitor running processes using common Linux commands.
* Manage processes by stopping, restarting, or terminating them.
* Understand Linux services and the `systemd` init system.
* Apply process management concepts during system administration and incident response.

---

# Introduction

Whenever you open an application, execute a command, or start a service in Linux, the operating system creates a **process**.

A process is simply a **running instance of a program**.

Linux constantly creates, manages, schedules, and terminates thousands of processes to keep the system functioning efficiently.

Understanding processes is essential for system administrators, developers, and cybersecurity professionals because many attacks, malware infections, and performance issues involve malicious or abnormal processes.

---

# Program vs Process

Many beginners confuse these two terms.

## Program

A **program** is a file stored on disk.

Examples:

* Firefox
* Nano
* Bash
* Python

A program is inactive until it is executed.

---

## Process

A **process** is a program that is currently running.

For example:

```bash
firefox
```

Launching Firefox creates one or more running processes.

---

## Comparison

| Program               | Process               |
| --------------------- | --------------------- |
| Stored on disk        | Running in memory     |
| Passive               | Active                |
| Contains instructions | Executes instructions |
| Does not consume CPU  | Uses CPU and memory   |

---

# Process Lifecycle

Every process goes through several stages during its lifetime.

```text
          Program
             │
             ▼
      Process Created
             │
             ▼
        Running State
             │
             ▼
      Waiting / Sleeping
             │
             ▼
       Running Again
             │
             ▼
      Process Terminated
```

---

# Process States

Linux processes exist in different states.

| State    | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| Running  | Currently executing on the CPU                                        |
| Sleeping | Waiting for an event or resource                                      |
| Stopped  | Suspended by the user or system                                       |
| Zombie   | Process has finished but its parent has not collected its exit status |
| Orphan   | Parent process has ended while the child process continues            |

---

# Process ID (PID)

Every process has a unique **Process ID (PID)**.

Example:

```text
PID: 2564
```

Linux uses the PID to identify and manage running processes.

No two active processes have the same PID.

---

# Parent Process ID (PPID)

Every process is started by another process.

The process that starts another process is called the **Parent Process**.

Example:

```text
systemd (PID 1)
      │
      ▼
   bash
      │
      ▼
   firefox
```

The Firefox process has Bash as its parent, and Bash has `systemd` as its parent.

---

# What is systemd?

`systemd` is the default **init system** on most modern Linux distributions.

It is the first process started by the Linux kernel during boot.

Its Process ID is always:

```text
1
```

Responsibilities include:

* Starting system services
* Managing background processes
* Monitoring system health
* Logging events
* Managing system startup

---

# What is a Daemon?

A **daemon** is a background process that runs without direct user interaction.

Examples:

* SSH Server
* Web Server
* Database Server
* Printing Service

Daemon names often end with the letter **d**.

Examples:

* sshd
* httpd
* systemd
* cupsd

---

# Process Hierarchy

Linux organizes processes in a tree structure.

```text
systemd (PID 1)
│
├── NetworkManager
├── sshd
├── cron
├── apache2
└── bash
      │
      ├── nano
      ├── python
      └── ls
```

Each process has a parent except `systemd`, which is the root of the process tree.

---

# Command: ps

## Purpose

Displays information about currently running processes.

---

## Syntax

```bash
ps
```

---

## Example

```bash
ps
```

Example Output

```text
PID TTY          TIME CMD
2521 pts/0    00:00:00 bash
2704 pts/0    00:00:00 ps
```

---

## Useful Options

### Display All Processes

```bash
ps -e
```

---

### Detailed Process Information

```bash
ps -ef
```

Displays:

* PID
* PPID
* User
* CPU Time
* Command

---

### User-Friendly Format

```bash
ps aux
```

This is one of the most commonly used commands by Linux administrators.

📸 **Screenshot Placeholder**

*Insert a screenshot showing the output of `ps aux`.*

---

# Command: top

## Purpose

Displays running processes in real time.

---

## Syntax

```bash
top
```

The display updates automatically every few seconds.

Information includes:

* CPU Usage
* Memory Usage
* Running Processes
* Load Average
* Uptime

Press:

```text
q
```

to exit.

📸 **Screenshot Placeholder**

*Insert a screenshot showing the `top` command.*

---

# Command: htop

## Purpose

Provides an interactive and user-friendly process viewer.

---

## Syntax

```bash
htop
```

Features:

* Colorful interface
* Easy navigation
* Search functionality
* Process filtering
* Interactive process management

> **Note:** `htop` may need to be installed separately using your distribution's package manager.

---

# Command: kill

## Purpose

Terminates a process using its Process ID (PID).

---

## Syntax

```bash
kill PID
```

Example

```bash
kill 3254
```

---

## Force Termination

```bash
kill -9 3254
```

Signal `9` (**SIGKILL**) immediately terminates the process.

Use it only when the process does not respond to normal termination.

---

# Common Signals

| Signal | Name    | Purpose                      |
| ------ | ------- | ---------------------------- |
| 1      | SIGHUP  | Reload configuration         |
| 2      | SIGINT  | Interrupt process (Ctrl + C) |
| 9      | SIGKILL | Forcefully terminate         |
| 15     | SIGTERM | Gracefully terminate         |

---

# Command: pkill

## Purpose

Terminates processes by name instead of PID.

---

## Syntax

```bash
pkill process_name
```

Example:

```bash
pkill firefox
```

Terminates all running Firefox processes.

---

# Command: pgrep

## Purpose

Finds the Process ID of a running process.

---

## Syntax

```bash
pgrep process_name
```

Example:

```bash
pgrep sshd
```

Example Output

```text
845
```

---

# Command: systemctl

## Purpose

Manages system services.

---

## Syntax

```bash
systemctl [command] service_name
```

---

## Check Service Status

```bash
systemctl status ssh
```

---

## Start a Service

```bash
systemctl start apache2
```

---

## Stop a Service

```bash
systemctl stop apache2
```

---

## Restart a Service

```bash
systemctl restart apache2
```

---

## Enable a Service at Boot

```bash
systemctl enable apache2
```

---

## Disable a Service

```bash
systemctl disable apache2
```

📸 **Screenshot Placeholder**

*Insert a screenshot showing `systemctl status ssh`.*

---

# Command: journalctl

## Purpose

Displays logs collected by `systemd`.

---

## Syntax

```bash
journalctl
```

---

## View Latest Logs

```bash
journalctl -n 20
```

Displays the last 20 log entries.

---

## Follow Logs in Real Time

```bash
journalctl -f
```

Continuously displays new log entries as they are generated.

---

## View Logs for a Specific Service

```bash
journalctl -u ssh
```

Displays logs related to the SSH service.

---

# Process Monitoring Workflow

```text
User Starts Program
        │
        ▼
 Linux Creates Process
        │
        ▼
Assign PID and Resources
        │
        ▼
Process Executes
        │
        ▼
Monitor Using:
 ├── ps
 ├── top
 ├── htop
 ├── pgrep
        │
        ▼
Terminate if Necessary
 ├── kill
 └── pkill
```

---

# Blue Team Perspective

Monitoring running processes is a critical task for SOC analysts and incident responders.

Suspicious indicators include:

* Unknown or unexpected processes.
* Processes consuming excessive CPU or memory.
* Services starting unexpectedly.
* Malware disguised as legitimate system processes.
* Processes running from unusual directories such as `/tmp`.

Useful commands during investigations include:

* `ps aux`
* `top`
* `htop`
* `pgrep`
* `systemctl`
* `journalctl`

These commands help identify malicious activity, troubleshoot system issues, and verify the health of critical services.

---

# Common Mistakes

* Forcefully terminating important system processes.
* Confusing a program with a process.
* Using `kill -9` unnecessarily.
* Forgetting to verify a process before terminating it.
* Disabling essential services accidentally.

---

# Best Practices

* Identify a process before terminating it.
* Prefer `SIGTERM` before using `SIGKILL`.
* Regularly monitor CPU and memory usage.
* Review service status after system updates.
* Investigate unfamiliar or unexpected processes.

---

# Chapter Summary

In this chapter, you learned:

* The difference between programs and processes.
* The Linux process lifecycle.
* Process states.
* The purpose of PID and PPID.
* The role of `systemd` and daemons.
* How to monitor processes using `ps`, `top`, and `htop`.
* How to terminate processes with `kill` and `pkill`.
* How to manage services using `systemctl`.
* How to view logs with `journalctl`.

---

# Interview Questions

1. What is a process in Linux?
2. What is the difference between a program and a process?
3. What is a Process ID (PID)?
4. What is a daemon?
5. What is the role of `systemd`?
6. What is the difference between `kill` and `pkill`?
7. What information does the `ps aux` command provide?
8. What is the purpose of the `top` command?
9. How do you check the status of a service?
10. Why is `journalctl` useful during incident investigations?

---

# References

* Linux man pages — https://man7.org/linux/man-pages/
* systemd Documentation — https://systemd.io/
* Ubuntu Documentation — https://help.ubuntu.com/

---

