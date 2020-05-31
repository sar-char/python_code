# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:56:57 2020

@author: sarah
"""


#Import Packages
import os
import pandas as pd

#Create Report of OS files
dir=r'C:\Users\sarah\.spyder-py3'
list=os.listdir(dir)
list=pd.DataFrame(list)
list.to_csv(r'C:\Users\sarah\.spyder-py3\list.csv', index=False)

#Delete files
#s.remove(dir+r'\list.csv')