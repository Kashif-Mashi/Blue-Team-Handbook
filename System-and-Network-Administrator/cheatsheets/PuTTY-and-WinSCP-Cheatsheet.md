# Remote Administration with PuTTY and WinSCP Cheatsheet

> **Operational Quick Reference for Windows-to-Linux Systems Administrators**  
> Companion detailed notes: [01-PuTTY-and-WinSCP.md](../06-Remote-File-Management/01-PuTTY-and-WinSCP.md)

---

## 🖥️ PuTTY Session Setup & Performance Optimization

```text
Host Name (or IP):  server01.lab.local  (or 192.168.1.50)
Port:               22                  (Standard SSH)
Connection Type:    SSH
```

### Essential Settings Before Saving Sessions:
1. **Prevent Idle Dropped Connections (Keepalive):**
   - Navigate: **Connection** (left pane) ──> Set **Seconds between keepalives** to **`30`**.
   - Prevents corporate firewalls from dropping inactive terminal sessions.
2. **Fix Corrupted Terminal Characters (UTF-8):**
   - Navigate: **Window** ──> **Translation** ──> Set **Remote character set** to **`UTF-8`**.
   - Ensures line-drawing characters in `top`, `ncurses`, and `htop` render properly.
3. **Save Session:** Navigate back to **Session** ──> Type descriptive label ──> Click **Save**.

---

## 🔑 SSH Public Key Authentication with PuTTYgen

$$\text{Private Key (.ppk on Windows Laptop)}\quad \longleftrightarrow\quad \text{Public Key (authorized\_keys on Linux Server)}$$

### Step 1: Generate Keypair (PuTTYgen)
1. Open **PuTTYgen** ──> Select **Ed25519** (modern elliptic curve) or **RSA (4096 bits)**.
2. Click **Generate** ──> Move mouse randomly to generate entropy.
3. Set a strong **Key passphrase**.
4. Click **Save private key** (`my_key.ppk`).
5. Copy the formatted public key from the top box: `ssh-ed25519 AAAA...`.

### Step 2: Deploy Public Key to Linux Server
```bash
# 1. Create hidden .ssh directory with strict permissions:
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 2. Append the public key string into authorized_keys:
echo "ssh-ed25519 AAAA... client_laptop" >> ~/.ssh/authorized_keys

# 3. Enforce mandatory read-only permissions (OpenSSH rejects keys if too wide!):
chmod 600 ~/.ssh/authorized_keys
```

### Step 3: Attach Private Key in PuTTY
- Navigate: **Connection** ──> **SSH** ──> **Auth** ──> **Credentials**.
- Browse and select `my_key.ppk` under **Private key file for authentication**.
- Save the session!

---

## 📁 WinSCP: Dual-Pane Secure SFTP File Transfers

| Transfer Mode | When to Use | Line Ending Behavior | Danger if Wrong Mode Used |
|---|---|---|---|
| **Binary Mode** | Images, videos, `.tar.gz`, ISOs, `.sql` dumps, compiled binaries | Bit-for-bit exact copy (0 modifications) | None; exact replica |
| **Text (ASCII) Mode**| Shell scripts (`.sh`), text configuration files (`.conf`, `.txt`) | Automatically converts Windows `CRLF` (`\r\n`) to Linux `LF` (`\n`) | Corrupts binary files (images/zips)! |

### The "Bad Interpreter `^M`" Fix on Linux:
If a shell script created in Windows fails to run on Linux with `/bin/bash^M: bad interpreter`:
```bash
dos2unix script.sh
```

---

## 🚨 Remote Connection Error Troubleshooting Matrix

| Error Message | Likely Root Cause | Immediate Diagnostic & Remediation Steps |
|---|---|---|
| **Network error: Connection timed out** | - Firewall dropping port 22<br/>- Target IP is incorrect<br/>- Server powered off | 1. Ping the server IP: `ping 192.168.1.50`<br/>2. Check intermediate VPN connection<br/>3. Verify AWS/Azure security group rules |
| **Network error: Connection refused** | - OpenSSH daemon (`sshd`) is stopped<br/>- Server listening on custom port | 1. Log into local server console<br/>2. Check status: `systemctl status sshd`<br/>3. Start service: `systemctl start sshd` |
| **Access Denied** | - Incorrect password<br/>- User account locked in shadow<br/>- Direct root login disabled | 1. Check `/var/log/secure` for auth failures<br/>2. Unlock user: `usermod -U username`<br/>3. Log in as regular user and run `sudo` |
| **Server key does not match registry cache** | - Host reinstalled (Legitimate)<br/>- Man-in-the-Middle attack (Malicious) | 1. Verify host key fingerprint with administrator<br/>2. If legitimate, delete stale registry key |
| **Authentication refused: bad ownership or modes** | - Permissions too wide on `~/.ssh` or `authorized_keys` | 1. Run `chmod 700 ~/.ssh`<br/>2. Run `chmod 600 ~/.ssh/authorized_keys` |
