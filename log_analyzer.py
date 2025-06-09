import re
from collections import Counter
import argparse

LOG_FILE = "auth.log"  # default log file path
FAILED_PATTERN = re.compile(r"Failed password for .* from (\d{1,3}(?:\.\d{1,3}){3})")

def parse_failed_logins(path):
    """Parse a log file and count failed SSH login attempts per IP."""
    ips = []
    with open(path) as f:
        for line in f:
            match = FAILED_PATTERN.search(line)
            if match:
                ips.append(match.group(1))
    return Counter(ips)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze failed SSH login attempts from a log file.")
    parser.add_argument("logfile", nargs="?", default=LOG_FILE, help="Path to the log file (default: auth.log)")
    args = parser.parse_args()

    counts = parse_failed_logins(args.logfile)
    for ip, num in counts.most_common():
        print(f"{ip}: {num} failed attempts")
