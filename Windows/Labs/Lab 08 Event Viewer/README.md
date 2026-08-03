# Lab 08 — Windows Event Viewer

## Scenario

The SOC received an alert from the SIEM: a burst of **47 failed logon attempts** (Event ID 4625) against the `Administrator` account on server `DC-PROD-01` occurred between 02:00 AM and 02:15 AM on Saturday, immediately followed by a **single successful logon** (Event ID 4624). Minutes later, a **new service was installed** (Event ID 7045) and a **new user account was created** (Event ID 4720).

This pattern is consistent with a brute-force attack followed by post-exploitation persistence. As a Tier 2 SOC Analyst, you must use Event Viewer and PowerShell to reconstruct the attack timeline, identify the attacker's source IP, and determine what persistence mechanisms were deployed.

---

# Mission

Use Event Viewer (`eventvwr.msc`) and PowerShell (`Get-WinEvent`) to parse the Security and System event logs, reconstruct the attacker's kill chain, and identify all indicators of compromise (IOCs).

---

# Story

The incident commander briefs you:

> *"Someone brute-forced the admin account on our production DC over the weekend. They got in, they created a backdoor account, and they installed a service. I need you to pull the logs, build the timeline, and tell me: what IP did they come from, what account did they create, and what service did they install. The board is asking questions."*

---

# Learning Objectives

After completing this lab, you will be able to:

* Navigate the Windows Event Viewer GUI and filter for specific Event IDs.
* Use PowerShell `Get-WinEvent` with `FilterHashtable` to query structured event data.
* Interpret Security Event IDs 4624, 4625, 4720, 4732, and 7045.
* Extract attacker IOCs (source IP, account names, service paths) from event log properties.
* Export event logs to `.evtx` files for offline forensic analysis.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Completed Chapter 10 (Windows Event Viewer & Logging).

---

# Clues

> **"Event ID 4625 contains the source IP of the failed logon in the `Properties[19]` field. Cross-reference this IP against all successful logons (4624) to confirm the attacker's pivot."**

> **"Event ID 7045 only fires once when a service is FIRST installed. If you see a 7045 at 02:17 AM on a Saturday morning, it was NOT an IT admin."**

---

# Your Tasks

Complete the following tasks to reconstruct the attack timeline.

### Task 1 — Simulate the Attack Evidence
Open Command Prompt as Administrator. Generate evidence that simulates the attacker's post-exploitation activity:

Create a backdoor account:
`net user APT_Backdoor P@ssw0rd123! /add`

Add the account to Administrators:
`net localgroup Administrators APT_Backdoor /add`

Create a persistence service:
`sc create PersistenceSvc binPath= "C:\Windows\Temp\beacon.exe" start= auto`

---

### Task 2 — Open Event Viewer
Launch Event Viewer by pressing `Win + R`, typing `eventvwr.msc`, and pressing Enter.
Navigate to **Windows Logs → Security**.

---

### Task 3 — Hunt for the Brute Force (Event ID 4625)
In the Security log, click **Filter Current Log** on the right pane. Enter `4625` in the Event ID field.
How many failed logon attempts do you see? What account was targeted?

---

### Task 4 — Find the Successful Logon (Event ID 4624)
Clear the filter and create a new one for Event ID `4624`.
Find the successful logon event that occurred AFTER the failed logon burst. Note:
- The **Logon Type** (Type 3 = Network, Type 10 = RDP).
- The **Source Network Address** (this is the attacker's IP).
- The **Account Name**.

---

### Task 5 — Detect the Backdoor Account (Event ID 4720)
Filter for Event ID `4720` (A user account was created).
Find the event showing the creation of `APT_Backdoor`. Note the **Subject** field — this tells you which account created the backdoor.

---

### Task 6 — Detect Privilege Escalation (Event ID 4732)
Filter for Event ID `4732` (A member was added to a security-enabled local group).
Find the event showing `APT_Backdoor` being added to the `Administrators` group.

---

### Task 7 — Detect the Persistence Service (Event ID 7045)
Switch to **Windows Logs → System**.
Filter for Event ID `7045` (A service was installed in the system).
Find the `PersistenceSvc` entry. Note the `ImagePath` — this is the malware binary location.

---

### Task 8 — PowerShell Timeline Construction
Use PowerShell to build a comprehensive attack timeline:

```powershell
# Get account creation events
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720} -MaxEvents 5 |
    Select-Object TimeCreated, @{Name="NewAccount";Expression={$_.Properties[0].Value}}, @{Name="CreatedBy";Expression={$_.Properties[4].Value}}

# Get new service installations
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -MaxEvents 5 |
    Select-Object TimeCreated, @{Name="ServiceName";Expression={$_.Properties[0].Value}}, @{Name="ImagePath";Expression={$_.Properties[1].Value}}
```

---

### Task 9 — Export Evidence
Export the Security log to a file for your incident report:
`wevtutil epl Security C:\Evidence\Security_Export.evtx`

---

### Task 10 — Clean Up
Remove the simulated attack artifacts:

```cmd
net user APT_Backdoor /delete
sc delete PersistenceSvc
```

---

# Success Criteria

You have successfully completed this lab if you can:

* Filter the Security log for specific Event IDs using Event Viewer GUI.
* Extract the attacker's source IP from Event ID 4624 properties.
* Identify backdoor account creation via Event ID 4720.
* Identify persistent service installation via Event ID 7045.
* Use `Get-WinEvent` with `FilterHashtable` to programmatically query events.

---

# 💙 Blue Team Insight

In a real-world SOC, you would never rely on manually checking Event Viewer. These events would be **forwarded to a SIEM** (Splunk, Elastic, Microsoft Sentinel) where automated detection rules fire alerts. For example:
- **Brute Force Rule**: Alert when > 10 Event ID 4625 events occur for the same account within 5 minutes.
- **New Service Rule**: Alert when Event ID 7045 fires outside of maintenance windows.
- **Account Creation Rule**: Alert when Event ID 4720 fires and the new account is immediately added to `Administrators` (4732).

---

# Key Takeaways

After completing this lab, you should be able to:

* Navigate the Windows Event Viewer and filter by Event ID.
* Extract critical attacker IOCs from structured event log fields.
* Construct an incident timeline using PowerShell event queries.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2008%20Solution.md)**
