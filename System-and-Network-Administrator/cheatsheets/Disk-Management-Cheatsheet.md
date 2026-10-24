# Disk Management Cheatsheet

## Inspect first

| Command | Purpose |
|---|---|
| `lsblk` | List block devices |
| `fdisk -l` | List partition tables where supported |
| `df -h` | Show mounted filesystem usage |
| `cat /proc/partitions` | Kernel partition information on Linux |
| `hostname` | Confirm current machine |

## Concepts
- **MBR:** older partition-table scheme with traditional limits.
- **GPT:** modern partition-table scheme with backup metadata.
- **RAID 1:** mirrors data across members.
- **PV:** LVM physical volume.
- **VG:** LVM volume group/storage pool.
- **LV:** LVM logical volume.

**Warning:** Partitioning, RAID creation, LVM initialization, and formatting can destroy data. Verify the machine and target disk, back up important data, and follow the exact procedure. Never assume `/dev/hdc` exists.

Related notes: [MBR vs GPT](../05-Disk-Management/01-MBR-vs-GPT.md) · [RAID and LVM](../05-Disk-Management/02-RAID-and-LVM.md)
