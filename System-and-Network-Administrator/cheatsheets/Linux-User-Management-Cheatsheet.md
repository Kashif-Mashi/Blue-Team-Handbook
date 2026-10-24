# Linux User and Group Management Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [05-User-Management.md](../03-Linux-Fundamentals/05-User-Management.md) | [Cheatsheets Index](README.md)

---

## 👤 User Account Management (`useradd`, `usermod`, `userdel`)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `useradd <name>` | Create user account | `useradd john` | [Modifies System] Creates user, home folder (`/home/john`), and primary group. |
| `useradd -u <UID> -s <shell>` | Create with custom parameters | `useradd -u 1500 -s /bin/bash john` | [Modifies System] Assigns explicit numerical UID and default shell. |
| `useradd -r -s /sbin/nologin`| Create non-login service user | `useradd -r -s /sbin/nologin svc_db` | [Modifies System] System account (low UID, no interactive login shell). |
| `usermod -aG <group> <user>` | Add user to secondary group | `usermod -aG wheel,developers john` | [Modifies System] ⚠️ **Always use `-a` (append)**! Omitting `-a` wipes existing secondary groups! |
| `usermod -s <shell> <user>` | Change user login shell | `usermod -s /sbin/nologin john` | [Modifies System] Disables interactive terminal login for account. |
| `usermod -d <dir> -m <user>`| Move home directory | `usermod -d /data/john -m john` | [Modifies System] `-m` automatically relocates existing files to new path. |
| `usermod -L <user>` | Lock user account | `usermod -L john` | [Security] Prepend `!` to password hash in `/etc/shadow`, blocking login. |
| `usermod -U <user>` | Unlock user account | `usermod -U john` | [Security] Removes `!` from `/etc/shadow`, re-enabling password login. |
| `userdel <user>` | Delete user record only | `userdel john` | `⚠️ DESTRUCTIVE` Deletes account record; leaves home folder and mail spool intact. |
| `userdel -r <user>` | Delete user AND purge home | `userdel -r john` | `⚠️ DESTRUCTIVE` Permanently deletes user account, `/home/<user>`, and mailbox. |

---

## 👥 Group Management (`groupadd`, `groupmod`, `groupdel`)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `groupadd <group>` | Create a new group | `groupadd developers` | [Modifies System] Creates group entry in `/etc/group` and allocates new GID. |
| `groupadd -g <GID> <group>`| Create group with specific GID | `groupadd -g 2000 dbadmins` | [Modifies System] Explicitly assigns numerical GID. |
| `groupmod -n <new> <old>` | Rename an existing group | `groupmod -n devs developers` | [Modifies System] Changes group name while preserving existing GID. |
| `groupdel <group>` | Delete a group | `groupdel developers` | `⚠️ DESTRUCTIVE` Removes group. Fails safely if group is the primary group of any user. |
| `groups <user>` | List user's active groups | `groups student` | [Read-Only] Displays primary and all secondary group memberships. |
| `id <user>` | Display UID and all GIDs | `id student` | [Read-Only] Detailed summary of numerical UID, GID, and supplementary groups. |

---

## 🔑 Passwords and Aging Policies (`passwd`, `chage`)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `passwd` | Change current user's password | `passwd` | [Interactive] Requires current password verification for standard users. |
| `passwd <user>` | Set/reset another user's password | `passwd student` | [Root Only] Superuser can overwrite any user's password without prompting for old. |
| `passwd -l <user>` | Lock account password | `passwd -l student` | [Security] Locks account by disabling password authentication. |
| `passwd -u <user>` | Unlock account password | `passwd -u student` | [Security] Re-enables password authentication. |
| `chage -l <user>` | List password aging policies | `chage -l student` | [Read-Only] Shows expiration date, max days, warning days, and last change date. |
| `chage -M <days> <user>` | Set maximum password validity | `chage -M 90 student` | [Security] Enforces 90-day mandatory password rotation. |
| `chage -d 0 <user>` | Force password change at next login | `chage -d 0 student` | [Security] Sets last-changed to 0, forcing password reset immediately on login. |

---

## ⚡ Privilege Elevation: `su` vs. `su -` vs. `sudo`

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `su - root` | Switch to root with full login environment | `su -` | ✅ **RECOMMENDED**: Loads root's clean `$PATH`, `$HOME`, and shell environment. |
| `su root` | Switch to root retaining user environment | `su` | ❌ **RISKY**: Retains user's `$PATH` and working directory; may execute wrong binaries. |
| `sudo <command>` | Execute single command as root | `sudo service httpd restart` | [Audited] Authenticates with user's own password; logged to `/var/log/secure`. |
| `sudo -i` | Interactive root login shell via sudo | `sudo -i` | [Audited] Drops into root shell while preserving administrative audit trails. |
| `visudo` | Safely edit `/etc/sudoers` | `visudo` | [Root Only] ⚠️ Always use `visudo`; prevents syntax errors that cause lockouts! |

---

## 🗃️ Identity Databases Field Structure Reference

### `/etc/passwd` (7 Fields): `username:x:UID:GID:GECOS:home:shell`
- Field 1: Username (`student`)
- Field 2: Password placeholder (`x` = check `/etc/shadow`)
- Field 3: Numerical User ID (`UID 1001`)
- Field 4: Primary Group ID (`GID 1001`)
- Field 5: Comment / GECOS description (`BSIT Student`)
- Field 6: Home directory path (`/home/student`)
- Field 7: Login shell (`/bin/bash` or `/sbin/nologin`)

### `/etc/shadow` (9 Fields): `username:hash:last:min:max:warn:inactive:expire:reserved`
- Restricted permissions: `000` or `400` (readable only by root).
- Algorithm `$6$` indicates SHA-512 encryption.
- Leading `!!` or `*` indicates a locked or unconfigured password.
