# Lab 07 — Windows Networking

## Scenario

Threat intelligence has identified a known Command and Control (C2) IP address (`198.51.100.45`) associated with a malware family called **DarkBeacon**. Your organization's IDS/IPS flagged outbound HTTPS traffic from workstation `WS-FINANCE-03` to this IP address every 60 seconds — a classic beaconing pattern.

As a SOC Analyst, you are assigned to investigate the endpoint. You must identify which process is establishing the C2 connection, determine if data is being exfiltrated, inspect the DNS cache for suspicious lookups, and use the Windows Firewall to block the attacker's infrastructure immediately.

---

# Mission

Use `netstat`, `Get-NetTCPConnection`, DNS tools, and Windows Firewall to isolate the rogue C2 connection, identify the responsible process, and block the exfiltration.

---

# Story

Your Tier 2 lead drops this in your lap:

> *"The IDS caught something big. `WS-FINANCE-03` is beaconing out to a known C2 address every minute, like clockwork. We think it's exfiltrating financial data. I need you on that box NOW. Find the process, find the connection, and block it at the host firewall before anything else leaks out."*

---

# Learning Objectives

After completing this lab, you will be able to:

* Enumerate active network connections and map them to responsible processes.
* Inspect the local DNS resolver cache for evidence of malicious domain lookups.
* Inspect and modify the Windows `hosts` file.
* Test network connectivity to specific TCP ports using PowerShell.
* Create Windows Firewall rules to block outbound C2 traffic.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 09 (Windows Networking Fundamentals).

---

# Clues

> **"C2 beacons show up as `ESTABLISHED` connections in `netstat`. The key is to match the remote IP + port back to a local Process ID (PID)."**

> **"The attacker's domain might still be sitting in the DNS cache even after the connection closes. Check `ipconfig /displaydns`."**

---

# Your Tasks

Complete the following tasks to investigate and contain the C2 beacon.

### Task 1 — Simulate the C2 Beacon
Before you can hunt it, you need to create the evidence. Open Command Prompt as Administrator.
Add a fake malicious domain entry to the local `hosts` file:
`echo 198.51.100.45 evil-c2-server.com >> C:\Windows\System32\drivers\etc\hosts`

Then, simulate a DNS lookup that populates the cache:
`nslookup evil-c2-server.com`

---

### Task 2 — Take a Snapshot of Active Connections
Run `netstat -ano` to see all active TCP/UDP sockets and their associated PIDs.
Look for any connections to the suspicious IP `198.51.100.45` or any unusual outbound connections on ports like 443, 4444, or 8080.

---

### Task 3 — Map Connections to Processes (PowerShell)
Use PowerShell for a more detailed view that includes process names:

```powershell
Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

Can you identify which process is responsible for the suspicious outbound connection?

---

### Task 4 — Inspect the DNS Cache
The attacker's malware resolved a domain name before connecting. That resolution might still be cached.
Run `ipconfig /displaydns` and search the output for any suspicious or unfamiliar domain entries.
Do you see `evil-c2-server.com` and the IP `198.51.100.45`?

---

### Task 5 — Investigate the hosts File
Sophisticated malware sometimes modifies the `hosts` file to redirect legitimate domains (e.g., Windows Update) to attacker-controlled servers.
Open the hosts file:
`type C:\Windows\System32\drivers\etc\hosts`
Look for any entries that should not be there.

---

### Task 6 — Test Port Connectivity
Use PowerShell to verify if the workstation can reach the C2 server:
`Test-NetConnection -ComputerName 198.51.100.45 -Port 443`
*(This will likely fail since the IP is fake, but the workflow is what matters. In a real scenario, a successful result confirms the firewall is NOT blocking the connection.)*

---

### Task 7 — Block the C2 at the Host Firewall
It's time to contain the threat. Create a Windows Firewall rule to block ALL outbound traffic to the C2 IP.

```cmd
netsh advfirewall firewall add rule name="BLOCK_C2_DarkBeacon" dir=out action=block remoteip=198.51.100.45
```

---

### Task 8 — Verify the Block
Confirm the firewall rule was created successfully.
Run: `netsh advfirewall firewall show rule name="BLOCK_C2_DarkBeacon"`

---

### Task 9 — Flush DNS and Clean the hosts File
Flush the poisoned DNS cache: `ipconfig /flushdns`
Edit the hosts file and remove the malicious entry you added in Task 1.

---

### Task 10 — Clean Up
Remove the firewall rule: `netsh advfirewall firewall delete rule name="BLOCK_C2_DarkBeacon"`

---

# Success Criteria

You have successfully completed this lab if you can:

* Use `netstat -ano` and `Get-NetTCPConnection` to identify active C2 connections and their PIDs.
* Find evidence of malicious DNS lookups in the resolver cache.
* Identify unauthorized modifications to the `hosts` file.
* Create and verify a Windows Firewall block rule against a known C2 IP.

---

# 💙 Blue Team Insight

In real-world incident response, blocking C2 at the host firewall is an emergency containment action. However, it is NOT sufficient on its own. The malware binary is still on disk, the persistence mechanism is still active, and lateral movement may have already occurred. Host firewall blocks buy you time while you perform full triage, memory acquisition, and disk imaging.

---

# Key Takeaways

After completing this lab, you should be able to:

* Perform network-level triage of a compromised endpoint using native Windows tools.
* Use DNS cache analysis as a forensic artifact during incident response.
* Rapidly contain threats at the host firewall layer.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2007%20Solution.md)**
