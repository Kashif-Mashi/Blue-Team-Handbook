# Lab 11 Solution — Software & Package Management

## Solution

---

### Task 1: List Installed Software via the Registry

#### Step-by-Step Instructions
1. Open PowerShell.
2. Run:
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Where-Object { $_.DisplayName }
```

#### Expected Output
```text
DisplayName          DisplayVersion   Publisher
-----------          --------------   ---------
Google Chrome        124.0.6367.91    Google LLC
Microsoft Edge       124.0.2478.51    Microsoft Corporation
```

#### Explanation
Reads the registry Uninstall key, one of the fastest and most complete methods for listing installed software.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 2: List Installed Software via winget

#### Step-by-Step Instructions
1. Run `winget list`.

#### Expected Output
```text
Name                    Id                          Version
----------------------  --------------------------  --------
Google Chrome           Google.Chrome               124.0.6367.91
Microsoft Edge          Microsoft.Edge              124.0.2478.51
```

#### Explanation
`winget list` shows software winget recognizes — compare it against Task 1's output to see any differences.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 3: Search for a Package

#### Step-by-Step Instructions
1. Run `winget search "notepad++"`.

#### Expected Output
```text
Name         Id                       Version    Source
-----------  -----------------------  ---------  ------
Notepad++    Notepad++.Notepad++      8.6.6       winget
```

#### Explanation
Confirms the exact package ID (`Notepad++.Notepad++`) needed for installation in the next task.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 4: Install a Test Package

#### Step-by-Step Instructions
1. Run `winget install Notepad++.Notepad++`.
2. Accept any source agreement prompts if shown.

#### Expected Output
```text
Found Notepad++ [Notepad++.Notepad++]
Downloading ...
Successfully installed
```

#### Explanation
Installs the package directly from the command line without needing a browser.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 5: Confirm the Installation

#### Step-by-Step Instructions
1. Run `winget list` again.

#### Expected Output
```text
Name         Id                       Version
-----------  -----------------------  --------
Notepad++    Notepad++.Notepad++      8.6.6
```

#### Explanation
Confirms the package now appears in the installed software list.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 6: Update All Packages

#### Step-by-Step Instructions
1. Run `winget upgrade --all`.

#### Expected Output
```text
Name    Id    Version    Available    Source
----    --    -------    ---------    ------
(No applicable updates found)
```

#### Explanation
Updates any winget-managed software that has a newer version available; output will vary depending on what's already up to date.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 7: Uninstall the Test Package

#### Step-by-Step Instructions
1. Run `winget uninstall Notepad++.Notepad++`.
2. Run `winget list` again and confirm it's gone.

#### Expected Output
```text
Successfully uninstalled
```

#### Explanation
Removes the test package, returning the machine to its original state.

---

### Screenshot

> **Insert Screenshot Here**

---

### Task 8: Export a Software Inventory Snapshot

#### Step-by-Step Instructions
1. Run:
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Where-Object { $_.DisplayName } |
    Export-Csv -Path "$env:USERPROFILE\Desktop\software_inventory.csv" -NoTypeInformation
```
2. Open the CSV file to confirm it was created correctly.

#### Expected Output
```text
(No console output — file is written to the Desktop)
```

#### Explanation
Creates a reusable snapshot of installed software that can be compared against a future snapshot to detect changes.

---

### Screenshot

> **Insert Screenshot Here**

---

## Challenge Answers

| Challenge | Solution |
|---|---|
| Filter by recent install date | Add `\| Where-Object { [datetime]::ParseExact($_.InstallDate,'yyyyMMdd',$null) -gt (Get-Date).AddDays(-30) }` |
| winget upgrade vs Windows Update | `winget upgrade --all` updates individual applications; Windows Update patches the OS itself and Microsoft-published components |
| Software missing from winget list | Software installed via a custom EXE installer, rather than through winget's supported sources, often won't appear |
| Count installed programs | `(Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" \| Where-Object {$_.DisplayName}).Count` |

---

## 🎉 Lab Complete!

You have practiced listing, installing, updating, and removing software, along with exporting a reusable inventory snapshot — core skills for vulnerability management and baseline comparison.