import argparse
import re

# Regular expressions for common failed SSH login patterns
PATTERNS = [
    re.compile(r"Failed password for"),
    re.compile(r"Invalid user"),
    re.compile(r"Failed publickey for"),
]

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze SSH logs for failed login attempts")
    parser.add_argument("log_file", help="Path to the SSH log file")
    return parser.parse_args()


def analyze_log(file_path):
    suspicious = []
    with open(file_path, errors="ignore") as fh:
        for line in fh:
            if any(p.search(line) for p in PATTERNS):
                suspicious.append(line.rstrip())
    return suspicious


def main():
    args = parse_args()
    entries = analyze_log(args.log_file)
    print(f"Found {len(entries)} failed SSH login attempts.")
    if entries:
        print("Suspicious entries:")
        for entry in entries:
            print(entry)


if __name__ == "__main__":
    main()
