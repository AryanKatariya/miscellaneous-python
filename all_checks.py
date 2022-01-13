#!/usr/bin/env python3
import shutil
import sys

def check_reboot():
    """Returns true if a computer has a pending reboot."""
    return os.path.exists("/run/reboot/-required")
def check_disk_full(disk,min_gb,min_absolute):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return true
    return False

def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    if check_disk_full(disk="/",2,10):
        print("Disk full.")
        sys.exit(1)

    print("Everthing Ok.")
    sys.exit(0)

main()
