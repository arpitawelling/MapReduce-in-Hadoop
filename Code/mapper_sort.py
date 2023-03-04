#!/usr/bin/python3
"""mapper.py"""

import re 
import sys

#pat = re.compile('(?P<ip>\d+. \d+. \d+. \d+).*?"\w+ (?P<subdir>.*?)')
pat = re.compile("(?P<ip>\d+\d+.\d+.\d+).+?\w+ (?P<subdir>.*?) ")
#pat = re.compile("(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
for line in sys.stdin:

    #match = line.split(" ")
    match = pat.search(line)
    #ip=match[0]
    #hour=match[3].split(":")[1]
    if match:
        #print('%s\t%s' % (ip, 1))
        print('%s\t%s' % (match.group('ip'), 1))