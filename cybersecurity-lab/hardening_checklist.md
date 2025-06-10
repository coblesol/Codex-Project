# System Hardening Checklist

Use this list as a starting point for securing your lab systems. Adjust according to your environment and risk tolerance.

## Accounts and Authentication
- Enforce strong, unique passwords for all user accounts.
- Disable or lock unused accounts.
- Configure multi-factor authentication (where available).
- Use key-based authentication for SSH instead of passwords.

## Software and Updates
- Keep the operating system and installed packages up to date.
- Remove unnecessary software packages and services.

## Network Configuration
- Enable and configure a host-based firewall to allow only required inbound/outbound traffic.
- Disable unused network services and ports.
- For remote administration, restrict access to specific IP addresses.

## Logging and Monitoring
- Enable system logging and regularly review logs for suspicious activity.
- Store logs securely and consider using a centralized log server for larger environments.

## File System and Permissions
- Grant the minimum required privileges to files and directories.
- Use file integrity monitoring tools to detect unauthorized changes.

## Backups
- Maintain regular backups of critical data and test restore procedures.

This checklist is not exhaustive but covers common steps to improve the security posture of a typical server or workstation.
