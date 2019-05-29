# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:26:46 2016

@author: Kazuma Wittick
"""


import re
with open('test.csv') as f:
    content = f.readlines()

content.pop(0)

result = []
for line in content:
    m = re.search('(\d+),"(.*)"', line)
    rowId = int(m.group(1))
    string = m.group(2)
    string = string.replace('"', '')
    array = map(int, string.split(','))
    result.append([rowId, 0])

with open('zeros.csv', 'w') as f:
    f.write("Id,Last\n")
    for row in result:
        f.write(str(row[0])+","+str(row[1])+'\n')
