#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Sarah Chapman'
__credits__ = ['Sarah Chapman']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Sarah Chapman'
__status__ = 'Production'
"""

#Import Packages
import os
import pandas as pd
import csv

#UserInput
#inputdir1 = input('Input Directory:')
#outputdir1 = input('Output Directory:')

#Create Report of OS files
inputdir=r'C:\Development\x_reporting_solution\PinPoint.Reports\PinPoint.Reports'
outputdir=r'C:\Users\UKSMC009'
outputfile=r'\List15.csv'

#Create a blank csv file 
f=open(outputdir+outputfile, 'w', newline='')  #write to an existing blank csv file

# Headers of csv files
names = ['FileNameAndPath', 'Name']

#Write to file
w=csv.writer(f)

#Write header to the file
w.writerow(names)

#Loop through directory and write root, dir, files to csv file
for root, dirs, files in os.walk(inputdir):
    for filename in files:
         FileNameAndPath=os.path.join(root, filename)
         Name=filename
         w.writerow([FileNameAndPath, Name])
        
#Close csv
f.close()
