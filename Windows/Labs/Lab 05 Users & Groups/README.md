# Lab 05 — Windows Users & Groups Management

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 06 (Windows Users & Groups).  
**Objectives**:
- Create and manage local user accounts using CMD and PowerShell.
- Create local security groups and manage group memberships.
- Inspect user Security Identifiers (SIDs) and account properties.
- Audit User Account Control (UAC) token integrity levels.
- Configure and test local account lockout policies.

---

## Scenario

A company's Internal Security Audit revealed unauthorized user creation on several workstations. To establish a hardened identity baseline, the SOC lead has instructed you to perform an identity audit on workstation `DESKTOP-TRIAGE`.

You will audit built-in accounts, configure password and lockout security policies, create controlled service groups, test administrative elevation, and track security event logs associated with identity management.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: `net.exe`, `wmic.exe`, `powershell.exe`, `secpol.msc` / `net accounts`

---

## Tasks

### Task 1: Audit Local Accounts via CMD
List all local user accounts on the host using `net user`.

### Task 2: Audit Account Details via PowerShell
Use `Get-LocalUser | Select-Object Name, Enabled, LastLogon, Description` to inspect user statuses.

### Task 3: Inspect User SIDs & RIDs
Run `wmic useraccount get name,sid` to extract SIDs for all local accounts. Identify the RID 500 account.

### Task 4: Inspect UAC Integrity Level & Token Privileges
Open standard CMD and elevated CMD, run `whoami /all` in both, and compare the Integrity Levels and privileges.

### Task 5: Create a New Local User Account
Create local user account `TempContractor` with password `ComplexP@ss2026!` using `net user`.

### Task 6: Disable Account Expiration / Require Password Change
Use PowerShell (`Set-LocalUser -Name TempContractor -PasswordNeverExpires $false`) to manage account parameters.

### Task 7: Create a Custom Local Security Group
Create security group `Tier1AnalystGroup` using `net localgroup Tier1AnalystGroup /add`.

### Task 8: Add User to Security Group
Add `TempContractor` to `Tier1AnalystGroup` using `net localgroup Tier1AnalystGroup TempContractor /add`.

### Task 9: Verify Group Memberships
Use `Get-LocalGroupMember -Group "Tier1AnalystGroup"` to verify group membership.

### Task 10: Query Current Account Lockout Policy
Run `net accounts` to view lockout threshold, duration, and password requirements.

### Task 11: Configure Account Lockout Policy
Set account lockout threshold to 5 failed attempts using `net accounts /lockoutthreshold:5`.

### Task 12: Set Account Lockout Duration
Set lockout duration to 30 minutes using `net accounts /lockoutduration:30`.

### Task 13: Disable Built-in Accounts
Ensure `Guest` account is disabled using `net user Guest /active:no`.

### Task 14: Track Security Events for Account Creation
Open Event Viewer (`eventvwr.msc`), navigate to `Windows Logs -> Security`, and filter for Event ID **4720** (User Account Created).

### Task 15: Clean Up Lab Artifacts
Remove user `TempContractor` and group `Tier1AnalystGroup` from the system.

---

## Verification

To verify success:
- Confirm `TempContractor` SID contains expected host SID format.
- Confirm `net accounts` shows lockout threshold set to 5.
- Confirm Event ID 4720 is present in Security log corresponding to account creation.

---

## Blue Team Notes

- **Detecting Rogue Accounts**: Attackers add backdoor accounts during post-exploitation. Monitoring Event ID 4720 allows immediate detection of unexpected account creation.
- **Group Escalation Monitoring**: Adding users to `Administrators` or `Remote Desktop Users` triggers Event ID 4732. SOC rules should alert whenever non-domain accounts are added to sensitive local groups.

---

## Common Errors

- **Non-Elevated Privilege Errors**: Commands like `net user /add` or `net accounts` fail with "Access is denied" if executed without administrative privileges.
- **Weak Passwords**: Creating test users with simple passwords fails if local password complexity policies are enabled.

---

## MITRE ATT&CK Mapping

- **T1087.001**: Account Discovery: Local Account
- **T1069.001**: Permission Groups Discovery: Local Groups
- **T1136.001**: Create Account: Local Account
- **T1078.003**: Valid Accounts: Local Accounts

---

## Challenge Section

1. Write a PowerShell script that exports all local user accounts, their SIDs, and group memberships into an HTML report.
2. Query Event ID **4732** in the Security Event Log using `Get-WinEvent` to identify who added a user to a security group.
3. Use PowerShell to check if the built-in Administrator account (RID 500) has been renamed.
4. Test account lockout by attempting invalid logons against a test account until locked out, then locate Event ID **4740** (Account Lockout).
5. Compare token privileges returned by `whoami /priv` before and after enabling `SeDebugPrivilege`.


---

# Solution

➡ **[View Solution](../Solution/Lab%2005%20Solution.md)**
