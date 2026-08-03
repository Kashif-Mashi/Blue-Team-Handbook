# Solution — Lab 07: Windows Networking

> This solution guide walks you through the C2 Beacon Hunt scenario, demonstrating how to identify active malicious connections, analyze the DNS cache, and contain the threat using the Windows Firewall.

---

# Task 1 — Simulate the C2 Beacon

## Steps

Open Command Prompt as Administrator and plant the evidence.

```cmd
echo 198.51.100.45 evil-c2-server.com >> C:\Windows\System32\drivers\etc\hosts
nslookup evil-c2-server.com
```

### Investigation Note
Adding an entry to the `hosts` file forces the OS to resolve `evil-c2-server.com` to `198.51.100.45` without ever querying a DNS server. Real-world malware often modifies this file to redirect update servers or security vendor domains to attacker infrastructure.

---

# Task 2 — Take a Snapshot of Active Connections

## Steps

```cmd
netstat -ano
```

### Example Output (Excerpt)

```
Proto  Local Address          Foreign Address        State           PID
TCP    10.0.2.15:49734        198.51.100.45:443      ESTABLISHED     3456
TCP    10.0.2.15:49801        13.107.42.14:443       ESTABLISHED     1892
TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       892
```

### Investigation Note
In the output above, PID `3456` has an `ESTABLISHED` connection to the suspicious IP `198.51.100.45` on port `443`. In our simulation, you may not see this exact entry (since the fake IP isn't reachable), but in a live incident, this is exactly what the C2 beacon looks like: a steady outbound HTTPS connection to a known bad IP.

---

# Task 3 — Map Connections to Processes (PowerShell)

## Steps

```powershell
Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

### Investigation Note
This PowerShell command adds the crucial `ProcessName` column that `netstat` lacks. In a real scenario, if you see a process like `rundll32.exe` or an unknown binary connecting to the C2 IP, you have found your malware. The `OwningProcess` PID allows you to pivot to `tasklist`, `wmic`, or Process Explorer for deeper analysis.

---

# Task 4 — Inspect the DNS Cache

## Steps

```cmd
ipconfig /displaydns
```

### Example Output (Excerpt)

```
    evil-c2-server.com
    ----------------------------------------
    Record Name . . . . . : evil-c2-server.com
    Record Type . . . . . : 1
    Time To Live  . . . . : 86400
    Data Length . . . . . : 4
    Section . . . . . . . : Answer
    A (Host) Record . . . : 198.51.100.45
```

### Investigation Note
Even if the C2 connection has closed, the DNS cache retains the lookup. This is a critical forensic artifact proving that the host resolved a known-malicious domain. In production, forward this evidence to your Threat Intel team to correlate with IOC feeds.

---

# Task 5 — Investigate the hosts File

## Steps

```cmd
type C:\Windows\System32\drivers\etc\hosts
```

### Example Output (Excerpt)

```
# Copyright (c) 1993-2009 Microsoft Corp.
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost

198.51.100.45 evil-c2-server.com
```

### Investigation Note
The malicious entry at the bottom is clearly not a default Windows entry. In sophisticated attacks, the `hosts` file is modified to:
- Redirect `windowsupdate.microsoft.com` to a fake server (preventing patches).
- Redirect AV vendor domains to `127.0.0.1` (disabling cloud signature updates).
- Force DNS resolution of a domain to an attacker-controlled IP without touching DNS infrastructure.

---

# Task 6 — Test Port Connectivity

## Steps

```powershell
Test-NetConnection -ComputerName 198.51.100.45 -Port 443
```

### Investigation Note
In our lab, this will likely return `TcpTestSucceeded : False` since the IP is not routable. In a real scenario, a result of `TcpTestSucceeded : True` proves the endpoint can still reach the C2 server, confirming no firewall or proxy is currently blocking the connection.

---

# Task 7 — Block the C2 at the Host Firewall

## Steps

```cmd
netsh advfirewall firewall add rule name="BLOCK_C2_DarkBeacon" dir=out action=block remoteip=198.51.100.45
```

### Expected Output

```
Ok.
```

### Investigation Note
This creates an outbound block rule that prevents ANY process on the host from connecting to `198.51.100.45`. This is your first containment action. Even if the malware tries to beacon again, the traffic will be silently dropped at the host level.

---

# Task 8 — Verify the Block

## Steps

```cmd
netsh advfirewall firewall show rule name="BLOCK_C2_DarkBeacon"
```

### Example Output

```
Rule Name:                            BLOCK_C2_DarkBeacon
----------------------------------------------------------------------
Enabled:                              Yes
Direction:                            Out
Profiles:                             Domain,Private,Public
Action:                               Block
RemoteIP:                             198.51.100.45/32
```

### Investigation Note
Confirm that `Enabled: Yes`, `Direction: Out`, `Action: Block`, and `RemoteIP` matches the C2 address. The rule applies across all firewall profiles (Domain, Private, Public).

---

# Task 9 — Flush DNS and Clean the hosts File

## Steps

Flush the poisoned DNS cache:

```cmd
ipconfig /flushdns
```

Edit the hosts file and remove the malicious entry. Open it in Notepad as Administrator:

```cmd
notepad C:\Windows\System32\drivers\etc\hosts
```

Delete the line `198.51.100.45 evil-c2-server.com` and save.

### Investigation Note
Flushing DNS prevents the compromised host from continuing to resolve the malicious domain from cache. Cleaning the hosts file restores normal DNS resolution behavior.

---

# Task 10 — Clean Up

## Steps

Remove the firewall rule:

```cmd
netsh advfirewall firewall delete rule name="BLOCK_C2_DarkBeacon"
```

---

# Scenario Conclusion

By using `netstat`, PowerShell, and DNS cache analysis, you successfully identified the C2 beacon, traced it to its responsible process, and implemented an immediate firewall containment rule. In a real-world SOC, this rapid triage buys the incident response team time to collect forensic artifacts, analyze malware samples, and coordinate a full remediation effort.
