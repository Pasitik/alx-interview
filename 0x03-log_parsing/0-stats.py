#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys
import re

pattern = (
    r'^('
    r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.'
    r'){3}'
    r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    r' - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1"'
    r' (\d{3}) (\d+)$'
)

count = 0
_sum = 0
status_dic = {}

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            line_parts = line.split(" ")
            status = line_parts[7]
            if status not in status_dic:
                status_dic[status] = 1
            else:
                status_dic[status] += 1
            count += 1
            _sum += int(line_parts[8])
            if count == 10:
                count = 0
                print("File size: {}".format(_sum))
                for key, value in sorted(status_dic.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(_sum))
    for key, value in sorted(status_dic.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
