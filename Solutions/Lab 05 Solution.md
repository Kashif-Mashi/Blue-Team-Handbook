# Lab 05 Solution — Windows Users & Groups Management

## Solution

---

### Task 1: Audit Local Accounts via CMD

#### Step-by-Step Instructions
1. Open CMD as Administrator.
2. Run `net user`.

#### Expected Output
```cmd
User accounts for \\DESKTOP-TRIAGE

-------------------------------------------------------------------------------
Administrator            DefaultAccount           WDAGUtilityAccount
Guest                    admin
The command completed successfully.
```

#### Explanation
Lists all local user identities registered in the local SAM database.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Audit Account Details via PowerShell

#### Step-by-Step Instructions
1. Open PowerShell as Administrator.
2. Run:
```powershell
Get-LocalUser | Select-Object Name, Enabled, LastLogon, Description
```

#### Expected Output
```text
Name               Enabled LastLogon             Description
----               ------- ---------             -----------
Administrator        False                       Built-in account for administering...
DefaultAccount       False                       A user account managed by the system.
Guest                False                       Built-in account for guest access...
WDAGUtilityAccount   False                       A user account managed and used by...
admin                 True 8/2/2026 10:00:00 AM  Local Administrator Account
```

#### Explanation
Displays account status and disabled states for built-in system accounts.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Inspect User SIDs & RIDs

#### Step-by-Step Instructions
1. Run `wmic useraccount get name,sid` in CMD or PowerShell.

#### Expected Output
```text
Name                SID
Administrator       S-1-5-21-3623811015-3361044348-30300820-500
Guest               S-1-5-21-3623811015-3361044348-30300820-501
DefaultAccount      S-1-5-21-3623811015-3361044348-30300820-503
admin               S-1-5-21-3623811015-3361044348-30300820-1001
```

#### Explanation
Identifies Security Identifiers. The built-in Administrator has RID 500 (`...-500`), while custom user accounts start at RID 1000 (`...-1001`).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Inspect UAC Integrity Level & Token Privileges

#### Step-by-Step Instructions
1. Run `whoami /all` in standard CMD and elevated CMD.

#### Expected Output (Elevated CMD snippet)
```text
Mandatory Label\High Mandatory Level S-1-16-12288

PRIVILEGES INFORMATION
----------------------
Privilege Name                  Description                         State
=============================== =================================== ========
SeDebugPrivilege                Debug programs                      Enabled
SeSecurityPrivilege             Manage auditing and security log    Disabled
SeTakeOwnershipPrivilege        Take ownership of files             Disabled
```

#### Explanation
Non-elevated CMD executes under Medium Integrity (`S-1-16-8192`); elevated CMD runs under High Integrity (`S-1-16-12288`) with administrative privileges enabled.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Create a New Local User Account

#### Step-by-Step Instructions
1. Run `net user TempContractor ComplexP@ss2026! /add` in CMD.

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Creates a new local user entry in the SAM database.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Disable Account Expiration / Require Password Change

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Set-LocalUser -Name "TempContractor" -PasswordNeverExpires $false
```

#### Expected Output
```text
Command completes silently.
```

#### Explanation
Configures account password expiration settings.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Create a Custom Local Security Group

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
net localgroup Tier1AnalystGroup /add
```

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Creates a local security group for grouping role permissions.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Add User to Security Group

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
net localgroup Tier1AnalystGroup TempContractor /add
```

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Adds `TempContractor` account SID to `Tier1AnalystGroup` access list.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Verify Group Memberships

#### Step-by-Step Instructions
1. Run in PowerShell:
```powershell
Get-LocalGroupMember -Group "Tier1AnalystGroup"
```

#### Expected Output
```text
ObjectClass Name                        PrincipalSource
----------- ----                        ---------------
User        DESKTOP-TRIAGE\TempContractor Local
```

#### Explanation
Verifies member identities belonging to the specified local group.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Query Current Account Lockout Policy

#### Step-by-Step Instructions
1. Run `net accounts` in CMD.

#### Expected Output
```cmd
Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          42
Minimum password length:                              8
Length of password history maintained:                5
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
```

#### Explanation
Displays current password age, complexity, and lockout limits. `Lockout threshold: Never` indicates vulnerable default settings.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: Configure Account Lockout Policy

#### Step-by-Step Instructions
1. Run `net accounts /lockoutthreshold:5` in elevated CMD.

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Enforces an account lockout after 5 consecutive invalid authentication attempts.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Set Account Lockout Duration

#### Step-by-Step Instructions
1. Run `net accounts /lockoutduration:30` in elevated CMD.

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Sets a 30-minute lockout timer before locked accounts auto-reset.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Disable Built-in Accounts

#### Step-by-Step Instructions
1. Run `net user Guest /active:no` in CMD.

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Ensures the Guest account remains disabled to prevent anonymous access.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Track Security Events for Account Creation

#### Step-by-Step Instructions
1. Open PowerShell and run:
```powershell
Get-WinEvent -LogName "Security" | Where-Object {$_.Id -eq 4720} | Select-Object -First 1 | Format-List
```

#### Expected Output
```text
TimeCreated  : 8/2/2026 10:40:12 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4720
Message      : A user account was created.

               Subject:
                 Security ID:  S-1-5-21-...-1001
                 Account Name: admin
               Target Account:
                 Security ID:  S-1-5-21-...-1008
                 Account Name: TempContractor
```

#### Explanation
Event ID 4720 logs the subject (creator) and target (new account name and SID).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Clean Up Lab Artifacts

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
net user TempContractor /delete
net localgroup Tier1AnalystGroup /delete
```

#### Expected Output
```cmd
The command completed successfully.
The command completed successfully.
```

#### Explanation
Deletes test identities and cleans up local SAM environment.

---

### Screenshot

> **Insert Screenshot Here**

---
