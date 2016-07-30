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

# The types of the columns of the csv file
df.dtypes

# The columns 'Sex' 'Pclass", 'Age' of the rows with the 'Age' column being null
df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

# A histagram of the ages without the nulls
#df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)

# create a new column with the map ('female'->0 and 'male'->1)
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

# 2d array 2 first then 3 
median_ages = np.zeros((2,3))

# for each gender populate the median_ages array
for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()
                              

# New column for a better age list
df['AgeFill'] = df['Age']

# Fill the empty values with the next geuss from the other data
for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = median_ages[i,j]
                
# Int column for determining if the agefill is an estimate
df['AgeIsNull'] = pd.isnull(df.Age).astype(int)
df[['Gender','Pclass','Age','AgeFill', 'AgeIsNull']].head(10)

# Column for family size
df['FamilySize'] = df['SibSp'] + df['Parch']
# Column for age class
df['Age*Class'] = df.AgeFill * df.Pclass

# Get all the columns with type 'object'
df.dtypes[df.dtypes.map(lambda x: x=='object')]

# Drop all the non number columns for ease of use later
df = df.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked', 'Age'], axis=1)
# Also remove the rows containing nulls
df = df.dropna()

train_data = df.values
print train_data
