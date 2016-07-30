# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:30:22 2016
@author: Jarrod, Jake and Kaz 
"""

import pandas as pd
import numpy as np
import pylab as P


# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('train.csv', header=0)

df.dtypes

df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

#df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)

df['Gender'] = 4

df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

median_ages = np.zeros((2,3))

for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()
                              
median_ages

df['AgeFill'] = df['Age']

for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = median_ages[i,j]
                


df['AgeIsNull'] = pd.isnull(df.Age).astype(int)

df[['Gender','Pclass','Age','AgeFill', 'AgeIsNull']].head(10)

print df.describe()