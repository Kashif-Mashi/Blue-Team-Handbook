# Chapter 10 – Linux Networking Basics

## Learning Objectives

By the end of this chapter, you will be able to:

* Understand basic networking concepts in Linux.
* Identify network interfaces and their purpose.
* Understand IPv4 and IPv6 addressing.
* Learn how Linux communicates over a network.
* Configure and inspect network settings.
* Understand DNS and routing basics.
* Use common Linux networking commands.
* Apply networking knowledge to troubleshooting and cybersecurity.

---

# Introduction

Networking allows computers to communicate and exchange information.

Whether you are browsing a website, downloading updates, connecting through SSH, or monitoring network traffic in a SOC, networking is involved.

Linux provides powerful networking tools that allow administrators and security professionals to inspect, troubleshoot, and manage network connections directly from the command line.

Understanding Linux networking is a fundamental skill for system administrators, penetration testers, and SOC analysts.

---

# What is a Network?

A **network** is a collection of computers and devices connected together to share information and resources.

Examples include:

* Home Wi-Fi network
* Office network
* University campus network
* The Internet

---

# Types of Networks

| Network Type                    | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| LAN (Local Area Network)        | Covers a small area such as a home, office, or school.             |
| MAN (Metropolitan Area Network) | Covers a city or metropolitan region.                              |
| WAN (Wide Area Network)         | Covers large geographical areas, connecting cities or countries.   |
| Internet                        | The world's largest public network connecting millions of devices. |

---

# How Communication Happens

When your computer communicates with another device, data travels through several layers.

```text
Application
      │
      ▼
Transport Layer
      │
      ▼
Internet Layer
      │
      ▼
Network Interface
      │
      ▼
Physical Network
```

Linux uses the TCP/IP protocol suite to perform this communication.

---

# What is an IP Address?

An **IP Address (Internet Protocol Address)** uniquely identifies a device on a network.

It allows devices to send and receive data correctly.

Example:

```text
192.168.1.10
```

Without an IP address, a computer cannot communicate over a network.

---

# IPv4 Address

IPv4 is the most commonly used version of the Internet Protocol.

Example:

```text
192.168.10.15
```

IPv4 addresses are **32 bits** long and are written as four decimal numbers separated by periods.

Example Structure:

```text
192 . 168 . 10 . 15
```

Each section is called an **octet** and ranges from **0 to 255**.

---

# IPv6 Address

IPv6 was developed to overcome the limitations of IPv4.

Example:

```text
2001:db8:85a3::8a2e:370:7334
```

IPv6 addresses are **128 bits** long and provide a much larger address space.

---

# Public vs Private IP Address

| Public IP                    | Private IP                            |
| ---------------------------- | ------------------------------------- |
| Accessible from the Internet | Used inside local networks            |
| Assigned by an ISP           | Assigned by a router or administrator |
| Must be globally unique      | Can be reused in different networks   |

Common private IPv4 ranges:

```text
10.0.0.0/8

172.16.0.0 – 172.31.255.255

192.168.0.0/16
```

---

# What is a Network Interface?

A **network interface** is the connection point that allows a computer to communicate with a network.

Examples:

* Ethernet
* Wi-Fi
* Virtual Network Interface
* Loopback Interface

Example interface names:

```text
eth0

ens33

wlan0

lo
```

---

# Loopback Interface

The **loopback interface** represents the local computer.

It allows the system to communicate with itself.

Interface Name:

```text
lo
```

Loopback Address:

```text
127.0.0.1
```

This address is commonly called **localhost**.

---

# What is DNS?

DNS (Domain Name System) translates human-readable domain names into IP addresses.

Example:

```text
www.google.com

↓

142.250.x.x
```

Without DNS, users would need to remember IP addresses instead of domain names.

---

# What is a Gateway?

A **gateway** connects one network to another.

Most home networks use a router as the default gateway.

Example:

```text
Computer
      │
      ▼
Router (Gateway)
      │
      ▼
Internet
```

---

# What is Routing?

Routing is the process of determining the best path for data to travel between networks.

Routers maintain **routing tables** that help forward packets to their destinations.

---

# Command: ip

## Purpose

Displays and configures network interfaces, IP addresses, and routing information.

---

## Display Network Interfaces

```bash
ip addr
```

Example Output:

```text
2: ens33
    inet 192.168.1.105/24
```

---

## Display Routing Table

```bash
ip route
```

Example Output:

```text
default via 192.168.1.1 dev ens33
```

---

## Display Link Information

```bash
ip link
```

Displays all available network interfaces.

---

# Command: ping

## Purpose

Tests network connectivity between two devices.

---

## Syntax

