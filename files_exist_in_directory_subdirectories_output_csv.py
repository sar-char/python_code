# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:07:36 2020

@author: sarah
"""
#Compare files in directory to spreadsheet

#Import Packages
import os
import pandas as pd
import csv

path=r'C:\Users\sarah\.spyder-py3'
file=r'C:\Users\sarah\.spyder-py3\list.csv'
new=r'C:\Users\sarah\.spyder-py3\output90.csv'

#Read in CSV File
list=pd.read_csv(file, header=None,skiprows=[0], dtype=str, names=['File'],usecols=[0], squeeze=True)
print(list)

# Create a workbook and add a worksheet.
f=open(new, 'w', newline='')
writer = csv.writer(f)
        
#Check if each file exists or not
for root, dirs, files in os.walk(path):
    for files in list:
        dir=os.path.join(root, files)
        if os.path.exists(dir):
            print(dir,'- exists')
            exists=dir+' -exists'
            writer.writerow([exists])
        else:
            print(dir,'- not exists')
            notexists=dir+'not exists'
            writer.writerow([notexists])
       
#Ouput results to csv
#file.close()