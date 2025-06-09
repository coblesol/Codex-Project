# Codex Project

## Log Analyzer

This repository includes a simple Python script to analyze system authentication logs for repeated failed SSH login attempts. The tool can help identify suspicious activity by summarizing how many times each IP address has failed to authenticate.

### Usage

1. Place or specify a log file, such as `/var/log/auth.log` or a custom log sample.
2. Run the analyzer and optionally provide the path to your log file:

```bash
python log_analyzer.py /path/to/auth.log
```

The script outputs each IP address and the number of failed login attempts found in the log.
