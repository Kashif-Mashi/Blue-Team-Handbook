# Disk Partitioning, RAID, and LVM Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guides:** [01-MBR-vs-GPT.md](../05-Disk-Management/01-MBR-vs-GPT.md) | [02-RAID-and-LVM.md](../05-Disk-Management/02-RAID-and-LVM.md) | [Cheatsheets Index](README.md)

---

## 🔍 Block Device & Filesystem Inspection (Non-Destructive)

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `lsblk` | Block device hierarchy | `lsblk -f` | [Read-Only] Lists all disks, partitions, LVMs, UUIDs, and mount points. |
| `fdisk -l` | List partition tables | `fdisk -l` | [Read-Only] Displays MBR/GPT sector sizes, disk geometry, and identifiers. |
| `blkid` | Display UUIDs and filesystems| `blkid /dev/sda1` | [Read-Only] Essential for finding reliable UUIDs for `/etc/fstab`. |
| `df -h` | Mounted disk usage | `df -h` | [Read-Only] Shows total, used, and available space in human-readable units. |
| `cat /proc/mdstat` | Check software RAID status | `cat /proc/mdstat` | [Read-Only] Real-time Linux kernel software RAID status. |

---

## 🛠️ Partition Table Management (`fdisk`, `gdisk`, `parted`)

> 🚨 **SAFETY RULE:** Never assume a drive is named `/dev/sdb` or `/dev/hdc`. Verify device identifiers with `lsblk` before running these tools!

| Command / Pattern | Purpose | Target Standard | Important Note |
|---|---|---|---|
| `fdisk /dev/sdb` | Interactive MBR partitioner | MBR (disks < 2.2 TB) | `⚠️ DESTRUCTIVE` Write changes only when pressing `w`; abort with `q`. |
| `gdisk /dev/sdb` | Interactive GPT partitioner | GPT (modern / > 2.2 TB) | `⚠️ DESTRUCTIVE` GPT counterpart to fdisk. `w` writes partition table to disk. |
| `parted /dev/sdb print` | Print partition table geometry | MBR or GPT | [Read-Only] Displays partition labels without altering data. |
| `parted /dev/sdb mklabel gpt` | Create fresh GPT disk label | GPT | `🚨 DATA WIPE` Immediately wipes all existing partitions on target disk! |

---

## 🗄️ Logical Volume Management (LVM) Workflow

### 1. Physical Volumes (PV)
| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `pvcreate <device>` | Initialize disk/partition for LVM | `pvcreate /dev/sdb1` | [Modifies Disk] Writes LVM metadata label to raw partition. |
| `pvs` | Brief Physical Volume summary | `pvs` | [Read-Only] Shows PV name, VG membership, size, and free space. |
| `pvdisplay <device>` | Detailed Physical Volume info | `pvdisplay /dev/sdb1` | [Read-Only] Shows total PE count, PE size, and UUID. |

### 2. Volume Groups (VG)
| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `vgcreate <vg_name> <pv>` | Create new Volume Group pool | `vgcreate vg_data /dev/sdb1` | [Modifies System] Groups one or more PVs into a unified storage pool. |
| `vgs` | Brief Volume Group summary | `vgs` | [Read-Only] Shows total capacity and unallocated free extents. |
| `vgdisplay <vg_name>` | Detailed Volume Group info | `vgdisplay vg_data` | [Read-Only] Shows Physical Extent (PE) allocation size (default: 4MB). |
| `vgextend <vg> <new_pv>` | Expand VG with another disk | `vgextend vg_data /dev/sdc1` | [Expands Pool] Adds capacity from an additional physical disk into pool. |

### 3. Logical Volumes (LV)
| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `lvcreate -L <size> -n <lv> <vg>` | Create Logical Volume by size | `lvcreate -L 20G -n lv_web vg_data` | [Modifies System] Carves block slice from pool (`/dev/vg_data/lv_web`). |
| `lvcreate -l 100%FREE -n <lv> <vg>`| Allocate all remaining space | `lvcreate -l 100%FREE -n lv_data vg_data`| [Modifies System] Uses 100% of unallocated Physical Extents. |
| `lvs` | Brief Logical Volume summary | `lvs` | [Read-Only] Lists all LVs, active sizes, and parent Volume Groups. |
| `lvdisplay <lv_path>` | Detailed Logical Volume info | `lvdisplay /dev/vg_data/lv_web`| [Read-Only] Displays volume block mapping and UUID. |
| `lvextend -L +<size> <lv_path>` | Expand Logical Volume live | `lvextend -L +10G /dev/vg_data/lv_web` | [Non-Destructive] Adds container space. Requires filesystem resize! |

---

## 💽 Filesystem Formatting & Resizing

| Command / Pattern | Purpose | Example | Important Note |
|---|---|---|---|
| `mkfs.ext4 <device>` | Format as ext4 (RHEL 6 default) | `mkfs.ext4 /dev/vg_data/lv_web` | `🚨 DATA WIPE` Formats block device. Wipes all preexisting data! |
| `mkfs.xfs <device>` | Format as XFS (RHEL 8/9 default) | `mkfs.xfs /dev/vg_data/lv_web` | `🚨 DATA WIPE` Enterprise standard for high-performance storage. |
| `resize2fs <lv_path>` | Expand ext4 filesystem online | `resize2fs /dev/vg_data/lv_web` | [Non-Destructive] Run *after* `lvextend` to expand ext4 filesystem live. |
| `xfs_growfs <mount_point>` | Expand XFS filesystem online | `xfs_growfs /var/www` | [Non-Destructive] ⚠️ Targets the **mount point**, not the device path! XFS cannot shrink! |

---

## 📌 Mounting and `/etc/fstab` Persistence

```bash
# Mount a logical volume manually
mount /dev/vg_data/lv_web /var/www/html

# Unmount a filesystem safely
umount /var/www/html

# Test /etc/fstab entries safely without rebooting
mount -a
```

### Typical `/etc/fstab` Format
```text
# <device_or_UUID>                 <mount_point>   <fstype>   <options>   <dump> <pass>
/dev/mapper/vg_data-lv_web         /var/www/html   ext4       defaults    1      2
UUID=a1b2c3d4-e5f6-7890-abcd       /data           xfs        defaults    0      0
```
