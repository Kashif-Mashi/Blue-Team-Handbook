# Linux User and Group Management Cheatsheet

> **Operational Quick Reference for System Administrators & BSIT Students**  
> Companion detailed notes: [05-User-Management.md](../03-Linux-Fundamentals/05-User-Management.md)

---

## 👥 Linux Account Tiers & UID Boundaries

| Account Category | UID Range (RHEL 7/8/9) | UID Range (RHEL 6) | Shell Environment | Primary Operational Role |
|---|---|---|---|---|
| **Superuser (`root`)** | `UID 0` | `UID 0` | `/bin/bash` | Complete administrative authority; bypasses DAC |
| **System / Service Accounts** | `UID 1 - 999` | `UID 1 - 499` | `/sbin/nologin` | Background services (Apache, MySQL, Chrony); no login |
| **Standard User Accounts** | `UID >= 1000` | `UID >= 500` | `/bin/bash` | Human employees, developers, and students |

---

## 🗃️ Identity Databases Field Structure Reference

### `/etc/passwd` (7 Fields): `username:x:UID:GID:GECOS:home:shell`
- **Field 1:** Username (`student`)
- **Field 2:** Password placeholder (`x` = check `/etc/shadow`)
- **Field 3:** Numerical User ID (`1001`)
- **Field 4:** Primary Group ID (`1001`)
- **Field 5:** GECOS / Comment description (`Standard User - IT Dept`)
- **Field 6:** Home directory absolute path (`/home/student`)
- **Field 7:** Login shell (`/bin/bash` for interactive; `/sbin/nologin` for services)

### `/etc/shadow` (9 Fields): `username:hash:last:min:max:warn:inact:expire:res`
- **Field 1:** Username matching `/etc/passwd`
- **Field 2:** Encrypted salted password hash (`$6$` = SHA-512, `$y$` = yescrypt; `!` or `*` = locked)
- **Field 3:** Days since epoch (Jan 1, 1970) when password was last changed
- **Field 4:** Minimum days required between password changes
- **Field 5:** Maximum days of password validity (e.g. `90`)
- **Field 6:** Warning days prior to password expiration (e.g. `7`)
- **Field 7:** Inactive days after expiration before account is disabled
- **Field 8:** Expiration date in epoch days when account terminates completely
- **Field 9:** Reserved field for future kernel use

### `/etc/group` (4 Fields): `group_name:password:GID:user_roster`
- **Field 1:** Group name (`developers`)
- **Field 2:** Group password placeholder (`x`)
- **Field 3:** Numerical Group ID (`1002`)
- **Field 4:** Comma-separated list of **supplementary members** (`alice,bob,student`)

---

## 👤 User Lifecycle Management Commands

| Administrative Operation | Command Line Syntax | Key Options & Notes |
|---|---|---|
| **Create Standard User** | `useradd -m -c "Comment" -s /bin/bash user` | `-m` creates home directory; `-c` sets GECOS |
| **Create with Specific UID** | `useradd -u 2050 -m user` | Assigns explicit numerical UID |
| **Create with Groups** | `useradd -m -G wheel,developers user` | Sets initial supplementary groups |
| **Append Supplementary Group** | `usermod -aG developers user` | ⚠️ **MANDATORY `-a`:** Omitting `-a` wipes existing groups! |
| **Change Login Shell** | `usermod -s /sbin/nologin user` | Disables interactive terminal login |
| **Lock Account Password** | `usermod -L user` or `passwd -l user` | Prepends `!` in `/etc/shadow` (locks account) |
| **Unlock Account Password** | `usermod -U user` or `passwd -u user` | Removes `!` in `/etc/shadow` |
| **Delete User (Keep Home)** | `userdel user` | Leaves home folder `/home/user` intact on disk |
| **Delete User (Remove Home)** | `userdel -r user` | **Permanently deletes** user account AND home directory |

---

## ⏳ Password Aging Policies (`chage`)

| Administrative Operation | Command Line Syntax | Operational Result |
|---|---|---|
| **Inspect Password Aging** | `chage -l <user>` | Displays expiration date, last change, and warning days |
| **Set Maximum Password Life** | `chage -M 90 <user>` | Enforces mandatory 90-day password rotation |
| **Set Expiration Warning Days**| `chage -W 7 <user>` | Alerts user 7 days before password expires |
| **Force Password Reset on Next Login**| `chage -d 0 <user>` | Sets last-changed date to 0; user must change password immediately |
| **Set Account Expiry Date** | `chage -E 2026-12-31 <user>` | Automatically terminates account on specified date |

---

## 🔑 Sudo Delegation and Privilege Escalation

```bash
# Switch to root with full login environment and $PATH (Always include the dash!)
su -

# Execute a single administrative command with root privileges
sudo systemctl restart httpd

# Safely edit the /etc/sudoers file with automated syntax validation
visudo
```

### Granting Sudo Privileges on RHEL:
Red Hat Enterprise Linux pre-configures the `wheel` group with full `sudo` privileges. To grant administrator rights to user `student`, simply append them to the `wheel` group:
```bash
usermod -aG wheel student
```
