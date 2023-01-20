#!/usr/bin/python3
"""
Task 0. Log Parsing
"""


import sys
from collections import defaultdict

total_size = 0
status_count = defaultdict(int)

line_count = 0

for line in sys.stdin:
    line_count += 1
    parts = line.split(" ")
    if len(parts) != 9:
        continue
    _, _, _, _, _, _, _, status_code, file_size = parts
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue
    if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
        continue
    total_size += file_size
    status_count[status_code] += 1

    try:
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_count.keys()):
                print(f"{status_code}: {status_count[status_code]}")
    except KeyboardInterrupt:
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_count.keys()):
                print(f"{status_code}: {status_count[status_code]}")
