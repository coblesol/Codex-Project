# Cybersecurity Lab Project

This project provides a basic home lab for practicing vulnerability assessment and system hardening techniques in a safe environment. The instructions assume you are running the lab within your own network using virtualization software such as VirtualBox, VMware, or Hyper-V.

## Lab Setup

1. **Create two virtual machines (VMs):**
   - **Target VM:** An operating system you want to secure (e.g., Ubuntu Server or Windows Server). Install a few common services such as SSH, a web server (Apache or Nginx), and an optional database.
   - **Scanner VM:** A machine that will run the scanning tools. Use a lightweight OS (e.g., another Ubuntu VM) with Python installed.

2. **Isolate the VMs:** Place both VMs on a private host-only or internal network so the scans do not affect other devices.

3. **Ensure you have administrator/root access** on both VMs so you can configure services and view logs.

## Custom Port Scanner

A simple Python-based port scanner is included in `port_scanner.py`. It attempts TCP connections to a list of ports and reports which ones are open.

```
python3 port_scanner.py <target_ip>
```

Example output:

```
[+] Scanning 10.0.0.5
Port 22 is open
Port 80 is open
Port 443 is closed
```

Use this scanner from the Scanner VM to probe the Target VM. You can edit the port list within the script to include additional services.

## Detecting Misconfigurations

After scanning, review the open ports and running services on the Target VM. Look for:

- Unnecessary or outdated services running.
- Weak or default credentials on any services.
- Services running as administrator/root when not required.
- Incomplete or missing firewall rules.

Use standard system logs (`/var/log` on Linux, Event Viewer on Windows) to check for suspicious login attempts or error messages.

## Hardening Checklist

See [`hardening_checklist.md`](hardening_checklist.md) for specific steps. Highlights include:

- Apply the latest system updates and security patches.
- Configure strong, unique passwords and consider key-based authentication for SSH.
- Disable or remove services you do not need.
- Set up a host-based firewall (such as `ufw` on Ubuntu or Windows Defender Firewall) to allow only required ports.
- Enable automatic updates where feasible.

## Optional Extensions

- **Log Analysis:** Build a Python script that parses authentication logs (e.g., `/var/log/auth.log`) and reports failed login attempts.
- **Vulnerability Scanning Tools:** Install open-source scanners like `nmap` or `OpenVAS` on your Scanner VM to perform more comprehensive checks.
- **Configuration Management:** Explore tools such as Ansible or Puppet to apply hardening steps across multiple machines.
- **Container Security:** Set up Docker containers and experiment with scanning container images for vulnerabilities.

By following this project, you can demonstrate foundational skills for Security+ or entry-level system administration roles.
