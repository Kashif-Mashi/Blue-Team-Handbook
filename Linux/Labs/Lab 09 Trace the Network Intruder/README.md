# Lab 09 – Linux Networking

## Scenario

The SOC has received multiple alerts indicating that a Linux server is communicating with unknown systems on the network. Before determining whether the activity is malicious, you must inspect the server's network configuration, verify connectivity, and identify active network connections.

As a Blue Team Analyst, your task is to investigate the system's network activity and ensure that only legitimate communication is taking place.

---

# Mission

Investigate the Linux network configuration, verify connectivity, identify active connections, and examine listening ports to establish a network baseline.

---

# Story

An automated monitoring system reports unusual outbound connections from one of your Linux servers.

Your team leader says:

> *"Every cyberattack leaves traces on the network. Before we hunt the attacker, we must understand how this system communicates with the outside world."*

Your mission is to investigate the server's network configuration and determine whether its activity appears normal.

---

# Learning Objectives

After completing this lab, you will be able to:

* View network interface information.
* Understand IP addressing.
* Verify network connectivity.
* Inspect routing information.
* Examine listening ports.
* Identify active network connections.
* Perform basic DNS lookups.
* Troubleshoot common network issues.

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

---

# Clues

> **"Every connection has two ends—find the other side."**

> **"Open ports are open doors. Know which ones should remain unlocked."**

> **"The network tells a story, but only if you know how to read it."**

---

# Your Tasks

Complete the following tasks using Linux networking commands.

### Task 1 – Identify Network Interfaces

Inspect the available network interfaces on your system.

Record:

* Interface names
* IPv4 and IPv6 addresses
* MAC addresses
* Interface status

---

### Task 2 – Verify Network Connectivity

Test connectivity to:

* Your default gateway
* Another device on your local network (if available)
* A public website or IP address

Record your observations.

---

### Task 3 – Investigate Network Configuration

Review your system's:

* IP address
* Default gateway
* DNS configuration
* Routing table

Document your findings.

---

### Task 4 – Inspect Listening Ports

Identify services currently listening for network connections.

Determine:

* Port number
* Protocol (TCP/UDP)
* Associated process

---

### Task 5 – Review Active Network Connections

Inspect all active network connections.

Identify:

* Local Address
* Remote Address
* Connection State
* Related Process

---

### Task 6 – Perform DNS Investigation

Resolve a domain name.

Verify:

* DNS server being used
* IP address returned
* Successful name resolution

---

### Task 7 – Verify SSH Connectivity

Confirm that SSH is installed and determine whether the SSH service is running.

If available, verify that the server can accept SSH connections.

---

### Task 8 – Create a Network Investigation Report

Prepare a report containing:

* Network interfaces
* IP configuration
* Routing information
* Open ports
* Active connections
* DNS observations
* Security recommendations

---

# Success Criteria

You have successfully completed this lab if you can:

* Identify network interfaces.
* Verify network connectivity.
* Explain your IP configuration.
* Inspect listening ports.
* Review active network sessions.
* Perform DNS lookups.
* Create a network investigation report.

---

# Hint

Think about the following before viewing the solution:

* Which command displays IP address information?
* How can you verify internet connectivity?
* Which command lists listening ports?
* How can you inspect active network connections?
* Which command resolves domain names?

If you need assistance, refer to **`Solutions/Lab-09-Solution.md`**.

---

# Blue Team Insight

Network analysis is one of the most important responsibilities of a Security Operations Center (SOC).

Blue Team analysts routinely:

* Detect unauthorized network connections.
* Identify suspicious listening services.
* Investigate command-and-control (C2) traffic.
* Troubleshoot connectivity issues.
* Validate firewall and network configurations.
* Establish normal network behavior to identify anomalies.

Understanding your system's network activity is essential for effective threat detection and incident response.

---

# Challenge

Without using a search engine:

1. Identify your system's IP address.
2. Determine your default gateway.
3. List all listening TCP and UDP ports.
4. Identify the process associated with one listening port.
5. Resolve a public domain name and record its IP address.
6. Verify that your system has internet connectivity.
7. Document all findings in a network investigation report.

---

# Reflection Questions

1. Why is it important to establish a network baseline?
2. How can open ports increase security risk?
3. Why should Blue Team analysts monitor active network connections?
4. How can DNS investigations assist during incident response?

---

# Key Takeaways

After completing this lab, you should be able to:

* Understand Linux networking fundamentals.
* Investigate network interfaces and IP configurations.
* Monitor active network connections.
* Identify listening services.
* Troubleshoot basic network issues.
* Apply network analysis techniques during Blue Team investigations.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, troubleshooting steps, and screenshots are available in **`Solutions/Lab-09-Solution.md`**.

---

## Next Lab

Continue to **Lab 10 – Logging & Monitoring**, where you will learn how to investigate Linux log files, monitor system events, and identify indicators of suspicious activity using built-in logging tools.


---

# Solution

➡ **[View Solution](../Solutions/Lab%2009%20Solution%20%E2%80%93%20Linux%20Networking.md)**
