# Disk Management, Partitioning, RAID, and LVM Cheatsheet

> **Operational Quick Reference for Storage Administrators & Systems Engineers**  
> Companion detailed notes: [01-MBR-vs-GPT.md](../05-Disk-Management/01-MBR-vs-GPT.md) | [02-RAID-and-LVM.md](../05-Disk-Management/02-RAID-and-LVM.md)

---

## 🔍 Block Device & Partition Inspection

| Command Syntax | Operational Purpose | Key Output Details |
|---|---|---|
| `lsblk` | Tree view of block devices, sizes, and mount points | Displays drive hierarchy |
| `lsblk -f` | Display filesystems (FSTYPE), UUIDs, and mount points | Best command for filesystem triage |
| `fdisk -l` | List partition tables, sector sizes, and disklabel type | Shows `Disklabel type: dos` (MBR) or `gpt` |
| `gdisk -l /dev/sda` | Detailed GPT partition header and backup table check | Validates GPT CRC32 integrity |
| `df -h` | Mounted filesystem disk space usage in human-readable units | Shows partition full percentages |

---

## 🗄️ MBR vs. GPT Architecture Rules

| Feature | Master Boot Record (MBR) | GUID Partition Table (GPT) |
|---|---|---|
| **Maximum Disk Size** | **2.2 Terabytes (2.0 TiB)** | **9.4 Zettabytes (8.0 ZiB)** |
| **Addressing Width** | 32-bit Logical Block Addressing | 64-bit Logical Block Addressing |
| **Primary Partitions** | **4 Primary Partitions Max** | **128 Partitions natively** |
| **Exceeding 4 Partitions**| Requires Extended + Logical partitions (5+) | Obsolete (Not needed) |
| **Redundant Backup** | ❌ NONE (Single Point of Failure at Sector 0) | ✅ YES (Mirrored backup table at end of disk) |
| **Integrity Checks** | ❌ None | ✅ CRC32 Checksums on header and entries |
| **Firmware Association** | Legacy BIOS | Modern UEFI |
| **Partition Editor** | `fdisk` | `gdisk`, `parted` |

---

## 🛡️ RAID Levels Quick Reference

| RAID Level | Primary Architecture | Minimum Disks | Usable Storage Capacity | Fault Tolerance | Best For |
|:---:|---|:---:|:---:|:---:|---|
| **RAID 0** | Striping | 2 Disks | 100% (Sum of all drives) | **ZERO** (1 disk fails = 100% data loss) | Scratch cache, non-critical data |
| **RAID 1** | Mirroring | 2 Disks | 50% (Size of smallest drive) | 1 Disk failure in mirror | OS boot partitions (`/boot`, `/`) |
| **RAID 5** | Distributed Parity | 3 Disks | $(N - 1) \times \text{Size}$ | 1 Disk failure | Standard enterprise file servers |
| **RAID 6** | Dual Dist. Parity | 4 Disks | $(N - 2) \times \text{Size}$ | **2 Simultaneous Disk failures** | Large high-capacity storage arrays |
| **RAID 10** | Mirrored Stripes | 4 Disks | 50% ($\text{Sum} \div 2$) | Up to 1 disk per mirror pair | High-performance enterprise databases |

---

## 📦 LVM 3-Tier Command Reference Matrix

| Administrative Operation | Physical Volume (PV) | Volume Group (VG) | Logical Volume (LV) |
|---|---|---|---|
| **Create** | `pvcreate /dev/sdb /dev/sdc` | `vgcreate vg_data /dev/sdb /dev/sdc` | `lvcreate -L 100G -n lv_web vg_data` |
| **Scan Existing** | `pvscan` | `vgscan` | `lvscan` |
| **Display Brief Summary** | `pvs` | `vgs` | `lvs` |
| **Display Detailed Report**| `pvdisplay` | `vgdisplay` | `lvdisplay` |
| **Extend / Add Storage** | `pvresize /dev/sdb` | `vgextend vg_data /dev/sdd` | `lvextend -L +50G /dev/vg_data/lv_web`|
| **Remove / Delete** | `pvremove /dev/sdb` | `vgremove vg_data` | `lvremove /dev/vg_data/lv_web` |

---

## 🚀 Online Logical Volume & Filesystem Expansion

$$\text{Step 1: Extend LV Container}\quad \longrightarrow\quad \text{Step 2: Grow Underlying Filesystem (Online)}$$

```bash
# 1. Extend the Logical Volume by 50 GB:
lvextend -L +50G /dev/vg_data/lv_storage

# 2A. For XFS Filesystems (Takes MOUNT POINT as argument):
xfs_growfs /mount/point

# 2B. For ext4 Filesystems (Takes DEVICE NODE as argument):
resize2fs /dev/vg_data/lv_storage

# ALL-IN-ONE SHORTCUT (-r automatically triggers correct filesystem growth):
lvextend -r -L +50G /dev/vg_data/lv_storage
```

---

## 🛡️ Pre-Execution Storage Safety Directives

1. **Verify Block Device Names:** Storage letters (`sda`, `sdb`) can shift between reboots. Always run `lsblk -f` before executing partition or format commands!
2. **Never Blindly Format:** Formatting with `mkfs.xfs` or `mkfs.ext4` destroys existing partition data instantly.
3. **RAID is NOT a Backup:** Mirroring replicates accidental file deletion (`rm -rf`) and database corruption immediately across both drives.
