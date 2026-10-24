# PuTTY and WinSCP Cheatsheet

| Item | Reminder |
|---|---|
| PuTTY | Remote terminal access, commonly over SSH |
| WinSCP | File transfer, commonly using SFTP |
| Hostname/IP | Authorized server address |
| Port 22 | Default SSH port unless configured otherwise |
| Username | Authorized Linux account |
| Host key | Verify identity; investigate unexpected changes |
| SFTP | File transfer over SSH |

## Connection checklist
1. Confirm address and SSH port.
2. Confirm the server's SSH service is running.
3. Use authorized credentials or an approved key.
4. Verify host key, especially on first connection.
5. Check remote directory permissions.
6. Do not store passwords in shared notes.

Related note: [PuTTY and WinSCP](../06-Remote-File-Management/01-PuTTY-and-WinSCP.md)
