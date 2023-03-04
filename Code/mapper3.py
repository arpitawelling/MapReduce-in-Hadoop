#!/usr/bin/python3
"""mapper.py"""

import sys
from operator import itemgetter

dict_ip_count = {}
range_given = sys.argv[1]
range_given = range_given.split("-")
for i in range(len(range_given)):
    range_given[i]=int(range_given[i])

make_range_str=[]
for x in range(range_given[0]+1,range_given[1]+1):
    if len(str(x))<2:
        make_range_str.append("0"+str(x)+":00")
    else:
        make_range_str.append(str(x)+":00")
for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    ip2, num = line.split('\t')
    temp1= ip2.split("[")
    time, ip = temp1[1].split("]")
    try:
        if time in make_range_str:
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