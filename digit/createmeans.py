# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:10:31 2016

@author: Kazuma Wittick
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

print 'Loading..'
data = np.loadtxt("train.csv", delimiter = ',', skiprows = 1)

numbers = data[:,0] #get the number labels
data = data[:,1:] #remove the labels

print 'Reshaping...'
data = data.reshape(42000, 28, 28) #reshape into each image
results = np.zeros(shape = (10, 28, 28), dtype = float) #make array of all the numbers

counts = [0 for i in range(10)]

print 'Averaging...'

index = 0
for i in range(len(data)):
    number = int(numbers[i])
    counts[number] += 1

    for j in range(28):
        for k in range(28):
            results[number, j, k] += data[i, j, k]

print counts

for i in range(10):
    results[i] = (results[i] / counts[i]).round()

    plt.imshow(results[i], interpolation='none', cmap='magma')
    plt.show()

    np.savetxt(str(i)+"_avg.csv", results[i], fmt="%i", delimiter=",")

print 'Done'
