# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

def fib_series(array):
    if len(array)<=2:
        return 0
    i = 2
    while i < len(array):
        if (array[i] != array[i-1]+array[i-2]):
            return 0
        i += 1
    
    return array[i-1]+array[i-2]



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
    next_num = fib_series(array)
    if (next_num != 0):
        print rowId, next_num 
    result.append([rowId, next_num])
    
with open('zeros.csv', 'w') as f:
    f.write("Id,Last\n")
    for row in result:
        f.write(str(row[0])+","+str(row[1])+'\n')

    
