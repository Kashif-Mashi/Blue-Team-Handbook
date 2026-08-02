# Lab 08 – Processes & Services

## Scenario

Employees have reported that a Linux server has become unusually slow. Applications are taking longer than expected to respond, and the CPU usage has increased significantly. The SOC suspects that an unauthorized process may be consuming system resources.

As a Blue Team Analyst, your responsibility is to investigate running processes, identify suspicious activity, and ensure that only legitimate system services remain active.

---

# Mission

Investigate running processes and system services to identify abnormal behavior and maintain a healthy Linux system.

---

# Story

Your SOC receives an alert indicating that a critical Linux server is experiencing high CPU utilization.

Your team leader approaches your desk and says:

> *"Attackers often leave behind malicious processes that run silently in the background. Before we can determine whether this is an attack or a system issue, we need you to investigate what's running on the server."*

Your mission is to inspect active processes, monitor system resources, and verify the status of important services.

---

# Learning Objectives

After completing this lab, you will be able to:

* Understand Linux processes and services.
* View running processes.
* Monitor CPU and memory usage.
* Identify suspicious or resource-intensive processes.
* Stop or terminate unnecessary processes.
* Manage Linux services.
* Verify the status of system services.

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

---

# Clues

> **"Every running program leaves a footprint."**

> **"Not every process belongs on the system."**

> **"A healthy server is one where every process has a purpose."**

---

# Your Tasks

Complete the following tasks using Linux process and service management tools.

### Task 1 – Inspect Running Processes

View the processes currently running on your system.

Identify:

* Process Name
* Process ID (PID)
* User
* CPU Usage
* Memory Usage

---

### Task 2 – Monitor System Performance

Observe your system's resource utilization.

Identify which processes consume the most:

* CPU
* Memory

Record your observations.

---

### Task 3 – Investigate a Process

Select one running process and investigate:

* Process owner
* Parent process
* Command used to start the process

Document your findings.

---

### Task 4 – Manage a Process

Start a harmless background process.

Locate its Process ID (PID).

Terminate the process safely and verify that it is no longer running.

---

### Task 5 – Examine System Services

Review the services currently installed on your Linux system.

Determine which services are:

* Active
* Inactive
* Failed

---

### Task 6 – Control a Service

Select a non-critical service and:

* Check its current status.
* Stop the service.
* Start the service again.
* Verify that it is running correctly.

---

### Task 7 – Investigate Startup Services

Review which services automatically start during system boot.

Identify any services that may not be necessary for your lab environment.

---

### Task 8 – Document Your Investigation

Create a report containing:

* High-resource processes
* Services inspected
* Actions performed
* Observations
* Recommendations

---

# Success Criteria

You have successfully completed this lab if you can:

* View running processes.
* Identify resource-intensive processes.
* Monitor system performance.
* Terminate unnecessary processes.
* Manage Linux services.
* Verify service status.

---

# Hint

Consider the following questions before searching for the solution:

* Which command lists running processes?
* Which utility provides a real-time view of system performance?
* How do you stop a running process?
* Which command displays the status of a system service?
* How can you start or stop a service safely?

If you need assistance, refer to **`Solutions/Lab-08-Solution.md`**.

---

# Blue Team Insight

Monitoring processes and services is a daily responsibility for SOC analysts.

During incident response, analysts use process and service information to:

* Detect malware.
* Identify unauthorized applications.
* Discover persistence mechanisms.
* Investigate abnormal CPU or memory usage.
* Stop malicious processes before they cause further damage.

Understanding normal system behavior makes it easier to recognize suspicious activity.

---

# Challenge

Without using a search engine:

1. Identify the five processes using the most CPU resources.
2. Find the PID of a running process.
3. Start a simple background process and terminate it safely.
4. Check the status of the SSH service.
5. Restart a non-critical service.
6. Determine which services start automatically when the system boots.

---

# Reflection Questions

1. What is the difference between a process and a service?
2. Why is monitoring system resources important for Blue Teams?
3. How can attackers misuse background processes?
4. Why should analysts verify services running at startup?

---

# Key Takeaways

After completing this lab, you should be able to:

* Monitor Linux processes.
* Investigate process activity.
* Manage system services.
* Identify abnormal system behavior.
* Apply process analysis techniques during security investigations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in **`Solutions/Lab-08-Solution.md`**.

---

## Next Lab

Continue to **Lab 09 – Linux Networking**, where you will learn how to inspect network interfaces, verify connectivity, examine listening ports, and troubleshoot network communication from a Blue Team perspective.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2008%20Solution%20%E2%80%93%20Processes%20%26%20Services.md)**
