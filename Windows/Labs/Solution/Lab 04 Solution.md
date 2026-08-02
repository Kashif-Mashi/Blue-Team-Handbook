# Lab 04 Solution — File Permissions & Access Control Investigation

## Solution

---

### Task 1: Create Lab Test Directory & Sensitive Files

#### Step-by-Step Instructions
1. Open elevated CMD and execute:
```cmd
mkdir C:\SecureData
echo Confidential Payroll Data > C:\SecureData\Payroll.txt
```

#### Expected Output
```cmd
C:\Windows\System32> mkdir C:\SecureData
C:\Windows\System32> echo Confidential Payroll Data > C:\SecureData\Payroll.txt
```

#### Explanation
Creates the test folder and sensitive payload file for access control testing.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: Inspect Initial File Permissions via CMD

#### Step-by-Step Instructions
1. Run `icacls C:\SecureData\Payroll.txt`.

#### Expected Output
```cmd
C:\SecureData\Payroll.txt NT AUTHORITY\SYSTEM:(I)(F)
                          BUILTIN\Administrators:(I)(F)
                          BUILTIN\Users:(I)(RX)
```

#### Explanation
The `(I)` flag indicates permissions are inherited from parent container `C:\SecureData`. `BUILTIN\Users` has Read & Execute `(RX)` rights by default.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Inspect Access Control Lists via PowerShell

#### Step-by-Step Instructions
1. Open PowerShell and run:
```powershell
Get-Acl C:\SecureData\Payroll.txt | Format-List
```

#### Expected Output
```text
Path   : Microsoft.PowerShell.Core\FileSystem::C:\SecureData\Payroll.txt
Owner  : BUILTIN\Administrators
Group  : WORKSTATION\Domain Users
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
```

#### Explanation
`Get-Acl` extracts owner details and explicit/inherited access control entries (ACEs) in .NET object format.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Create a Dedicated Test User Account

#### Step-by-Step Instructions
1. In CMD, execute:
```cmd
net user TestUser01 P@ssword2026! /add
```

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Creates a standard local user identity for verifying DACL boundaries.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Grant Explicit Read Permissions

#### Step-by-Step Instructions
1. Run:
```cmd
icacls C:\SecureData\Payroll.txt /grant TestUser01:(R)
```

#### Expected Output
```cmd
processed file: C:\SecureData\Payroll.txt
Successfully processed 1 files; Failed processing 0 files
```

#### Explanation
Adds an explicit Access Control Entry (ACE) granting Read `(R)` permission to `TestUser01`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Verify Modified DACL Output

#### Step-by-Step Instructions
1. Run `icacls C:\SecureData\Payroll.txt`.

#### Expected Output
```cmd
C:\SecureData\Payroll.txt DESKTOP-TRIAGE\TestUser01:(R)
                          NT AUTHORITY\SYSTEM:(I)(F)
                          BUILTIN\Administrators:(I)(F)
                          BUILTIN\Users:(I)(RX)
```

#### Explanation
Shows `TestUser01:(R)` added as an explicit ACE at the top of the DACL (explicit entries precede inherited ones).

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Test Access Rights

#### Step-by-Step Instructions
1. Run PowerShell command as `TestUser01`:
```powershell
Get-Content C:\SecureData\Payroll.txt
```

#### Expected Output
```text
Confidential Payroll Data
```

#### Explanation
`TestUser01` successfully reads the file content based on explicit Read access.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Disable Permission Inheritance on Folder

#### Step-by-Step Instructions
1. Run `icacls C:\SecureData /inheritance:d`.

#### Expected Output
```cmd
processed file: C:\SecureData
Successfully processed 1 files; Failed processing 0 files
```

#### Explanation
`/inheritance:d` disables inheritance and converts all inherited parent ACEs into explicit ACEs on `C:\SecureData`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 9: Remove Standard Users Group Access

#### Step-by-Step Instructions
1. Run `icacls C:\SecureData /remove Users`.

#### Expected Output
```cmd
processed file: C:\SecureData
Successfully processed 1 files; Failed processing 0 files
```

#### Explanation
Strips all ACE entries matching the local `Users` group from the folder DACL.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 10: Enforce Full Control for Administrators Only

#### Step-by-Step Instructions
1. Run:
```cmd
icacls C:\SecureData /grant Administrators:(OI)(CI)F /T
```

#### Expected Output
```cmd
processed file: C:\SecureData
processed file: C:\SecureData\Payroll.txt
Successfully processed 2 files; Failed processing 0 files
```

#### Explanation
`(OI)` (Object Inherit) and `(CI)` (Container Inherit) propagate Full Control `(F)` to all current and future child files and subdirectories.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 11: Transfer File Ownership via CMD

#### Step-by-Step Instructions
1. Run `takeown /F C:\SecureData\Payroll.txt /A`.

#### Expected Output
```cmd
SUCCESS: The file (or folder): "C:\SecureData\Payroll.txt" now owned by the administrators group.
```

#### Explanation
`/A` assigns ownership to the local `Administrators` group instead of the individual user running the command.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 12: Verify Ownership Change via PowerShell

#### Step-by-Step Instructions
1. Run `(Get-Acl C:\SecureData\Payroll.txt).Owner`.

#### Expected Output
```text
BUILTIN\Administrators
```

#### Explanation
Confirms the owner attribute in the NTFS file header is set to `BUILTIN\Administrators`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 13: Revoke Individual User Permissions

#### Step-by-Step Instructions
1. Run `icacls C:\SecureData\Payroll.txt /remove TestUser01`.

#### Expected Output
```cmd
processed file: C:\SecureData\Payroll.txt
Successfully processed 1 files; Failed processing 0 files
```

#### Explanation
Removes explicit ACE for `TestUser01`, revoking read access.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 14: Modify File ACLs using PowerShell `Set-Acl`

#### Step-by-Step Instructions
1. Run script in PowerShell:
```powershell
$Acl = Get-Acl "C:\SecureData"
$Ar = New-Object System.Security.AccessControl.FileSystemAccessRule("SYSTEM","FullControl","ContainerInherit,ObjectInherit","None","Allow")
$Acl.SetAccessRule($Ar)
Set-Acl -Path "C:\SecureData" -AclObject $Acl
```

#### Expected Output
```text
Command completes silently. ACL updated.
```

#### Explanation
Programmatically constructs a .NET AccessRule object and commits it using `Set-Acl`.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 15: Clean Up Test Artifacts

#### Step-by-Step Instructions
1. Run in CMD:
```cmd
rmdir /s /q C:\SecureData
net user TestUser01 /delete
```

#### Expected Output
```cmd
The command completed successfully.
```

#### Explanation
Removes temporary lab files and test user identity.

---

### Screenshot

> **Insert Screenshot Here**

---
