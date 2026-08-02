# Lab 07 — Windows Networking Investigation

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 09 (Windows Networking Fundamentals).  
**Objectives**:
- Enumerate host IP configurations, interface properties, and routing tables.
- Analyze active TCP/UDP network connections and map sockets to active processes.
- Inspect, query, and flush local DNS resolver cache and host files.
- Test remote socket connectivity using `Test-NetConnection`.
- Audit Windows Firewall profiles and deploy custom command-line firewall block rules.

---

## Scenario

A network intrusion detection system (NIDS) flagged suspicious outbound beaconing from workstation `WORKSTATION-03` to an external IP address.

As a Tier 1 SOC Analyst, you are assigned to investigate endpoint socket activity, map network connection PIDs to active processes on disk, inspect the local DNS cache for malicious domain queries, test socket connectivity, and configure Windows Firewall rules to isolate the host from the malicious IP address.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: `ipconfig`, `netstat`, `arp`, `nslookup`, `netsh`, `powershell.exe`

---

## Tasks

### Task 1: Complete IP Interface Audit via CMD
Open an elevated Command Prompt and execute `ipconfig /all` to record adapter names, IPv4 addresses, subnet masks, default gateways, and DNS servers.

### Task 2: PowerShell Network Adapter Inspection
Run `Get-NetAdapter` in PowerShell to check link status, interface speed, and MAC addresses.

### Task 3: ARP Cache Table Inspection
Run `arp -a` in CMD to view current IP-to-MAC address resolution mappings.

### Task 4: Active Network Connection Audit
Execute `netstat -ano` to list all active network connections, listening ports, and associated Process IDs (PIDs).

### Task 5: Isolate Active ESTABLISHED Sockets
Filter `netstat` output using `findstr "ESTABLISHED"` to list foreign IP addresses and open socket PIDs.

### Task 6: Map Socket PIDs to Executable Binaries
Use `tasklist /FI "PID eq <PID>"` to identify the exact executable name corresponding to an active socket PID found in Task 5.

### Task 7: PowerShell Socket & Process Correlation
Use PowerShell (`Get-NetTCPConnection -State Established`) to display local IP, local port, remote IP, remote port, and process name in a single formatted table.

### Task 8: Local DNS Resolver Cache Audit
Run `ipconfig /displaydns` to view recently resolved hostnames and IP records stored in memory.

### Task 9: Flush DNS Resolver Cache
Run `ipconfig /flushdns` to clear local DNS entries.

### Task 10: Inspect Local `hosts` Override File
Navigate to `C:\Windows\System32\drivers\etc` and inspect the `hosts` file using `type hosts`.

### Task 11: Query DNS Records via `nslookup`
Run `nslookup cloudflare.com` to test external domain name resolution.

### Task 12: Test Specific Remote Port Connectivity
Use PowerShell `Test-NetConnection -ComputerName 1.1.1.1 -Port 53` to verify TCP port accessibility.

### Task 13: Audit Windows Firewall Profile Status
Run `netsh advfirewall show allprofiles` to verify state (ON/OFF) for Domain, Private, and Public profiles.

### Task 14: Deploy Outbound Firewall Block Rule via `netsh`
Execute `netsh advfirewall firewall add rule name="Block_Malicious_C2" dir=out action=block remoteip=198.51.100.50` to isolate the host from a C2 IP.

### Task 15: Clean Up Lab Firewall Rule
Delete the test firewall rule using `netsh advfirewall firewall delete rule name="Block_Malicious_C2"`.

---

## Verification

To verify success:
- Confirm `netstat -ano` successfully maps active TCP connections to valid PIDs.
- Confirm `netsh advfirewall firewall show rule name="Block_Malicious_C2"` displays `Action: Block` before deletion.
- Confirm `ipconfig /flushdns` returns `Successfully flushed the DNS Resolver Cache`.

---

## Blue Team Notes

- **Network Socket Correlation**: Finding an ESTABLISHED connection in `netstat` is only half the job. Responders must map the PID to a process name, inspect the process binary path, and check digital signatures to confirm or rule out malware.
- **Host Isolation via Firewall**: In the absence of an EDR isolation feature, creating an outbound block-all firewall rule allows emergency host isolation while preserving live incident response access.

---

## Common Errors

- **Misinterpreting `127.0.0.1` Connections**: Local loopback connections (`127.0.0.1` or `::1`) represent internal inter-process communication, NOT external network threats.
- **Forgetting Administrator Elevation**: Commands modifying firewall rules (`netsh advfirewall`) fail without elevated rights.

---

## MITRE ATT&CK Mapping

- **T1049**: System Network Connections Discovery
- **T1016**: System Network Configuration Discovery
- **T1071.001**: Application Layer Protocol: Web Protocols
- **T1562.004**: Impair Defenses: Disable or Modify System Firewall

---

## Challenge Section

1. Write a PowerShell one-liner that lists all listening TCP ports and the service or process name owning each port.
2. Query Sysmon Event ID **3** in the Operational log using `Get-WinEvent` to find all outbound connections created by `powershell.exe`.
3. Create an inbound Windows Firewall rule via PowerShell (`New-NetFirewallRule`) blocking port `445` (SMB).
4. Perform a `tracert` to a public IP and identify all intermediate network hops.
5. Inspect active DNS cache entries and pipe the results to `Select-String` to look for specific domain suffixes.


---

# Solution

➡ **[View Solution](../Solution/Lab%2007%20Solution.md)**
