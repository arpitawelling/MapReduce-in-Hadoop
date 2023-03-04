#!/usr/bin/python3
"""mapper.py"""

import sys
from operator import itemgetter
dict_word_count = {}

for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    words = line.split(" ")
    for word in words:
        #print(word)
        if len(word)==0:
            continue
        if word not in dict_word_count.keys():
            dict_word_count[word]=1
        else:
            dict_word_count[word]+=1

for word, count in dict_word_count.items():
    print('%s\t%s' % (word, count))