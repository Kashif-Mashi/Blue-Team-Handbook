# Lab 12 Solution — PowerShell Scripting Basics

## Solution

---

### Task 1: Write a Script with a Comment and a Variable

#### Step-by-Step Instructions
1. Open Notepad or VS Code.
2. Create a new file named `Hello.ps1` with the following content:
```powershell
# Hello.ps1 - A simple script that greets the current computer
$computerName = $env:COMPUTERNAME
Write-Host "Hello from $computerName!"
```
3. Save the file.

#### Expected Output
```text
(File created — no console output yet)
```

#### Explanation
The comment documents the script's purpose; `$computerName` stores a reusable value read from an environment variable.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Run the Script

#### Step-by-Step Instructions
1. Open PowerShell and navigate to the script's folder, e.g. `cd C:\Lab`.
2. Run `.\Hello.ps1`.

#### Expected Output
```text
Hello from WORKSTATION-07!
```

#### Explanation
The `.\` prefix tells PowerShell to run the script from the current folder.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Add a Parameter

#### Step-by-Step Instructions
1. Modify `Hello.ps1`:
```powershell
# Hello.ps1 - Greets the current computer with a custom message
param(
    [string]$Greeting = "Hello"
)

$computerName = $env:COMPUTERNAME
Write-Host "$Greeting from $computerName!"
```
2. Run `.\Hello.ps1 -Greeting "Good morning"`.

#### Expected Output
```text
Good morning from WORKSTATION-07!
```

#### Explanation
The `param()` block lets whoever runs the script customize its behavior without editing the file itself.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Define a Function

#### Step-by-Step Instructions
1. Create `DefenderCheck.ps1`:
```powershell
# DefenderCheck.ps1 - Reports Defender status
function Get-DefenderSummary {
    Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
}
```
2. Save the file.

#### Expected Output
```text
(File created — the function is defined but not yet called)
```

#### Explanation
Defining a function doesn't run it — it just makes it available to call later, as done in the next task.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Call the Function

#### Step-by-Step Instructions
1. Add this line to the bottom of `DefenderCheck.ps1`:
```powershell
Get-DefenderSummary
```
2. Run `.\DefenderCheck.ps1`.

#### Expected Output
```text
AntivirusEnabled RealTimeProtectionEnabled
---------------- -------------------------
            True                      True
```

#### Explanation
Calling the function by name executes the code inside it.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Add an if/else Check

#### Step-by-Step Instructions
1. Add this to `DefenderCheck.ps1`, below the function call:
```powershell
$firewallStatus = Get-NetFirewallProfile -Profile Public

if ($firewallStatus.Enabled -eq $true) {
    Write-Host "[+] Public firewall profile is enabled." -ForegroundColor Green
} else {
    Write-Host "[!] WARNING: Public firewall profile is disabled!" -ForegroundColor Red
}
```
2. Run the script.

#### Expected Output
```text
[+] Public firewall profile is enabled.
```

#### Explanation
The `if`/`else` block prints a different message depending on the actual firewall state.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Add a foreach Loop

#### Step-by-Step Instructions
1. Add this to the bottom of `DefenderCheck.ps1`:
```powershell
$servicesToCheck = @("WinDefend", "wuauserv", "mpssvc")

foreach ($service in $servicesToCheck) {
    Get-Service -Name $service | Select-Object Name, Status
}
```
2. Run the script.

#### Expected Output
```text
Name       Status
----       ------
WinDefend  Running
wuauserv   Running
mpssvc     Running
```

#### Explanation
The loop repeats the same `Get-Service` check once for each entry in the list, avoiding repeated code.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Combine Everything into One Script

#### Step-by-Step Instructions
1. Create `SecurityCheck.ps1`:
```powershell
# SecurityCheck.ps1
# Combines Defender, Firewall, and Service checks into one reusable script

param(
    [switch]$Detailed
)

function Get-DefenderSummary {
    Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
}

Write-Host "=== Defender Status ===" -ForegroundColor Cyan
Get-DefenderSummary

Write-Host "`n=== Firewall Status ===" -ForegroundColor Cyan
$firewallStatus = Get-NetFirewallProfile -Profile Public
if ($firewallStatus.Enabled -eq $true) {
    Write-Host "[+] Public firewall profile is enabled." -ForegroundColor Green
} else {
    Write-Host "[!] WARNING: Public firewall profile is disabled!" -ForegroundColor Red
}

Write-Host "`n=== Service Status ===" -ForegroundColor Cyan
$servicesToCheck = @("WinDefend", "wuauserv", "mpssvc")
foreach ($service in $servicesToCheck) {
    Get-Service -Name $service | Select-Object Name, Status
}

if ($Detailed) {
    Write-Host "`n=== Recent Threat Detections ===" -ForegroundColor Cyan
    Get-MpThreatDetection
}
```
2. Run `.\SecurityCheck.ps1` and then `.\SecurityCheck.ps1 -Detailed` to compare output.

#### Expected Output
```text
=== Defender Status ===
AntivirusEnabled RealTimeProtectionEnabled
---------------- -------------------------
            True                      True

=== Firewall Status ===
[+] Public firewall profile is enabled.

=== Service Status ===
Name       Status
----       ------
WinDefend  Running
wuauserv   Running
mpssvc     Running
```

#### Explanation
Running without `-Detailed` skips the threat detection section entirely; running with `-Detailed` adds it, demonstrating how a switch parameter changes script behavior.

---

### Screenshot

> **Insert Screenshot Here**

---

## Challenge Answers

| Challenge | Solution |
|---|---|
| Add BitLocker check | Add a function calling `Get-BitLockerVolume \| Select-Object MountPoint, ProtectionStatus` |
| Show StartType in the loop | Change to `Get-Service -Name $service \| Select-Object Name, Status, StartType` |
| Add `-ComputerName` parameter | Add `[string]$ComputerName = $env:COMPUTERNAME` to `param()`; remote checks would require `-ComputerName` support on each cmdlet (e.g. `Invoke-Command`) |
| Trustworthiness of commented scripts | Comments let you verify what a script does before running it, rather than blindly trusting unfamiliar code |

---

## 🎉 Lab Complete!

You have built a reusable PowerShell script from the ground up — comments, variables, parameters, functions, decision-making, and loops — combining checks from earlier chapters into one repeatable tool.