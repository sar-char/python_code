# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:07:36 2020

@author: sarah
"""
#Compare files in directory to spreadsheet

#Import Packages
import os
import pandas as pd

path=r'C:\Users\sarah\.spyder-py3'
file=r'C:\Users\sarah\.spyder-py3\list.csv'

#Read in CSV File
list=pd.read_csv(file, header=None,skiprows=[0], dtype=str, names=['File'],usecols=[0], squeeze=True)
print(list)

#Check if each file exists or not
for files in list:
   dir=os.path.join(path,files)
   if os.path.exists(dir):
       print(dir,'exists')
   else:
       print(dir,'not exists')
