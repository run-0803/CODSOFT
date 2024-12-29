import os
import time
import psutil
from prettytable import PrettyTable
from prettytable import doubleborder

"""UNITS OF MEMORY"""
size=['B','KB','MB','GB','TB','PB']

"""FUNCTION TO CONVERT MEMORY SIZE INTO HUMAN READABLE FORMAT"""
def get_size(bytes):
    for x in size:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0


def get_memory_usage():
    memory = psutil.virtual_memory()
    total = get_size(memory.total)
    available = get_size(memory.available)
    used = get_size(memory.used)
    percent = memory.percent
    return total, available, used, percent

# Example of using these functions
total, available, used, percent = get_memory_usage()
print(f"Total Memory: {total}")
print(f"Available Memory: {available}")
print(f"Used Memory: {used}")
print(f"Memory Usage: {percent}%")
