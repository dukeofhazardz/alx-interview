#!/usr/bin/python3
""" Log parsing Algorithm """

import sys
import signal
""" A script that reads stdin line by line and computes metrics """


def print_statistics(file_size, status_codes):
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        if count == 0:
            continue
        print(f"{code}: {count}")


file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def signal_handler(sig, frame):
    print_statistics(file_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        log = line.strip()
        params = log.split(" ")
        status_code_str = params[-2]
        file_size_str = params[-1]
        status_code = int(status_code_str)
        current_file_size = int(file_size_str)
    except ValueError:
        continue

    file_size += current_file_size
    if status_code in status_codes:
        status_codes[status_code] += 1

    line_count += 1
    if line_count == 10:
        print_statistics(file_size, status_codes)
        line_count = 0
