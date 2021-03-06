# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:30:22 2016
@author: Jarrod, Jake and Kaz
"""
import os

import pandas as pd
import numpy as np
import pylab as P


def cleanUpTheData(filenamewithext):
    #split so we can save it later (train.csv -> 'train', '.csv')
    filename, file_extension = os.path.splitext(filenamewithext)

    # For pd.read_csv, always use header=0 when you know row 0 is the header row
    df = pd.read_csv(filename+file_extension, header=0)

    # The types of the columns of the csv file
    df.dtypes
    
    # The columns 'Sex' 'Pclass", 'Age' of the rows with the 'Age' column being null
    df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

    # A histagram of the ages without the nulls
    #df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)

    # create a new column with the map ('female'->0 and 'male'->1)
    df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

    #######
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


    #######
    # Convert the Embarked values into something we can machine learn with as suggested by the tree tutorial
    # Not sure if the dropping of the 3 rows without gender is such a good idea
    df['EmbarkedNum'] = df['Embarked'].fillna('C').map( { 'C':0, 'S':1, 'Q':2, }, True).astype(int)

    #######
    # Int column for determining if the agefill is an estimate
    df['AgeIsNull'] = pd.isnull(df.Age).astype(int)
    # Show some columns
    df[['Gender','Pclass','Age','AgeFill', 'AgeIsNull', 'PassengerId']].head(10)

    # Fare is empty in the test data:
    df.loc[ (df['Fare'].isnull()) ] = 0 #cop out because it should be average

    # Column for family size, fsf = familysizeFactor
    df['FamilySize'] = df['SibSp'] + df['Parch']
    #df['fsf'] = 1/(df['FamilySize']+1)

    # Column for age class
    df['Age*Class'] = df.AgeFill * df.Pclass


    df['Gender*Age*Class'] = 0.0
    for row in range(len(df.AgeFill)):
        index = int(df['AgeFill'][row]/(buckets))
        df.set_value(row, 'Gender*Age*Class', df['Pclass'][row] * ages_percentage[index] * int(not bool(df['Gender'][row])) )


    # Get all the columns with type 'object'
    df.dtypes[df.dtypes.map(lambda x: x=='object')]

    # Drop all the non number columns for ease of use later
    df = df.drop(['Name', 'Cabin','Sex', 'Ticket', 'Embarked', 'Age', 'PassengerId', 'AgeIsNull', 'SibSp', 'Parch' ], axis=1)
    # Also remove the rows containing nulls
    df = df.dropna()

    #save to file for machine learning (with out the array index at the start)
    df.to_csv(filename+'_noNa'+file_extension, index=False)

    #print df[df['Gender']<1][['Survived', 'Gender', 'FamilySize']]
    #print df[['Survived', 'Gender', 'FamilySize', 'Gender*Age*Class']]
    #print df[(df['AgeFill']<65) & (df['AgeFill']>50)][['Survived']].mean()
    #print df

df = pd.read_csv('train_noNa.csv', header=0)
# Get age bucket percentage survival
buckets = 10
ages_survived = np.zeros((buckets))
ages_total = np.zeros((buckets))

for row in range(len(df.AgeFill)):
    i = int(df['AgeFill'][row]/(buckets))
    ages_survived[i] += df['Survived'][row]
    ages_total[i] += 1

ages_percentage = ages_survived/ages_total





cleanUpTheData('train.csv') # the data to train off
cleanUpTheData('test.csv') # the data we get assessed on
