import re

failed = {}

with open("/var/log/auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                if ip in failed:
                    failed[ip] += 1
                else:
                    failed[ip] = 1

for ip,count in failed.items():
    print(f"{ip} -> {count} failed attempts")
    if count>=5:
        print(f"alert: Brute force detected from {ip}!")
