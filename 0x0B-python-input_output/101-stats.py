#!/usr/bin/python3
"""LogParsing module"""

import sys
from collections import defaultdict

def compute_metrics():
    """
    Reads stdin line by line and computes metrics.
    Input format: - "GET /projects/260 HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
        Total file size: File size: <total size> where <total size> is the sum of all previous (see input format above)
        Number of lines by status code: possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        If a status code doesn’t appear, don’t print anything for this status code
        Format: <status code>: <number>
        Status codes should be printed in ascending order.
    """
    total_size = 0
    status_code_counts = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin):
            ip, _, _, _, _, _, _, _, status_code, file_size = line.split()
            total_size += int(file_size)
            status_code_counts[status_code] += 1

            if (i+1) % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print()
    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for code in sorted(status_code_counts.keys()):
            print(f"{code}: {status_code_counts[code]}")
