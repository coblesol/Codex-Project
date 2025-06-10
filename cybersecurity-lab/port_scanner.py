#!/usr/bin/env python3
"""Simple TCP port scanner for educational use.

Scan a target host for a list of common ports and report which are open.
Only run this against systems you own or have permission to test.
"""

import socket
import sys
from typing import Iterable, Tuple

COMMON_PORTS = [22, 23, 80, 443, 3389]


def scan_port(host: str, port: int) -> Tuple[int, bool]:
    """Attempt to connect to a TCP port. Returns (port, is_open)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        return port, result == 0


def run_scan(host: str, ports: Iterable[int] = COMMON_PORTS) -> None:
    print(f"[+] Scanning {host}")
    for port in ports:
        _, is_open = scan_port(host, port)
        status = "open" if is_open else "closed"
        print(f"Port {port} is {status}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    run_scan(target_ip)
