#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Returns true if a computer has a pending reboot."""
    return os.path.exists("/run/reboot/-required")
def check_disk_full(disk,min_gb,min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return true
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/",min_gb=2,min_percent=10)

def main():
    checks=[
    (check_reboot, "Pending reboot"),
    (check_root_full, "Root partition full"),
    ]
    everthing_ok = True

    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everthing_ok:
            sys.exit(1)

    print("Everthing Ok.")
    sys.exit(0)

main()
