# Solution — Lab 04: File Permissions & Access Control

> This solution guide walks you through the HR Data Leak scenario, demonstrating how to inspect NTFS ACLs, break inheritance, and enforce strict directory restrictions using native Windows utilities.

---

# Task 1 — Recreate the Incident Environment

## Steps

Open Command Prompt as Administrator and set up the test scenario.

```cmd
mkdir C:\Confidential
echo "Sensitive Payroll Data" > C:\Confidential\Payroll.txt
```

### Investigation Note
By default, any new folder created at the root of the `C:\` drive inherits permissions from the `C:\` drive itself. This is the root cause of many privilege escalation and data leak vulnerabilities in enterprise environments.

---

# Task 2 — Inspect Initial Vulnerabilities

## Steps

Check the permissions applied to the newly created file.

```cmd
icacls C:\Confidential\Payroll.txt
```

### Example Output

```
C:\Confidential\Payroll.txt 
  BUILTIN\Administrators:(I)(F)
  NT AUTHORITY\SYSTEM:(I)(F)
  BUILTIN\Users:(I)(RX)
  NT AUTHORITY\Authenticated Users:(I)(M)
```

### Investigation Note
The `(I)` indicates that these permissions are **Inherited** from the parent container (`C:\Confidential`). Notice that `BUILTIN\Users` has `(RX)` (Read and Execute) access. This means *any* standard user on the machine can read this file. This explains how the HR data was leaked.

---

# Task 3 — The PowerShell Perspective

## Steps

Retrieve the detailed Access Control List and owner information via PowerShell.

```powershell
Get-Acl C:\Confidential\Payroll.txt | Format-List
```

### Investigation Note
`Get-Acl` provides a more programmatic view of the Security Descriptor. You will see the `Owner` property (likely your Administrator account or the `BUILTIN\Administrators` group) and the specific Access Control Entries (ACEs).

---

# Task 4 — Simulate the Insider Threat

## Steps

Create a standard, non-administrative user account to test the vulnerability.

```cmd
net user SuspectUser Password123! /add
```

### Investigation Note
Testing your assumptions by creating a standard user is a reliable way to verify NTFS misconfigurations during a live audit.

---

# Task 5 — Prove Unauthorized Access

## Steps

Verify that the `SuspectUser` can read the confidential data. 

```cmd
runas /user:SuspectUser "cmd /k type C:\Confidential\Payroll.txt"
```
*(Enter the password `Password123!` when prompted).*

### Investigation Note
The command successfully prints "Sensitive Payroll Data" to the screen. You have just proven the vulnerability: a standard user leveraged inherited `Users` group permissions to access data they shouldn't see.

---

# Task 6 — Stop the Bleeding (Disable Inheritance)

## Steps

To secure the folder, you must first break the inheritance chain so permissions stop flowing down from `C:\`.

```cmd
icacls C:\Confidential /inheritance:d
```

### Investigation Note
The `/inheritance:d` flag disables inheritance and copies the currently inherited ACEs and converts them into explicit ACEs. This ensures you don't accidentally lock yourself out of the folder while reconfiguring it.

---

# Task 7 — Evict the Unauthorized

## Steps

Now that permissions are explicit, safely remove the `Users` group.

```cmd
icacls C:\Confidential /remove Users
```

*(You may also want to remove `Authenticated Users` using `icacls C:\Confidential /remove "Authenticated Users"`).*

### Investigation Note
By removing the broad `Users` group, you immediately cut off access to standard accounts like `SuspectUser`. Only Administrators and SYSTEM remain on the DACL.

---

# Task 8 — Enforce Strict Access Controls

## Steps

Ensure the `Administrators` group has explicit, propagating Full Control.

```cmd
icacls C:\Confidential /grant Administrators:(OI)(CI)F /T
```

### Investigation Note
- `(OI)`: Object Inherit (Files will inherit this permission)
- `(CI)`: Container Inherit (Subfolders will inherit this permission)
- `(F)`: Full Control
- `/T`: Applies the change recursively to all existing files inside the directory.

---

# Task 9 — Reclaim File Ownership

## Steps

If an attacker or rogue admin had changed the file owner to lock you out, you can take it back.

```cmd
takeown /F C:\Confidential\Payroll.txt /A
```

### Investigation Note
The `/A` flag gives ownership to the local `Administrators` group rather than your specific logged-in user account. A file owner ALWAYS has the implicit right to modify the DACL (change permissions), even if the DACL explicitly denies them access!

---

# Task 10 — Verify the Remediation

## Steps

Verify the final, hardened permissions.

```cmd
icacls C:\Confidential
```

### Example Output

```
C:\Confidential 
  BUILTIN\Administrators:(OI)(CI)(F)
  NT AUTHORITY\SYSTEM:(OI)(CI)(F)
```

### Investigation Note
The `Users` group is gone. The `(I)` inheritance flag is gone. The folder is now secured with explicit permissions, stopping the data leak immediately.

---

# Task 11 — Clean up the Environment

## Steps

Remove the artifacts created during this lab.

```cmd
rmdir /S /Q C:\Confidential
net user SuspectUser /delete
```

---

# Scenario Conclusion

By understanding how NTFS inherited permissions propagate from root directories, you successfully identified the misconfiguration that caused the data exposure. Using `icacls`, you broke the inheritance chain, evicted the unauthorized users, and re-secured the directory, mitigating the incident.
