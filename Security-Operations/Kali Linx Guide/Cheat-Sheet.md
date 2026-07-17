# Kali Linux Command Cheat Sheet

This cheat sheet contains the most commonly used commands covered throughout this guide.

---

# System Information

```bash
hostnamectl
uname -a
cat /etc/os-release
lsb_release -a
```

---

# Networking

```bash
ip addr
ip route
ping google.com
ss -tln
```

---

# Package Management

```bash
sudo apt update
sudo apt full-upgrade -y
sudo apt install <package>
sudo apt remove <package>
sudo apt purge <package>
sudo apt autoremove
sudo apt clean
sudo apt autoclean
apt search <package>
apt show <package>
```

---

# SSH

```bash
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl restart ssh
sudo systemctl enable ssh
ssh username@IP
scp file.txt username@IP:/home/username/
```

---

# Disk & Memory

```bash
df -h
du -sh *
free -h
top
htop
```

---

# File Management

```bash
pwd
ls
ls -la
cd
mkdir
cp
mv
rm
find
cat
nano
vim
```

---

# User Management

```bash
whoami
id
passwd
sudo adduser username
sudo deluser username
```

---

# Useful Security Tools

| Tool | Purpose |
|------|----------|
| Nmap | Network Scanning |
| Wireshark | Packet Analysis |
| Burp Suite | Web Application Testing |
| Gobuster | Directory Enumeration |
| FFUF | Web Fuzzing |
| John the Ripper | Password Auditing |
| Hydra | Login Auditing |
| Hashcat | Password Recovery |
| Ghidra | Reverse Engineering |
| Metasploit | Security Testing Framework |

---

# Useful Maintenance Commands

```bash
sudo apt update
sudo apt full-upgrade
sudo apt autoremove
sudo apt clean
sudo reboot
sudo shutdown now
```

---

# Useful Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + Alt + T | Open Terminal |
| Ctrl + C | Stop Running Command |
| Ctrl + L | Clear Terminal |
| Ctrl + R | Search Command History |
| Tab | Auto Complete |

---

Keep this cheat sheet open while following the guide or working in your cybersecurity lab.