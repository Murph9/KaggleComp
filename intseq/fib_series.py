# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
from scipy import stats as st

def fib_series(array):
    if len(array)<=2:
        return 0
    i = 2
    while i < len(array):
        if (array[i] != array[i-1]+array[i-2]):
            return 0
        i += 1
    
    return array[i-1]+array[i-2]

def first_digit(array):
    for i in range(len(array)):
        if (array[i] < 0):
            return 0
        s = str(i)[0]
        if int(s) != array[i]:
            return 0

    return int(str(len(array))[0])

def get_mode(array):
    maxMode = 0
    for i in array:
        getMode = array.count(i)
        if getMode > maxMode:
            maxMode = getMode
            modeNumber = i
    return modeNumber

    

#Fucntion array, put a function in here to run it..
test_funcs = [fib_series, first_digit, get_mode, lambda x: 0]

# ..here
def get_next(array):
    result = 0
    for funct in test_funcs:
        result = funct(array)
        if result != 0:
            return result
    return result


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
    next_num = get_next(array)
    result.append([rowId, next_num])
    
with open('zeros.csv', 'w') as f:
    f.write("Id,Last\n")
    for row in result:
        f.write(str(row[0])+","+str(row[1])+'\n')

    
