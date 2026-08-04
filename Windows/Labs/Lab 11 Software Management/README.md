# Lab 11 — Software & Package Management

## Difficulty

🟢 Beginner

**Estimated Time**: 35 Minutes  
**Prerequisites**: Completion of Chapter 13 (Software & Package Management).  
**Objectives**:
- List installed software using PowerShell and the registry.
- Search for and install a package using `winget`.
- Update installed packages using `winget`.
- Uninstall a package from the command line.
- Export a software inventory snapshot to a file.

---

## Scenario

Your organization wants to start keeping a simple software inventory for each workstation as part of routine hygiene. You've been asked to practice the process on a lab machine: list what's installed, install and remove a small test application, and produce an exportable inventory snapshot.

---

## Lab Environment

- **Operating System**: Windows 10 / 11 Workstation
- **User Role**: Local Administrator privileges available
- **Internet Access**: Enabled
- **Tools Used**: PowerShell, `winget`

---

## Tasks

### Task 1: List Installed Software via the Registry
Run `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | Select-Object DisplayName, DisplayVersion, Publisher | Where-Object { $_.DisplayName }` to view a full software list.

### Task 2: List Installed Software via winget
Run `winget list` and compare the results against Task 1's output.

### Task 3: Search for a Package
Run `winget search "notepad++"` to confirm the package is available in the winget catalog.

### Task 4: Install a Test Package
Run `winget install Notepad++.Notepad++` to install it.

### Task 5: Confirm the Installation
Run `winget list` again and confirm Notepad++ now appears.

### Task 6: Update All Packages
Run `winget upgrade --all` to update any outdated software winget manages.

### Task 7: Uninstall the Test Package
Run `winget uninstall Notepad++.Notepad++` to remove it again.

### Task 8: Export a Software Inventory Snapshot
Run the following to save a CSV snapshot for later comparison:
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Where-Object { $_.DisplayName } |
    Export-Csv -Path "$env:USERPROFILE\Desktop\software_inventory.csv" -NoTypeInformation
```

---

## Verification

To verify success:
- Confirm Notepad++ appeared in `winget list` after Task 4 and is gone after Task 7.
- Confirm `software_inventory.csv` exists on the Desktop after Task 8 and can be opened.

---

## Blue Team Notes

- **No Single Source of Truth**: Comparing the registry-based list (Task 1) against `winget list` (Task 2) reinforces why analysts check more than one method — some software won't appear in both.
- **Baselines Need Snapshots**: The CSV exported in Task 8 is exactly the kind of artifact used to build a baseline for comparison during a later investigation.

---

## Common Errors

- **Assuming winget shows everything**: `winget list` only shows software winget recognizes and can manage — it is not a complete inventory on its own.
- **Forgetting the exact package ID**: `winget install` requires the correct package ID (e.g. `Notepad++.Notepad++`), not just the display name.

---

## MITRE ATT&CK Mapping

- **T1518**: Software Discovery
- **T1195**: Supply Chain Compromise (relevant when discussing why software provenance matters)

---

## Challenge Section

1. Modify Task 8's command to also filter for software published in the last 30 days.
2. Research and explain the difference between `winget upgrade --all` and manually checking Windows Update.
3. Find one piece of software on your own machine that appears in the registry list but not in `winget list`, and explain why that might be.
4. Write a one-line command that counts the total number of installed programs found via the registry method.