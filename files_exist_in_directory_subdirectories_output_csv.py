#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Sarah Chapman'
__credits__ = ['Sarah Chapman']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Sarah Chapman'
__status__ = 'Production'
__description__='Check if a list of filenames exist in a directory'
"""

#Compare files in directory to spreadsheet

#Import Packages
import os
import pandas as pd
import csv

path=r'C:\Users\sarah\.spyder-py3'
file=r'C:\Users\sarah\.spyder-py3\list.csv'
new=r'C:\Users\sarah\.spyder-py3\output16.csv'

#Read in CSV File
list=pd.read_csv(file, header=None,skiprows=[0], dtype=str, names=['File'],usecols=[0], squeeze=True)
print(list)

# Create csv file
f=open(new, 'w', newline='')
writer = csv.writer(f)

# helo
#for root, dirs, files in os.walk(path):
 #   for file in files:
  #      if file==filename:
   #         print('File exists')
##

#
for root, dirs, files in os.walk(path):
found = list.intersection(files)
    for list in found:
      f.write(os.path.join(root, name) + '\n')





#Check if each file exists or not
for root, dirs, files in os.walk(path):
    for list in files:
        dir=list
        if os.path.isfile(dir):
            print(list,'exists')
            
            exists=dir+' exists'
            writer.writerow([exists])
        else:
            notexists=dir+' not exists'
            writer.writerow([notexists])
       
    
#Check if each file exists or not
for root, dirs, files in os.walk(path):
    for filename in files:
        dir=os.path.join(root, filename)
        if os.path.exists(dir):
            exists=dir+' exists'
            writer.writerow([exists])
        else:
            notexists=dir+' not exists'
            writer.writerow([notexists])
       
#Ouput results to csv
f.close()
