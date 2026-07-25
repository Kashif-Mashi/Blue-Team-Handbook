# Linux Cheat Sheet

A quick reference for commonly used Linux commands.

---

# Navigation

| Command | Description |
|----------|-------------|
| pwd | Print current directory |
| ls | List files |
| ls -la | List hidden files |
| cd | Change directory |
| cd .. | Go back one directory |
| cd ~ | Go to home directory |
| clear | Clear terminal |

---

# File Management

| Command | Description |
|----------|-------------|
| touch | Create file |
| mkdir | Create directory |
| rm | Remove file |
| rm -r | Remove directory |
| cp | Copy files |
| mv | Move or rename files |
| cat | Display file |
| less | View file |
| head | First lines |
| tail | Last lines |

---

# File Permissions

| Command | Description |
|----------|-------------|
| chmod | Change permissions |
| chown | Change owner |
| chgrp | Change group |
| umask | View default permissions |

Common Permission Values

| Value | Meaning |
|------|---------|
| 777 | Full access |
| 755 | Recommended for scripts |
| 644 | Recommended for files |
| 600 | Private file |

---

# Users

| Command | Description |
|----------|-------------|
| whoami | Current user |
| id | User information |
| groups | User groups |
| passwd | Change password |
| useradd | Create user |
| userdel | Delete user |
| sudo | Run as administrator |

---

# Processes

| Command | Description |
|----------|-------------|
| ps aux | View processes |
| top | Real-time monitoring |
| htop | Interactive monitoring |
| kill PID | Kill process |
| pkill | Kill by name |
| pgrep | Find process |

---

# Services

| Command | Description |
|----------|-------------|
| systemctl status | Service status |
| systemctl start | Start service |
| systemctl stop | Stop service |
| systemctl restart | Restart service |
| systemctl enable | Enable at boot |

---

# Networking

| Command | Description |
|----------|-------------|
| ip addr | IP addresses |
| ip route | Routing table |
| ping | Connectivity test |
| ss -tuln | Listening ports |
| curl | HTTP request |
| wget | Download files |
| dig | DNS lookup |
| nslookup | DNS lookup |
| traceroute | Route tracing |
| ssh | Remote login |

---

# Logs

| Command | Description |
|----------|-------------|
| journalctl | System logs |
| journalctl -f | Live logs |
| tail -f | Live file |
| grep | Search logs |
| dmesg | Kernel logs |

---

# Packages

| Command | Description |
|----------|-------------|
| apt update | Update package list |
| apt upgrade | Upgrade packages |
| apt install | Install package |
| apt remove | Remove package |
| apt autoremove | Remove unused packages |
| apt search | Search packages |

---

# Bash

| Command | Description |
|----------|-------------|
| echo | Print text |
| read | User input |
| chmod +x | Make executable |
| ./script.sh | Run script |
| echo $? | Exit code |

---

# Firewall

| Command | Description |
|----------|-------------|
| ufw status | Firewall status |
| ufw enable | Enable firewall |
| ufw disable | Disable firewall |
| ufw allow ssh | Allow SSH |

---

# Useful Directories

| Directory | Purpose |
|------------|---------|
| /home | User files |
| /etc | Configuration |
| /var | Logs |
| /usr | Programs |
| /bin | Essential binaries |
| /tmp | Temporary files |
| /opt | Optional software |

---

# Blue Team Favorites

```bash
ps aux

ss -tuln

journalctl -f

tail -f /var/log/auth.log

grep "Failed" /var/log/auth.log

systemctl status ssh

ip addr

whoami

id

sudo apt update
```