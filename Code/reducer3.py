#!/usr/bin/python3
"""reducer.py"""

import sys
from operator import itemgetter

dict_ip_count={}
for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    ip2, num = line.split('\t')
    try:
        if ip2 in dict_ip_count.keys():
            dict_ip_count[ip2] += num
        else:
            dict_ip_count[ip2]= num
            
    except ValueError:
        pass

sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)
stop=0
for ip,count in sorted_dict_ip_count:
    if stop==3:
        break
    print("%s\t%s"%(ip,count))
    stop+=1