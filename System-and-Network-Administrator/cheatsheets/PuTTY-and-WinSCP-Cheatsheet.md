# PuTTY and WinSCP Remote Administration Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [01-PuTTY-and-WinSCP.md](../06-Remote-File-Management/01-PuTTY-and-WinSCP.md) | [Cheatsheets Index](README.md)

---

## 🖥️ Part 1: PuTTY Configuration Steps

| Configuration Step | Category in PuTTY | Parameter & Value | Operational Purpose |
|---|---|---|---|
| **Set Destination** | Session | **Host Name:** `<Server_IP>`, **Port:** `22` | Specifies target Linux server and SSH port. |
| **Select Protocol** | Session | **Connection type:** `SSH` | Ensures encrypted transport. |
| **Save Profile** | Session | **Saved Sessions:** `<Label>` -> Click **Save** | Stores IP and connection parameters for one-click launch. |
| **Increase Scrollback** | Window | **Lines of scrollback:** `10000` | Prevents lost terminal output when running long diagnostic scripts. |
| **Attach Private Key**| Connection -> SSH -> Auth | **Private key file:** Browse to `<key.ppk>` | Enables passwordless public-key authentication. |
| **Set Keepalive** | Connection | **Seconds between keepalives:** `30` | Sends null packets to prevent firewall session dropouts during idle periods. |

---

## 🔑 Part 2: PuTTYgen Key Pair Generation Workflow

1. **Launch PuTTYgen**: Select **RSA** (2048 or 4096 bits) or **Ed25519**.
2. **Generate Entropy**: Click **Generate** and move your mouse randomly across the window.
3. **Set Passphrase**: Enter a strong **Key passphrase** to protect the `.ppk` file on Windows.
4. **Save Private Key**: Click **Save private key** to generate your `.ppk` file.
5. **Copy Public Key**: Copy the plaintext single-line string from the box labeled *Public key for pasting into OpenSSH authorized_keys file*:
   ```text
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3... rsa-key-admin
   ```

### Linux Server Key Deployment & Strict Permissions
Execute on the Linux server as the target user:
```bash
# 1. Create .ssh directory with strict permissions
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 2. Append the public key string copied from PuTTYgen
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3... rsa-key-admin" >> ~/.ssh/authorized_keys

# 3. Enforce strict permissions on the authorized_keys file
chmod 600 ~/.ssh/authorized_keys
```
> ⚠️ **StrictModes Enforcement:** If `~/.ssh` is `777` or `authorized_keys` is group-writable, OpenSSH will silently **refuse to use the key** and fallback to prompting for a password!

---

## 📂 Part 3: WinSCP SFTP Configuration & Operations

| Task | Configuration / Action | Shortcut | Operational Note |
|---|---|:---:|---|
| **New Session** | Protocol: `SFTP`, Port: `22`, Host: `<IP>` | `Ctrl + N` | Establishes encrypted dual-pane file manager session. |
| **Attach Key** | Advanced -> SSH -> Authentication -> Attach `.ppk` | — | Uses PuTTY private key for SFTP authentication. |
| **Copy File** | Drag between panes, or press **F5** | `F5` | Uploads from left (Windows) to right (Linux) or vice versa. |
| **Move File** | Move selected file between panes | `F6` | Relocates file across systems. |
| **New Folder** | Create new remote directory | `F7` | Prompts for folder name on active pane. |
| **Delete File** | Delete selected remote file | `F8` | `⚠️ DESTRUCTIVE` Permanently unlinks file on server. |
| **Direct Edit** | Double-click remote text file | `F4` | Opens file in internal editor; saving updates remote server directly. |
| **Check Permissions**| Right-click file -> **Properties** | — | Graphical review of octal permissions (`0644`), UID, and GID. |

---

## ⚠️ CRLF vs. LF Line Ending Warning

- Windows text editors format newlines as **CRLF** (`\r\n`), while Linux uses **LF** (`\n`).
- If you edit a Bash script on Windows and upload it via WinSCP, Linux will fail to run it with:
  ```text
  /bin/bash^M: bad interpreter: No such file or directory
  ```
- **Fix in WinSCP**: In Preferences -> Transfer, set transfer mode to **Text/ASCII** for `*.sh`, `*.conf`, `*.py`.
- **Fix on Linux**: Run `dos2unix <script.sh>` or `tr -d '\r' < script.sh > clean_script.sh`.

---

## 🛡️ Remote Administration Security Checklist

```text
[ ] OpenSSH service running: service sshd status (RHEL 6) / systemctl status sshd
[ ] Host firewall allows port 22: iptables -L -n / firewall-cmd --list-all
[ ] SSH key authentication tested successfully
[ ] Root login disabled in /etc/ssh/sshd_config: PermitRootLogin no
[ ] Password authentication disabled in /etc/ssh/sshd_config: PasswordAuthentication no
[ ] Configuration reloaded: service sshd reload / systemctl reload sshd
```