```bash
ping hostname
```

Example:

```bash
ping google.com
```

Example Output:

```text
64 bytes from google.com:
```

Press:

```text
Ctrl + C
```

to stop the command.

Common Uses:

* Verify Internet connectivity.
* Test communication with another host.
* Measure response time.

---

# Command: ss

## Purpose

Displays network sockets and active connections.

---

## Syntax

```bash
ss
```

Useful Options:

Display listening ports:

```bash
ss -l
```

Display TCP connections:

```bash
ss -t
```

Display UDP connections:

```bash
ss -u
```

Display all listening TCP ports:

```bash
ss -tuln
```
---

# Command: netstat

## Purpose

Displays network connections, routing tables, and interface statistics.

---

## Syntax

```bash
netstat -tuln
```

> **Note:** On many modern Linux distributions, `ss` is recommended instead of `netstat`.

---

# Command: curl

## Purpose

Transfers data to or from a server.

---

## Syntax

```bash
curl URL
```

Example:

```bash
curl https://example.com
```

Common Uses:

* Download web content.
* Test APIs.
* Check web server responses.
* Troubleshoot HTTP services.

---

# Command: wget

## Purpose

Downloads files from the Internet.

---

## Syntax

```bash
wget URL
```

Example:

```bash
wget https://example.com/file.zip
```

Unlike `curl`, `wget` is designed primarily for downloading files.

---

# Command: traceroute

## Purpose

Displays the path packets take to reach a destination.

---

## Syntax

```bash
traceroute google.com
```

Each hop represents a router between your system and the destination.

---

# Command: dig

## Purpose

Queries DNS servers for information about domain names.

---

## Syntax

```bash
dig google.com
```

Useful Information:

* IP Address
* DNS Server
* Response Time
* Record Type

---

# Command: nslookup

## Purpose

Looks up DNS information for a domain.

---

## Syntax

```bash
nslookup google.com
```

Example Output:

```text
Name: google.com
Address: 142.250.x.x
```

---

# Command: ssh

## Purpose

Securely connects to a remote Linux system.

SSH stands for **Secure Shell**.

---

## Syntax

```bash
ssh username@hostname
```

Example:

```bash
ssh kashif@192.168.1.100
```

SSH encrypts communication between the client and the remote server.

---

# Common Networking Workflow

```text
Application
      │
      ▼
DNS Resolution
      │
      ▼
Destination IP Found
      │
      ▼
Routing Decision
      │
      ▼
Packets Sent Through Network Interface
      │
      ▼
Remote Server Responds
```

---

# Blue Team Perspective

Networking is one of the most important areas for SOC analysts.

Security teams regularly investigate:

* Suspicious outbound connections.
* Unexpected listening ports.
* Failed SSH login attempts.
* DNS requests to malicious domains.
* Unauthorized remote access.
* Network service availability.

Common commands used during investigations include:

* `ip`
* `ss`
* `ping`
* `curl`
* `dig`
* `journalctl`
* `ssh`

Understanding these tools helps analysts quickly identify connectivity issues and potential security threats.

---

# Common Mistakes

* Confusing public and private IP addresses.
* Ignoring firewall rules when troubleshooting connectivity.
* Leaving unnecessary services listening on open ports.
* Assuming DNS is working without verification.
* Using insecure protocols instead of SSH.

---

# Best Practices

* Use SSH instead of Telnet for remote administration.
* Regularly review open ports using `ss -tuln`.
* Verify DNS resolution before troubleshooting applications.
* Keep unnecessary network services disabled.
* Monitor network connections for unusual activity.

---

# Chapter Summary

In this chapter, you learned:

* Basic networking concepts.
* IPv4 and IPv6 addressing.
* Public and private IP addresses.
* Network interfaces.
* DNS and routing fundamentals.
* How to use `ip`, `ping`, `ss`, `curl`, `wget`, `traceroute`, `dig`, `nslookup`, and `ssh`.
* Networking best practices for Linux administration and cybersecurity.

---

# Interview Questions

1. What is an IP address?
2. What is the difference between IPv4 and IPv6?
3. What is the purpose of DNS?
4. What is a network interface?
5. What does the `ip addr` command display?
6. What is the difference between `curl` and `wget`?
7. What is the purpose of the `ss` command?
8. Why is SSH preferred over Telnet?
9. What does `traceroute` do?
10. Why is networking knowledge important for a SOC analyst?

---

# References

* Linux man pages — https://man7.org/linux/man-pages/
* Ubuntu Documentation — https://help.ubuntu.com/
* RFC 791 – Internet Protocol (IPv4)
* RFC 8200 – Internet Protocol Version 6 (IPv6)

---
