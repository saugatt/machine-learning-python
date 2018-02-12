#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:02:04 2018

@author: saugat
"""
import numpy as np
import matplotlib.pyplot as plt  # plot nice charts with this 
import pandas as pd 

# Importing datasets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1 ].values 
y= dataset.iloc[:,3].values

#Taking care of the missing data
from sklearn.preprocessing import Imputer