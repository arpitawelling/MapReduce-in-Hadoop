#!/usr/bin/python3
"""mapper.py"""

import re 
import sys

#pat = re.compile('(?P<ip>\d+. \d+. \d+. \d+).*?"\w+ (?P<subdir>.*?)')
pat =re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
#print(sys.argv[0]
# #\print(sys.argv[1])
for line in sys.stdin:

    #match = line.split(" ")
    match = pat.search(line)
    #ip=match[0]
    #hour=match[3].split(":")[1]
    if match:
        #print('%s\t%s' % (ip, 1))
        print('%s\t%s' % ('['+match.group('hour')+":00"+']'+match.group('ip'), 1))