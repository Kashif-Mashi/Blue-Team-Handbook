# Wazuh Installation Troubleshooting Runbook

> **Scenario**
>
> During the installation of **Wazuh 4.12** on **Ubuntu Server 22.04 LTS**, the installer failed while installing the Wazuh Dashboard and automatically rolled back the installation.
>
> This document records the complete troubleshooting process, commands used, root cause, and final resolution. It can be reused whenever a similar installation issue occurs.

---

# Environment

| Component | Value |
|-----------|-------|
| Operating System | Ubuntu Server 22.04.5 LTS |
| Wazuh Version | 4.12.0 |
| Installation Method | Official `wazuh-install.sh` |
| Virtualization | Oracle VirtualBox |
| Storage | Dynamically Allocated VDI |
| Deployment | All-in-One |

---

# Symptoms

During installation, the following errors appeared:

```text
ERROR: Wazuh dashboard installation failed
Write error: write (28): No space left on device
```

Later, the installer attempted to roll back the installation.

Additional errors included:

```text
/var/ossec/bin/wazuh-control: No such file or directory
/var/ossec/bin/wazuh-keystore: No such file or directory
```

The Wazuh Manager service could not start.

---

# Root Cause

The issue was caused by **multiple factors**:

- Ubuntu LVM was only using approximately half of the available virtual disk.
- The Wazuh Dashboard installation exhausted the available filesystem space.
- The installer automatically rolled back the installation.
- The rollback left the `wazuh-manager` package in an inconsistent state because the package removal scripts failed.

As a result:

- Package metadata still existed.
- Service files still existed.
- `/var/ossec` had already been removed.

---

# Troubleshooting Steps

## Step 1 — Check System Resources

Verify storage, memory, CPU, and LVM configuration.

```bash
lsblk
sudo vgdisplay
df -h
free -h
nproc
```

Purpose:

- Verify disk layout
- Check available storage
- Confirm memory
- Inspect LVM free space

---

## Step 2 — Review Installation Logs

Check the installer log for the first failure.

```bash
sudo head -10 /var/log/wazuh-install.log
sudo tail -10 /var/log/wazuh-install.log
sudo grep -i -n "ERROR\|CRITICAL\|FAILED\|Exception" /var/log/wazuh-install.log
```

Expected discovery:

```text
ERROR: Wazuh dashboard installation failed
Write error: write (28): No space left on device
```

---

## Step 3 — Verify Wazuh Service Status

Determine which services are running.

```bash
sudo systemctl status wazuh-manager.service
sudo systemctl status wazuh-indexer.service
ls -l /var/ossec/bin
dpkg -l | grep wazuh
apt-cache policy wazuh-manager
```

Purpose:

- Check Manager
- Check Indexer
- Verify installation files
- Verify package state

---

## Step 4 — Expand the Ubuntu LVM

The virtual disk had free space, but Ubuntu was not using it.

First extend the logical volume.

```bash
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h /
```

If additional virtual disk space was added later, expand the partition and physical volume first.

```bash
sudo growpart /dev/sda 3
sudo pvresize /dev/sda3
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

---

## Step 5 — Remove Broken Packages

Stop services.

```bash
sudo systemctl stop wazuh-manager wazuh-indexer wazuh-dashboard filebeat 2>/dev/null
```

Remove packages.

```bash
sudo apt purge -y wazuh-manager wazuh-indexer wazuh-dashboard filebeat
```

Force package removal.

```bash
sudo dpkg --purge --force-all wazuh-manager wazuh-indexer wazuh-dashboard filebeat 2>/dev/null
```

Remove remaining files.

```bash
sudo rm -rf \
/var/ossec \
/etc/wazuh-indexer \
/var/lib/wazuh-indexer \
/var/log/wazuh-indexer \
/etc/filebeat \
/usr/share/filebeat \
/etc/wazuh-dashboard \
/var/lib/wazuh-dashboard
```

Verify remaining packages.

```bash
dpkg -l | grep -i wazuh
```

---

## Step 6 — Repair Broken Package Removal Scripts

Inspect package scripts.

```bash
ls -la /var/lib/dpkg/info/wazuh-manager.*
```

Replace broken scripts.

```bash
echo -e '#!/bin/sh\nexit 0' | sudo tee /var/lib/dpkg/info/wazuh-manager.prerm
echo -e '#!/bin/sh\nexit 0' | sudo tee /var/lib/dpkg/info/wazuh-manager.postrm
```

Make executable.

```bash
sudo chmod +x \
/var/lib/dpkg/info/wazuh-manager.prerm \
/var/lib/dpkg/info/wazuh-manager.postrm
```

Force removal.

```bash
sudo dpkg --purge --force-all wazuh-manager
```

Verify package removal.

```bash
dpkg -l | grep -i wazuh
```

---

## Step 7 — Clean Previous Installation

Delete previous logs.

```bash
sudo rm -f /var/log/wazuh-install.log
```

Remove old installation archive.

```bash
rm -f ~/wazuh-install-files.tar
```

Repair dependencies.

```bash
sudo apt-get update
sudo apt-get install -f
```

---

## Step 8 — Reinstall Wazuh

Monitor storage usage in another terminal.

```bash
watch -n5 df -h /
```

Run the installer.

```bash
cd ~
sudo ./wazuh-install.sh -a
```

---

## Step 9 — Verify Installation

Verify services.

```bash
sudo systemctl is-active \
wazuh-manager \
wazuh-indexer \
wazuh-dashboard \
filebeat
```

Expected:

```text
active
active
active
active
```

Check for errors.

```bash
sudo grep -i -E "error|failed|critical" /var/log/wazuh-install.log
```

Retrieve dashboard credentials.

```bash
sudo tar -O -xvf wazuh-install-files.tar \
wazuh-install-files/wazuh-passwords.txt \
| grep -A1 "'admin'"
```

Retrieve server IP.

```bash
hostname -I
```

Open:

```text
https://<SERVER-IP>
```

---

# Lessons Learned

During this troubleshooting process we learned:

- LVM free space is not automatically used by Ubuntu.
- Dashboard installation requires sufficient free disk space.
- Automatic rollback may leave packages in an inconsistent state.
- `dpkg` may report packages as installed even after rollback.
- Installation logs should always be reviewed before attempting another installation.
- Monitoring available disk space during installation helps identify storage-related failures.

---

# Best Practices

- Allocate at least **30–50 GB** of virtual disk space for an all-in-one Wazuh deployment.
- Assign **4 CPU cores** and **8 GB RAM** when possible.
- Expand LVM after increasing virtual disk size.
- Verify storage before installation.
- Keep a copy of the generated `wazuh-install-files.tar`.
- Record the generated administrator credentials.

---

# References

- Wazuh Documentation
- Ubuntu LVM Documentation
- Oracle VirtualBox Documentation

---

# Conclusion

This runbook documents the complete troubleshooting path from:

```text
Disk Space Issue
        │
        ▼
Dashboard Installation Failure
        │
        ▼
Automatic Rollback
        │
        ▼
Broken Package State
        │
        ▼
LVM Expansion
        │
        ▼
Package Cleanup
        │
        ▼
Repair Removal Scripts
        │
        ▼
Clean Reinstallation
        │
        ▼
Successful Wazuh Deployment
```

This procedure can be reused whenever a similar Wazuh installation issue occurs.