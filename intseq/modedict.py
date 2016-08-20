# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:52 2016

@author: Kazuma Wittick
"""

maxMode = 0
array = [12, 3, 4, 5, 6, 7, 8, 9, 1, 4,4, 6, 2,1, 5, 76, 6, 6, 6 ]
for i in array:
    getMode = array.count(i)
    if getMode > maxMode:
        maxMode = getMode
        modeNumber = i


print modeNumber
    
    



