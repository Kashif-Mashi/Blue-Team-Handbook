# Lab 06 — Windows Processes & Services

## Scenario

A network monitoring alert triggered on `SRV-APP-01` indicating steady outbound traffic to an unknown IP address over port 4444. The system is also running noticeably slower than usual, and the CPU fans are spinning loudly. The SOC suspects a cryptominer or a persistent backdoor is running on the server.

As an Incident Responder, you are tasked with performing live process and service analysis on the endpoint to hunt down the anomalous process, identify any evasion techniques in use, and determine how the malware is persisting on the machine.

---

# Mission

Use native Windows utilities (`tasklist`, `wmic`, `sc.exe`) alongside Sysinternals `Process Explorer` to hunt down the evasive process, identify process hollowing or masquerading, and trace the parent-child lineage to locate the malicious service.

---

# Story

You get a ticket marked high severity:

> *"Server admin noticed `SRV-APP-01` CPU is pegged at 95%. Endpoint logs show a weird `svchost.exe` process making outbound connections. Find out what it is, where it started from, and shut it down before it spreads."*

You need to recreate the conditions, find the rogue process hiding in plain sight, and kill the backdoor service.

---

# Learning Objectives

After completing this lab, you will be able to:

* Enumerate running processes and services using native Windows CLI tools.
* Use Sysinternals Process Explorer to analyze process trees and parent-child relationships.
* Identify process masquerading and hollowing (e.g., malware hiding as `svchost.exe`).
* Map a running process to its associated Windows Service.
* Stop and delete persistent malicious background services.

---

# Prerequisites

Before starting this lab, ensure you have:

* A working Windows 10 or Windows 11 Workstation.
* Local Administrator privileges.
* Sysinternals Suite downloaded (specifically `procexp.exe`).
* Completed Chapter 08 (Windows Processes & Services).

---

# Clues

> **"Legitimate `svchost.exe` instances are ALWAYS launched by `services.exe` and ALWAYS reside in `C:\Windows\System32`. If you see an `svchost.exe` launched by `cmd.exe` or running from `C:\Temp`, it's malware."**

> **"Malware creates background services to guarantee it restarts every time the server reboots. You have to kill the process AND delete the service."**

---

# Your Tasks

Complete the following tasks to conduct the process hunt.

### Task 1 — Simulate the Compromise
You need to plant the backdoor to hunt it. Open Command Prompt as Administrator and simulate a malicious service that masquerades as a legitimate binary.
Run: 
`sc create UpdaterSvc binPath= "cmd.exe /c start /B C:\Windows\System32\notepad.exe"`
Start it:
`net start UpdaterSvc`
*(Note: We are using `notepad.exe` to safely simulate the "malware" process).*

---

### Task 2 — The Initial Hunt (CLI)
You know a process is acting strangely. Use the command line to see what's running.
Run `tasklist | findstr notepad.exe` to locate the PID of the simulated malware.

---

### Task 3 — Identify the Parent Process
Malware often has an anomalous parent. Let's trace its lineage using Windows Management Instrumentation (WMI).
Use `wmic process get processid, parentprocessid, name | findstr <PID>` (replace `<PID>` with the ID you found in Task 2) to find the Parent Process ID (PPID).

---

### Task 4 — Trace the Lineage
Look up the PPID you just found using `tasklist /fi "PID eq <PPID>"`.
What process spawned the "malware"? 

---

### Task 5 — Sysinternals Deep Dive
Command line is great, but GUI is faster for deep triage.
Launch **Process Explorer** (`procexp.exe`) as Administrator.
Locate the malicious `notepad.exe` in the process tree. Right-click it and select **Properties**.
Navigate to the **Image** tab. Note the "Current directory" and "Parent" fields. What do you see?

---

### Task 6 — Link the Process to the Persistence Mechanism
You need to find out *how* this process survives reboots. The alert mentioned a service.
In an Administrator Command Prompt, run:
`tasklist /svc`
Can you map the running processes to the services hosting them? 
*(Alternatively, use `Get-WmiObject win32_service | Where-Object {$_.Name -eq 'UpdaterSvc'}` in PowerShell to inspect the service).*

---

### Task 7 — Investigate the Rogue Service
Now that you suspect a service named `UpdaterSvc` is the persistence mechanism, query its configuration.
Run `sc query UpdaterSvc` and `sc qc UpdaterSvc`.
Look at the `BINARY_PATH_NAME`. This reveals the exact command the attacker used to launch the backdoor!

---

### Task 8 — Stop the Bleeding
First, terminate the active process to stop the immediate threat.
Run `taskkill /F /PID <PID>` (using the PID of the `notepad.exe` process).

---

### Task 9 — Eradicate the Persistence
Now, remove the malicious service so it doesn't restart.
Run `sc delete UpdaterSvc`.

---

# Success Criteria

You have successfully completed this lab if you can:

* Find a specific process ID using `tasklist` and `findstr`.
* Trace a process back to its parent using `wmic` or Process Explorer.
* Identify the service configuration and binary path of a persistent threat using `sc qc`.
* Successfully terminate a running process and delete its associated service.

---

# 💙 Blue Team Insight

Adversaries rely on **Process Masquerading**. They name their malware `svchost.exe`, `lsass.exe`, or `explorer.exe` to blend in. However, they cannot easily fake the **Process Lineage**. A true `svchost.exe` must be spawned by `services.exe`. A true `lsass.exe` must be spawned by `wininit.exe`. If you see `explorer.exe` spawning `svchost.exe`, you are looking at a compromised host.

---

# Key Takeaways

After completing this lab, you should be able to:

* Use CLI and GUI tools to analyze the process tree.
* Map suspicious processes to the services that launched them.
* Terminate active threats and eradicate their service-based persistence mechanisms.

---

## Need Help?

A complete walkthrough, command explanations, expected outputs, and troubleshooting tips are available in the **Solutions** directory.

---

# Solution

➡ **[View Solution](../Solution/Lab%2006%20Solution.md)**
