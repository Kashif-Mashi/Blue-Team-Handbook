# Lab 07 Solution — Windows Networking Investigation

## Solution

---

### Task 1: Complete IP Interface Audit via CMD

#### Step-by-Step Instructions
1. Open elevated CMD.
2. Run `ipconfig /all`.

#### Expected Output
```cmd
Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : localdomain
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection
   Physical Address. . . . . . . . . : 00-0C-29-88-AB-12
   DHCP Enabled. . . . . . . . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.50(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 1.1.1.1, 8.8.8.8
```

#### Explanation
Outputs IP configuration parameters required for network triage.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: PowerShell Network Adapter Inspection

#### Step-by-Step Instructions
1. Open PowerShell and run `Get-NetAdapter`.

#### Expected Output
```text
Name                      InterfaceDescription                    ifIndex Status       MacAddress         LinkSpeed
----                      --------------------                    ------- ------       ----------         ---------
Ethernet0                 Intel(R) Ethernet Connection                 12 Up           00-0C-29-88-AB-12     1 Gbps
```

#### Explanation
Displays physical network adapter properties, hardware MAC address, and link speed.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: ARP Cache Table Inspection

#### Step-by-Step Instructions
1. Run `arp -a` in CMD.

#### Expected Output
```cmd
Interface: 192.168.1.50 --- 0xc
  Internet Address      Physical Address      Type
  192.168.1.1           00-50-56-fe-11-22     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
```

#### Explanation
Shows local IP-to-MAC resolution entries used for Ethernet frame forwarding.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Active Network Connection Audit

#### Step-by-Step Instructions
1. Run `netstat -ano` in CMD.

#### Expected Output
```cmd
  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       940
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    192.168.1.50:49672     198.51.100.50:443      ESTABLISHED     4820
```

#### Explanation
Enumerates active network sockets, connection states, and associated Process IDs (PIDs).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Isolate Active ESTABLISHED Sockets

#### Step-by-Step Instructions
1. Run `netstat -ano | findstr "ESTABLISHED"` in CMD.

#### Expected Output
```cmd
  TCP    192.168.1.50:49672     198.51.100.50:443      ESTABLISHED     4820
```

#### Explanation
Filters socket listings to reveal active outbound connections and PID 4820.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Map Socket PIDs to Executable Binaries

#### Step-by-Step Instructions
1. Run `tasklist /FI "PID eq 4820"`.

#### Expected Output
```cmd
Image Name                   PID Session Name        Session#    Mem Usage
========================= ====== ================ ======== ============
cmd.exe                     4820 Console                 1      5,120 K
```

#### Explanation
Matches socket PID 4820 to its host binary (`cmd.exe`).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: PowerShell Socket & Process Correlation

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess
```

#### Expected Output
```text
LocalAddress LocalPort RemoteAddress  RemotePort OwningProcess
------------ --------- -------------  ---------- -------------
192.168.1.50     49672 198.51.100.50         443          4820
```

#### Explanation
`Get-NetTCPConnection` parses network socket objects programmatically.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Local DNS Resolver Cache Audit

#### Step-by-Step Instructions
1. Run `ipconfig /displaydns` in CMD.

#### Expected Output
```cmd
    Record Name . . . . . : cloudflare.com
    Record Type . . . . . : 1
    Time To Live  . . . . : 300
    Data Length . . . . . : 4
    Section . . . . . . . : Answer
    A (Host) Record . . . : 104.16.132.229
```

#### Explanation
Displays DNS records stored in the client cache memory.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Flush DNS Resolver Cache

#### Step-by-Step Instructions
1. Run `ipconfig /flushdns`.

#### Expected Output
```cmd
Successfully flushed the DNS Resolver Cache.
```

#### Explanation
Purges local DNS resolution entries to clear potential stale or poisoned DNS mappings.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Inspect Local `hosts` Override File

#### Step-by-Step Instructions
1. Run `type C:\Windows\System32\drivers\etc\hosts`.

#### Expected Output
```cmd
# Copyright (c) 1993-2009 Microsoft Corp.
#
127.0.0.1       localhost
::1             localhost
```

#### Explanation
Verifies that no static DNS overrides or redirection entries exist in the `hosts` file.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: Query DNS Records via `nslookup`

#### Step-by-Step Instructions
1. Run `nslookup cloudflare.com`.

#### Expected Output
```cmd
Server:  one.one.one.one
Address:  1.1.1.1

Non-authoritative answer:
Name:    cloudflare.com
Addresses:  104.16.132.229
          104.16.133.229
```

#### Explanation
Queries configured DNS servers for target domain IP records.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Test Specific Remote Port Connectivity

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Test-NetConnection -ComputerName 1.1.1.1 -Port 53
```

#### Expected Output
```text
ComputerName           : 1.1.1.1
RemoteAddress          : 1.1.1.1
RemotePort             : 53
InterfaceAlias         : Ethernet0
TcpTestSucceeded       : True
```

#### Explanation
Tests 3-way TCP handshake connectivity to port 53 (DNS).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Audit Windows Firewall Profile Status

#### Step-by-Step Instructions
1. Run `netsh advfirewall show allprofiles` in CMD.

#### Expected Output
```cmd
Domain Profile Settings:
----------------------------------------------------------------------
State                                 ON

Private Profile Settings:
----------------------------------------------------------------------
State                                 ON

Public Profile Settings:
----------------------------------------------------------------------
State                                 ON
```

#### Explanation
Confirms all three host firewall profiles are active.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Deploy Outbound Firewall Block Rule via `netsh`

#### Step-by-Step Instructions
1. Run in elevated CMD:
```cmd
netsh advfirewall firewall add rule name="Block_Malicious_C2" dir=out action=block remoteip=198.51.100.50
```

#### Expected Output
```cmd
Ok.
```

#### Explanation
Creates an outbound block rule isolating the host from C2 IP `198.51.100.50`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Clean Up Lab Firewall Rule

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
netsh advfirewall firewall delete rule name="Block_Malicious_C2"
```

#### Expected Output
```cmd
Deleted 1 rule(s).
Ok.
```

#### Explanation
Removes temporary firewall block rule from the policy database.

---

### Screenshot

> **Insert Screenshot Here**

---
