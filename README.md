# SSH Brute Force Detector

## Objective
Detect SSH brute force attacks in real time by analyzing authentication logs and alerting when a single IP exceeds a failed login threshold.

## Environment
- Attacker: Kali Linux VM
- Target/Defender: Ubuntu 24.04 VM
- Network: Bridged Adapter (home network)
- Tools: Python3, OpenSSH, auth.log

## How It Works
1. Reads /var/log/auth.log continuously
2. Extracts IP addresses from failed login attempts
3. Counts failures per IP
4. Fires an alert if an IP exceeds 5 failed attempts

## Usage
python3 step2.py

## What I Learned
- How SSH authentication logs work
- Regex for log parsing
- Dictionary based IP tracking
- Real attacker vs defender lab setup
