import re
from datetime import datetime, timedelta
from collections import defaultdict

THRESHOLD = 5
WINDOW = 60

failed = defaultdict(list)

with open("/var/log/auth.log","r") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                now = datetime.now()
                failed[ip].append(now)

                cutoff = now - timedelta(seconds=WINDOW)
                failed[ip] = [t for t in failed[ip] if t > cutoff]

                count = len(failed[ip])
                if count >= THRESHOLD:
                    print(f"ALERT: {ip} has {count} failed attempts in {WINDOW}s!")
