# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:30:22 2016
@author: Jarrod, Jake and Kaz 
"""

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb')) 
header = csv_file_object.next() 
data=[] 

for row in csv_file_object:
    data.append(row)
data = np.array(data) 

