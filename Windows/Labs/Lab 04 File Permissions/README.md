# Lab 04 — File Permissions & Access Control Investigation

## Difficulty

🟢 Beginner

**Estimated Time**: 45 Minutes  
**Prerequisites**: Completion of Chapter 03 (File System) and Chapter 07/Concepts (NTFS Permissions).  
**Objectives**:
- Inspect NTFS permissions using `icacls` and `Get-Acl`.
- Differentiate between explicit permissions and inherited permissions.
- Modify Discretionary Access Control Lists (DACLs) via command line.
- Enforce folder access restrictions and test user permissions.
- Audit owner changes using `takeown` and PowerShell (`Set-Acl`).

---

## Scenario

A financial organization suffered a data exposure incident. Sensitive internal reports stored in `C:\Confidential` were accessed by non-authorized users due to inherited permission misconfigurations.

As an Incident Responder and Systems Auditor, you are assigned to inspect current access control lists (ACLs), remove excessive permissions, break permission inheritance on sensitive directories, and grant restricted access exclusively to administrative security groups.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: `icacls.exe`, `takeown.exe`, `Get-Acl`, `Set-Acl`

---

## Tasks

### Task 1: Create Lab Test Directory & Sensitive Files
Create directory `C:\SecureData` and a test file `C:\SecureData\Payroll.txt`.

### Task 2: Inspect Initial File Permissions via CMD
Run `icacls C:\SecureData\Payroll.txt` and document default inherited permissions.

### Task 3: Inspect Access Control Lists via PowerShell
Use `Get-Acl C:\SecureData\Payroll.txt | Format-List` to inspect access rules and file owner.

### Task 4: Create a Dedicated Test User Account
Create local user `TestUser01` with a secure password using `net user`.

### Task 5: Grant Explicit Read Permissions
Use `icacls` to grant `TestUser01` explicit Read `(R)` access to `C:\SecureData\Payroll.txt`.

### Task 6: Verify Modified DACL Output
Re-run `icacls C:\SecureData\Payroll.txt` to verify the addition of `TestUser01:(R)`.

### Task 7: Test Access Rights
Attempt to read `C:\SecureData\Payroll.txt` under the security context of `TestUser01`.

### Task 8: Disable Permission Inheritance on Folder
Use `icacls C:\SecureData /inheritance:d` to convert inherited permissions into explicit permissions.

### Task 9: Remove Standard Users Group Access
Use `icacls C:\SecureData /remove Users` to strip access rights from the local `Users` group.

### Task 10: Enforce Full Control for Administrators Only
Grant `Administrators` group Full Control `(F)` over `C:\SecureData` recursively using `icacls C:\SecureData /grant Administrators:(OI)(CI)F /T`.

### Task 11: Transfer File Ownership via CMD
Use `takeown /F C:\SecureData\Payroll.txt /A` to transfer file ownership to the local Administrators group.

### Task 12: Verify Ownership Change via PowerShell
Run `(Get-Acl C:\SecureData\Payroll.txt).Owner` to confirm the new owner identity.

### Task 13: Revoke Individual User Permissions
Use `icacls C:\SecureData\Payroll.txt /remove TestUser01` to revoke all privileges from `TestUser01`.

### Task 14: Modify File ACLs using PowerShell `Set-Acl`
Construct a PowerShell script that applies a restrictive Access Rule to `C:\SecureData` using `System.Security.AccessControl.FileSystemAccessRule`.

### Task 15: Clean Up Test Artifacts
Remove directory `C:\SecureData` and delete account `TestUser01`.

---

## Verification

To verify success:
- Confirm `icacls C:\SecureData` shows inheritance disabled `(Disabled)`.
- Confirm `Users` group is stripped from access list.
- Confirm file owner is assigned to `BUILTIN\Administrators`.

---

## Blue Team Notes

- **Privilege Escalation via Weak ACLs**: Attackers look for weak directory permissions on system services (e.g. write access to service executables or unquoted service paths) to escalate privileges to `SYSTEM`.
- **Inheritance Misconfigurations**: Folders created under `C:\` inherit `Users:(RX)` rights by default. Sensitive data must have inheritance disabled and explicit DACLs applied.

---

## Common Errors

- **Forgetting Object/Container Inherit Flags**: Applying `(F)` without `(OI)(CI)` flags causes subfolders and files to miss permission propagation.
- **Accidental Lockout**: Removing `SYSTEM` or `Administrators` from DACLs locks out access. Take ownership (`takeown`) to restore access if locked out.

---

## MITRE ATT&CK Mapping

- **T1222.001**: File and Directory Permissions Modification: Windows File and Directory Permissions Modification
- **T1070.004**: Indicator Removal on Host: File Deletion

---

## Challenge Section

1. Identify all files under `C:\Windows\System32` where `Users` group has Modify `(M)` or Write `(W)` access using `icacls`.
2. Write a PowerShell script that audits all subdirectories under `C:\` and reports directories with disabled inheritance.
3. Use `Get-Acl` to output file owner SIDs across all `.exe` files in a given directory.
4. Modify an ACL to explicitly Deny write access to a user while granting Read access, and test which rule takes precedence.
5. Restore default inherited permissions on a directory using `icacls /reset`.


---

# Solution

➡ **[View Solution](../Solution/Lab%2004%20Solution.md)**
