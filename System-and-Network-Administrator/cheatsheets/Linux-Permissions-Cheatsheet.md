# Linux Permissions Cheatsheet

## Octal mapping

| Symbol | Binary | Octal |
|---|---:|---:|
| `---` | `000` | 0 |
| `--x` | `001` | 1 |
| `-w-` | `010` | 2 |
| `-wx` | `011` | 3 |
| `r--` | `100` | 4 |
| `r-x` | `101` | 5 |
| `rw-` | `110` | 6 |
| `rwx` | `111` | 7 |

| Command | Meaning |
|---|---|
| `chmod 640 file` | Owner rw, group r, others none |
| `chmod 600 file` | Owner rw only |
| `chmod 755 script.sh` | Owner rwx, group/others rx |
| `chmod 667 file` | Owner/group rw, others rwx |
| `chmod 777 file` | Everyone rwx; usually too permissive |
| `chmod u+x script.sh` | Add owner execute |
| `ls -l file` | Inspect mode and ownership |
| `chown user file` | Change owner, subject to privileges |
| `chgrp group file` | Change group, subject to privileges |

Choose least privilege. Directory permissions differ from regular-file permissions.
Related note: [File Permissions](../03-Linux-Fundamentals/04-File-Permissions.md)
