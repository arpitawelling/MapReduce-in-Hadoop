#!/usr/bin/python3
"""reducer.py"""

import sys
from operator import itemgetter

dict_word_count = {}

for line in sys.stdin:
    #print(line)
    line = line.strip()
    if len(line)==0:
        continue
    word, count = line.split('\t')
    if word not in dict_word_count.keys():
        dict_word_count[word]=count
    else:
        dict_word_count[word]+=count
for word, count in dict_word_count.items():
    print('%s\t%s' % (word, count))