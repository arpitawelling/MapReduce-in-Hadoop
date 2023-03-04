#!/usr/bin/python3
"""mapper.py"""

import sys
from operator import itemgetter
dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    ip, num = line.split('\t')
    temp1= ip.split("[")
    time, ip = temp1[1].split("]")
    try:
        num = int(num)
        if time in dict_ip_count.keys():
            # if ip in dict_ip_count[time].keys():
            #     dict_ip_count[time][ip]+= 1
            # else:
            #     dict_ip_count[time][ip]= 1
            dict_ip_count[time][ip]= num
        else:
            dict_ip_count[time]={}
            dict_ip_count[time][ip]= num
            
    except ValueError:
        pass

#sorted_dict_ip_count = sorted(dict_ip_count.items (), key=itemgetter(0))
#print(dict_ip_count)
for hour, count in dict_ip_count.items():
    sorted_count = sorted(count.items (), key=itemgetter(1),reverse=True)
    stop=0
    for key,val in sorted_count:
        if stop==3:
            break
        print("%s\t%s" % ('['+hour+']'+key, val))
        stop+=1
