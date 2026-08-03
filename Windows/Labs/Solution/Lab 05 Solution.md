# Solution — Lab 05: Windows Users & Groups Management

> This solution guide walks you through the Insider Threat scenario, demonstrating how to audit local accounts, identify unauthorized privilege escalation, analyze Security Identifiers (SIDs), and harden local account lockout policies.

---

# Task 1 — Simulate the Compromise

## Steps

Open Command Prompt as Administrator. Create the backdoor account and escalate its privileges.

```cmd
net user TempContractor ComplexP@ss2026! /add
net localgroup Administrators TempContractor /add
```

### Investigation Note
Attackers often name their backdoor accounts something innocuous like `TempContractor`, `Helpdesk`, or `UpdateService` so that they blend into normal IT operations.

---

# Task 2 — Audit Local Accounts (CMD)

## Steps

List all local user accounts on the host.

```cmd
net user
```

### Example Output

```
User accounts for \\DESKTOP-TRIAGE

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest
JohnDoe                  TempContractor
The command completed successfully.
```

### Investigation Note
The `TempContractor` account is clearly visible. While `net user` is fast, it lacks context (like creation date or enabled status), which is why we must escalate to PowerShell.

---

# Task 3 — Audit Account Details (PowerShell)

## Steps

Retrieve detailed user status using PowerShell.

```powershell
Get-LocalUser | Select-Object Name, Enabled, LastLogon, Description
```

### Example Output

```
Name           Enabled LastLogon Description
----           ------- --------- -----------
Administrator    False           Built-in account for administering the computer/domain
DefaultAccount   False           A user account managed by the system.
Guest            False           Built-in account for guest access to the computer/domain
JohnDoe           True 8/2/2026  
TempContractor    True           
```

### Investigation Note
You can immediately see that `TempContractor` is Enabled, has no description, and has no `LastLogon` time (since the attacker just created it and hasn't logged in interactively yet).

---

# Task 4 — Inspect SIDs and RIDs

## Steps

Extract SIDs for all local accounts to identify built-in accounts vs custom accounts.

```cmd
wmic useraccount get name,sid
```

### Example Output

```
Name            SID
Administrator   S-1-5-21-3623811015-3361044348-30300820-500
DefaultAccount  S-1-5-21-3623811015-3361044348-30300820-503
Guest           S-1-5-21-3623811015-3361044348-30300820-501
JohnDoe         S-1-5-21-3623811015-3361044348-30300820-1001
TempContractor  S-1-5-21-3623811015-3361044348-30300820-1002
```

### Investigation Note
The built-in Administrator will *always* end in `-500`, even if an attacker renames the account to `Guest` or `Helpdesk` to hide it. Custom user accounts always start with `-1000` or higher. `TempContractor` is clearly a newly created custom account.

---

# Task 5 — Audit Administrative Privilege Escalation

## Steps

Check if the rogue account has elevated privileges.

```powershell
Get-LocalGroupMember -Group "Administrators"
```

### Example Output

```
ObjectClass Name                                PrincipalSource
----------- ----                                ---------------
User        DESKTOP-TRIAGE\Administrator        Local
User        DESKTOP-TRIAGE\JohnDoe              Local
User        DESKTOP-TRIAGE\TempContractor       Local
```

### Investigation Note
The `TempContractor` account is in the Administrators group. The attacker has achieved full privilege escalation and can now bypass UAC, modify the registry, and install persistent kernel-level malware.

---

# Task 6 — Track the Origin (Event Logs)

## Steps

1. Open **Event Viewer** (`eventvwr.msc`).
2. Navigate to **Windows Logs** -> **Security**.
3. Click **Filter Current Log** on the right pane.
4. Enter `4720` in the `<All Event IDs>` box.

### Investigation Note
Event ID 4720 logs the exact second the account was created. By looking at the "Subject" field in the event details, you can see which user account *created* the `TempContractor` account, providing a crucial pivot point for your investigation.

---

# Task 7 — Review Password Policies

## Steps

Check the host's vulnerability to brute force attacks.

```cmd
net accounts
```

### Example Output

```
Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          42
Minimum password length:                              0
Length of password history maintained:                None
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
```

### Investigation Note
The `Lockout threshold` is set to "Never", meaning an attacker can attempt to guess passwords infinitely without ever being locked out.

---

# Task 8 — Harden the System

## Steps

Enforce a strict lockout policy to prevent brute forcing.

```cmd
net accounts /lockoutthreshold:5
net accounts /lockoutduration:30
```

### Investigation Note
Now, if an attacker guesses the wrong password 5 times, the account will be locked and unusable for 30 minutes, effectively neutralizing automated brute-force attacks.

---

# Task 9 — Remediate the Threat

## Steps

Eradicate the backdoor from the system.

```cmd
net user TempContractor /delete
```

### Investigation Note
Deleting the account immediately severs the attacker's persistent access. In a real-world scenario, you would also force a password reset on all other administrator accounts, as the attacker likely dumped the LSASS memory before you caught them.

---

# Scenario Conclusion

By methodically auditing the local user database, extracting hidden SIDs, and validating group memberships, you successfully identified the unauthorized backdoor account and proved that the attacker had escalated to local Administrator. By deleting the account and hardening the lockout policy, you contained the incident and fortified the endpoint.
