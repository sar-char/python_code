#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Sarah Chapman'
__credits__ = ['Sarah Chapman']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Sarah Chapman'
__status__ = 'Production'
__description__= 'Create a given directory'
"""

    
#Import Packages
import os
import shutil

#Define folder structure variables
path=r'c:/Users/sarah/.spyder-py3'
parent='Sunnica'
sub1='GSSDATAK_'

#Define folder structure paths
dir = os.path.join(path, parent, sub1)
print(dir)

#Create directory if exists or report it already exists
if not os.path.exists(dir): 
    os.makedirs(dir)
    print(dir, 'created')
else: 
    print(dir, 'already exists')


    
    
