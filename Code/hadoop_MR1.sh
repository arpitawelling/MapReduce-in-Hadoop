#!/bin/bash

/opt/homebrew/Cellar/hadoop/3.3.4/bin/hadoop jar /Users/arpitawelling/ECC_A1/hadoop-*streaming*.jar -file /Users/arpitawelling/ECC_A1_code/mapper_time.py    -mapper /Users/arpitawelling/ECC_A1_code/mapper_time.py -file /Users/arpitawelling/ECC_A1_code/reducer_ip.py  -reducer /Users/arpitawelling/ECC_A1_code/reducer_ip.py -input /user/access.log -output /user/ECC_A1-output_access_partial

/opt/homebrew/Cellar/hadoop/3.3.4/bin/hadoop jar /Users/arpitawelling/ECC_A1/hadoop-*streaming*.jar -file /Users/arpitawelling/ECC_A1_code/mapper2.py    -mapper /Users/arpitawelling/ECC_A1_code/mapper2.py -file /Users/arpitawelling/ECC_A1_code/reducer2.py  -reducer /Users/arpitawelling/ECC_A1_code/reducer2.py -input /user/ECC_A1-output_access_partial/part-00000 -output /user/ECC_A1-output_access_full
