# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:36:59 2016

@author: Kazuma Wittick
"""
"""
import numpy as np

train = np.loadtxt('train.csv', dtype = str)

train = train[1:2]



for row in train:
    seq = str(row)
    print seq
"""

import re
with open('train.csv') as f:
    content = f.readlines()

content.pop(0)

data = []
for line in content:
    m = re.search('"(.*)"', line)
    string = m.group(0)
    string = string.replace('"', '')
    array = map(int, string.split(','))
    data.append(array)
    
#print data[0:10]

minimum = 10000
for array in data:
    yy = len(array)
    minimum = min(yy, minimum)
    if yy == 1:
        print array
print minimum

print 348751093847501987*19087501938475