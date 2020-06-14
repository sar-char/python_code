#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Sarah Chapman'
__credits__ = ['Sarah Chapman']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Sarah Chapman'
__status__ = 'Production'
__description__= 'Create directory with subfolders and checks'
"""

#Import packages
import os
import shutil

#Define folder structure variables
path=r'c:/Users/sarah/.spyder-py3'#r raw string to avoid escape sequences where '\'='\\'
parent='TTT'
sub1='GSSDATAK_'
sub2=['SQL','XML','Templates']

#Create directory if exists or report it already exists
for folder in sub2:
    dir=os.path.join(path, parent, sub1, folder)
    if not os.path.isdir(dir): #can also use os.path.exists
        os.makedirs(dir)
        print(dir,'created')
    else: 
        print(dir,'already exists')

#Remove directory
#os.removedirs('c:/Users/sarah/.spyder-py3/Sunnica/GSSDATAK_')

#Copy Checking Schedule, Bulk Postage ---BUG TO RESOLVE
#src='c:/Users/sarah/.spyder-py3/master'
#dst=(os.path.join(path, parent, sub1)
#shutil.copy(src, dst, *, follow_symlinks=True)




    
    
