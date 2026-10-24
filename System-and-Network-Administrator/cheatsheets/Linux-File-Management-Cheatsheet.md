# Linux File Management Cheatsheet

| Task | Command | Caution |
|---|---|---|
| Show location | `pwd` | Check before relative operations |
| List files | `ls -la` | Includes hidden names |
| Create file | `touch notes.txt` | Existing file timestamp may change |
| Create directory | `mkdir notes` | Parent must exist unless options are used |
| Read file | `cat notes.txt` | Large output may flood terminal |
| Copy | `cp source.txt copy.txt` | Check before overwriting |
| Move/rename | `mv old.txt new.txt` | Verify destination |
| Replace content | `echo "text" > file.txt` | `>` overwrites |
| Append content | `echo "text" >> file.txt` | Appends |
| Remove empty directory | `rmdir folder` | Must be empty |
| Remove file | `rm file.txt` | Deletion may be difficult to reverse |
| Find by name | `find /path -name '*.txt'` | Limit search scope |

Shell wildcards are not regex. Be careful with wildcards and deletion.
Related note: [File Management](../03-Linux-Fundamentals/03-File-Management.md)
