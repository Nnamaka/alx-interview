#!/usr/bin/python3
"""Rreads stdin line by line and computes metrics"""
import sys

total_size = 0
count = 0
staticmethod = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def print_stat():
    print('File size: {}'.format(total_size))
    for key, value in sorted(staticmethod.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])

            if code in staticmethod.keys():
                staticmethod[code] += 1

            total_size += size
            count += 1

        if count == 10:
            count = 0
            print_stat()

except Exception as err:
    pass

finally:
    print_stat()
