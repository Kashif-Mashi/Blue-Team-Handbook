# Wazuh Command Cheat Sheet

---

# Service Management

```bash
sudo systemctl status wazuh-manager
sudo systemctl restart wazuh-manager
sudo systemctl start wazuh-manager
sudo systemctl enable wazuh-manager
```

---

# Dashboard

```bash
sudo systemctl status wazuh-dashboard
sudo systemctl restart wazuh-dashboard
```

---

# Indexer

```bash
sudo systemctl status wazuh-indexer
sudo systemctl restart wazuh-indexer
```

---

# View Logs

```bash
sudo tail -f /var/ossec/logs/ossec.log
```

---

# System Information

```bash
hostnamectl
ip addr
ip route
df -h
free -h
```

---

# Package Management

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Check Running Services

```bash
systemctl --type=service
```

---

# Network

```bash
ping google.com
ping 192.168.56.30
ss -tln
```

---

# Common File Locations

```text
/var/ossec/
/var/ossec/etc/
/var/ossec/logs/
/etc/systemd/system/
```

---

# Useful Maintenance

```bash
sudo reboot
sudo shutdown now
sudo journalctl -xe
```

---

# Important Commands

```bash
curl
chmod
systemctl
journalctl
hostnamectl
ip
ss
tail
```