# Lab 12 — PowerShell Scripting Basics

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 14 (PowerShell Scripting Basics).  
**Objectives**:
- Write and run a basic `.ps1` script.
- Use comments, variables, and a `param()` block.
- Define and call a function.
- Add `if`/`else` decision-making to a script.
- Add a `foreach` loop to a script.
- Combine these elements into one reusable security-check script.

---

## Scenario

Your team lead wants junior analysts to stop manually re-typing the same Defender and Firewall checks from Chapter 11 every time they triage a machine. Your task is to build a small, reusable PowerShell script that automates those checks — starting simple, and adding one new scripting concept at a time.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Tools Used**: PowerShell, a text editor (Notepad or VS Code)

---

## Tasks

### Task 1: Write a Script with a Comment and a Variable
Create a file named `Hello.ps1` containing a comment explaining its purpose, a variable storing the computer name (`$env:COMPUTERNAME`), and a line that prints it with `Write-Host`.

### Task 2: Run the Script
Navigate to the script's folder and run it using `.\Hello.ps1`.

### Task 3: Add a Parameter
Modify the script to accept a `-Greeting` parameter (a string) using a `param()` block, and use it in the `Write-Host` line instead of a hardcoded greeting.

### Task 4: Define a Function
Create a new script, `DefenderCheck.ps1`, containing a function named `Get-DefenderSummary` that runs `Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled`.

### Task 5: Call the Function
Add a line at the bottom of the script that calls `Get-DefenderSummary`, then run the script.

### Task 6: Add an if/else Check
Extend `DefenderCheck.ps1` to check the Firewall's Public profile status and print a green message if it's enabled, or a red warning if it's not, using `if`/`else`.

### Task 7: Add a foreach Loop
Add a `foreach` loop that checks the status of three services: `WinDefend`, `wuauserv`, and `mpssvc`.

### Task 8: Combine Everything into One Script
Combine Tasks 4–7 into a single script named `SecurityCheck.ps1`, including a `-Detailed` switch parameter that additionally runs `Get-MpThreatDetection` when present.

---

## Verification

To verify success:
- Confirm `Hello.ps1` runs and prints the greeting with the computer name.
- Confirm `DefenderCheck.ps1` prints Defender status, the firewall if/else message, and the foreach service loop results.
- Confirm `SecurityCheck.ps1` behaves differently when run with and without `-Detailed`.

---

## Blue Team Notes

- **From One-Off Commands to Reusable Tools**: This lab mirrors exactly how real SOC tooling starts — a manual check gets scripted once it's clear it will be repeated.
- **Readable Scripts Are Safer Scripts**: A well-commented script with clear parameter names is easier for a teammate (or your future self) to trust and reuse without re-checking every line.

---

## Common Errors

- **Forgetting `.\` when running a script**: PowerShell may not run a local script without this prefix.
- **Missing `param()` at the very top**: The `param()` block must be the first executable line in a script (comments above it are fine).
- **Confusing a switch parameter with a string parameter**: A switch parameter (`[switch]$Detailed`) doesn't take a value — you either include `-Detailed` or you don't.

---

## MITRE ATT&CK Mapping

- **T1059.001**: Command and Scripting Interpreter: PowerShell

---

## Challenge Section

1. Add a fourth check to `SecurityCheck.ps1` that verifies BitLocker status, reusing the command from Chapter 11.
2. Modify the `foreach` loop from Task 7 so it also prints whether each service's `StartType` is `Automatic`.
3. Add a `-ComputerName` parameter to `SecurityCheck.ps1` (even if you don't fully implement remote checking) and explain what would need to change to support running it against a remote machine.
4. Explain, in your own words, why a script like `SecurityCheck.ps1` is more trustworthy to run against a real machine than a script you found online with no comments.