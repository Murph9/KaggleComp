# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:21:35 2016

@author: Jake
"""

#Finally some machine learning, yay.
import os
import pandas as pa
import csv as csv

#Oh look a library that does it for us: (luckily included in anaconda)
from sklearn.ensemble import RandomForestClassifier

ids = pa.read_csv('test.csv', header=0)
ids = ids[ids.columns[0]]

train_data = pa.read_csv('train_noNa.csv', header=0).values

#use to quit without killing spyder (imagine what happened to me)
#raise Exception('exit')

test_data_pa = pa.read_csv('test_noNa.csv', header=0)
test_data = test_data_pa.values

print 'Training...'
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit( train_data[0::,1::], train_data[0::,0] )

print 'Predicting...'
output = forest.predict(test_data).astype(int)

predictions_file = open('myfirstforest.csv', 'wb')
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done: '+ str(len(output))