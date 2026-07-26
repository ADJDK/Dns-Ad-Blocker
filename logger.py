import os
from datetime import datetime
from config import LOG_FILE

os.makedirs("logs", exist_ok=True)


def log_request(status, domain):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {status}: {domain}\n")