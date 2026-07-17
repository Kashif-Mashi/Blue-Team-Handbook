# Ubuntu Server Command Cheat Sheet

This document contains the most commonly used Ubuntu Server commands covered in this guide.

---

# Package Management

```bash
sudo apt update

sudo apt upgrade -y

sudo apt install <package>

sudo apt remove <package>

sudo apt purge <package>

sudo apt autoremove

sudo apt clean

sudo apt autoclean

apt search <package>

apt list --installed
```

---

# Network Commands

```bash
ip addr

ip route

ping google.com

hostnamectl
```

---

# Netplan

Open configuration

```bash
sudo nano /etc/netplan/50-cloud-init.yaml
```

Apply configuration

```bash
sudo netplan apply
```

Test configuration

```bash
sudo netplan try
```

---

# SSH

Check SSH

```bash
sudo systemctl status ssh
```

Enable SSH

```bash
sudo systemctl enable ssh
```

Start SSH

```bash
sudo systemctl start ssh
```

Restart SSH

```bash
sudo systemctl restart ssh
```

SSH Login

```bash
ssh username@192.168.56.10
```

Copy Files

```bash
scp file.txt username@192.168.56.10:/home/username/
```

---

# System Information

```bash
hostnamectl

lsb_release -a

uname -a

free -h

df -h
```

---

# Useful Commands

```bash
pwd

ls

ls -la

cd

mkdir

cp

mv

rm

cat

nano

grep

find
```

---

# VirtualBox Networking

Adapter 1

```
NAT
```

Adapter 2

```
Host-Only Adapter
```

---

# Recommended Lab IP Address

Ubuntu Server

```
192.168.56.10
```

Windows 11

```
192.168.56.20
```

Kali Linux

```
192.168.56.30
```

---

# Common Troubleshooting

## Update package list

```bash
sudo apt update
```

## Apply network changes

```bash
sudo netplan apply
```

## Restart SSH

```bash
sudo systemctl restart ssh
```

## Verify IP

```bash
ip addr
```

## Check Internet

```bash
ping google.com
```

## Check Disk Space

```bash
df -h
```

## Check Memory

```bash
free -h
```

---

# One-Line Summary

This cheat sheet provides a quick reference to the essential Ubuntu Server commands used throughout the guide.