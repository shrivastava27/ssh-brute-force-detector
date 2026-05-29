# SSH Brute Force Detector

## Objective
Detect SSH brute force attacks in real time by analyzing 
authentication logs and automatically blocking attackers 
via iptables firewall rules.

## Environment
- Attacker: Kali Linux VM
- Defender: Ubuntu 24.04 LTS VM
- Network: Bridged Adapter
- Tools: Python3, OpenSSH, iptables

## How It Works
1. Reads /var/log/auth.log for failed SSH logins
2. Extracts attacker IP using regex
3. Tracks failures per IP within a 60 second window
4. Fires alert if failures exceed threshold (default: 5)
5. Automatically blocks attacker IP via iptables
6. Prevents duplicate blocking using a set

## Usage
sudo python3 step2.py

## Detection Logic
- Threshold: 5 failed attempts
- Time Window: 60 seconds
- Blocking: iptables DROP rule on INPUT chain

## What I Learned
- Python file handling and log parsing
- Regex for IP extraction
- defaultdict and set data structures
- datetime for time window detection
- subprocess to automate iptables commands
- Real attacker vs defender lab setup
- Git version control workflow

## Lab Setup
- Simulated brute force using manual SSH attempts from Kali
- Verified firewall rules using: sudo iptables -L INPUT -n
