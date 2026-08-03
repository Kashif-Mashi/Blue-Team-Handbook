# Solution — Lab 08: Windows Event Viewer

> This solution guide walks you through the Brute-Force Attack Timeline Reconstruction scenario, demonstrating how to parse Security and System event logs to identify attacker IOCs and build a forensic timeline.

---

# Task 1 — Simulate the Attack Evidence

## Steps

Open Command Prompt as Administrator and generate the evidence.

```cmd
net user APT_Backdoor P@ssw0rd123! /add
net localgroup Administrators APT_Backdoor /add
sc create PersistenceSvc binPath= "C:\Windows\Temp\beacon.exe" start= auto
```

### Investigation Note
These three commands simulate the exact post-exploitation playbook an attacker would follow: create a backdoor account, escalate it to Administrator, and install a persistent service. Each of these actions generates a distinct event in the Windows logs.

---

# Task 2 — Open Event Viewer

## Steps

Press `Win + R`, type `eventvwr.msc`, press Enter.
Navigate to **Windows Logs → Security** in the left pane.

---

# Task 3 — Hunt for the Brute Force (Event ID 4625)

## Steps

1. Click **Filter Current Log** in the right-hand Actions pane.
2. In the "Event IDs" field, type `4625`.
3. Click OK.

### Investigation Note
In our simulation, you may see only a few 4625 events (from any recent failed logons on your machine). In a real brute-force attack, you would see dozens or hundreds of 4625 events in a short time window, all targeting the same account (usually `Administrator`).

Key fields to examine in each 4625 event:
- **Account Name**: The targeted account.
- **Failure Reason**: Usually "Unknown user name or bad password."
- **Source Network Address**: The attacker's IP.
- **Logon Type**: Type 3 (Network) or Type 10 (RDP).

---

# Task 4 — Find the Successful Logon (Event ID 4624)

## Steps

1. Clear the existing filter.
2. Apply a new filter for Event ID `4624`.
3. Find the most recent logon event.

### Investigation Note
Key fields to extract:
- **Logon Type**: Type 10 = RDP, Type 3 = Network (SMB/WinRM).
- **Source Network Address**: This is the attacker's IP address. Cross-reference this against the IPs seen in Event ID 4625 to confirm they're from the same source.
- **Account Name**: The compromised account.
- **Logon ID**: A hex identifier that links this logon session to all subsequent actions.

---

# Task 5 — Detect the Backdoor Account (Event ID 4720)

## Steps

Filter the Security log for Event ID `4720`.

### Example Output (Event Detail)

```
A user account was created.

Subject:
    Security ID:        DESKTOP-TRIAGE\JohnDoe
    Account Name:       JohnDoe

New Account:
    Security ID:        DESKTOP-TRIAGE\APT_Backdoor
    Account Name:       APT_Backdoor
```

### Investigation Note
The **Subject** section reveals WHO created the account. In our simulation, it was your own admin account. In a real attack, this tells you which compromised account the attacker was using to perform post-exploitation.

---

# Task 6 — Detect Privilege Escalation (Event ID 4732)

## Steps

Filter for Event ID `4732`.

### Example Output (Event Detail)

```
A member was added to a security-enabled local group.

Subject:
    Account Name:       JohnDoe

Member:
    Account Name:       APT_Backdoor

Group:
    Group Name:         Administrators
```

### Investigation Note
This is the privilege escalation step. The attacker added `APT_Backdoor` to the `Administrators` group. In a SOC environment, a SIEM rule should fire an alert whenever ANY non-domain-admin account is added to the local Administrators group.

---

# Task 7 — Detect the Persistence Service (Event ID 7045)

## Steps

Navigate to **Windows Logs → System**.
Filter for Event ID `7045`.

### Example Output (Event Detail)

```
A service was installed in the system.

Service Name:    PersistenceSvc
Service File Name: C:\Windows\Temp\beacon.exe
Service Type:    user mode service
Service Start Type: auto start
Service Account: LocalSystem
```

### Investigation Note
This is the persistence mechanism. Key red flags:
1. **Service File Name** points to `C:\Windows\Temp\` — no legitimate service binary lives in the Temp directory.
2. **Service Start Type** is `auto start` — the malware will survive reboots.
3. **Service Account** is `LocalSystem` — it runs with the highest privilege level on the host.

---

# Task 8 — PowerShell Timeline Construction

## Steps

```powershell
# Get account creation events
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720} -MaxEvents 5 |
    Select-Object TimeCreated, @{Name="NewAccount";Expression={$_.Properties[0].Value}}, @{Name="CreatedBy";Expression={$_.Properties[4].Value}}

# Get new service installations
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -MaxEvents 5 |
    Select-Object TimeCreated, @{Name="ServiceName";Expression={$_.Properties[0].Value}}, @{Name="ImagePath";Expression={$_.Properties[1].Value}}
```

### Example Output

```
TimeCreated           NewAccount      CreatedBy
-----------           ----------      ---------
8/2/2026 2:15:32 AM   APT_Backdoor    JohnDoe

TimeCreated           ServiceName     ImagePath
-----------           -----------     ---------
8/2/2026 2:17:45 AM   PersistenceSvc  C:\Windows\Temp\beacon.exe
```

### Investigation Note
By combining these timestamps, you can construct a clear attack timeline:
1. **02:00 - 02:15 AM**: Brute-force attack (Event ID 4625 × 47).
2. **02:15 AM**: Successful logon (Event ID 4624).
3. **02:15 AM**: Backdoor account created (Event ID 4720).
4. **02:16 AM**: Backdoor added to Administrators (Event ID 4732).
5. **02:17 AM**: Persistence service installed (Event ID 7045).

---

# Task 9 — Export Evidence

## Steps

```cmd
wevtutil epl Security C:\Evidence\Security_Export.evtx
```

### Investigation Note
Always export logs BEFORE performing any remediation. The exported `.evtx` file can be opened on any Windows machine using Event Viewer, or ingested into forensic tools like Chainsaw, EvtxEcmd, or Elastic.

---

# Task 10 — Clean Up

## Steps

```cmd
net user APT_Backdoor /delete
sc delete PersistenceSvc
```

---

# Scenario Conclusion

By systematically parsing Security and System event logs, you reconstructed the complete attacker kill chain: brute-force entry → account creation → privilege escalation → service persistence. This is the exact workflow a Tier 2 SOC Analyst follows during a real-world incident investigation, and the evidence you collected would be presented in the formal Incident Report to leadership.
