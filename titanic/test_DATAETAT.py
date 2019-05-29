# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 15:52:35 2016

@author: Kazuma Wittick
"""

import os

import pandas as pd
import numpy as np
import pylab as P


# For pd.read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('train.csv', header=0)
print df[['Survived','Fare']]
df['Age'].hist(bins=15)
P.show()
