#!/usr/bin/python3
"""reducer.py"""

import sys
from operator import itemgetter
dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
    except ValueError:
        pass

sorted_dict_ip_count = sorted(dict_ip_count.items (), key=itemgetter(1))
for ip, count in sorted_dict_ip_count:
    print('%s\t%s' % (ip, count))