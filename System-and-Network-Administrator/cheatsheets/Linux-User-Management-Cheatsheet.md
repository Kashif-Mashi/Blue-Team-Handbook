# Linux User Management Cheatsheet

| Command | Purpose |
|---|---|
| `whoami` | Effective username |
| `id username` | UID and group IDs |
| `groups username` | Group memberships |
| `getent passwd username` | Query account database |
| `useradd username` | Create account on typical systems |
| `passwd username` | Set/change password interactively |
| `groupadd groupname` | Create group |
| `usermod -aG group username` | Append supplementary group |
| `chage -l username` | Password-aging info where supported |

Account commands may require administrative privileges and vary by configuration. Verify the target account and approved workflow. Avoid manually editing `/etc/passwd` or `/etc/shadow`.
Related note: [User Management](../03-Linux-Fundamentals/05-User-Management.md)
