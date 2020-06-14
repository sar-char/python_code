# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:13:12 2020

@author: sarah

@Description: Flytipping Dataset
"""
#Import Packages
import pandas as pd
import chardet
import numpy as np
import matplotlib.pyplot as plt

#Diplay causes the issues
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',50)
#pd.set_option('display.max_colwidth',10)
#pd.set_option('display.width',None)
#pd.set_option('display.expand_frame_repr', True)

#Import the csv
path=r'C:\Users\sarah\OneDrive\Documents\SQL\Flytipping_2012_2019.csv'
data = pd.read_csv(path, header=0, skiprows=[0,1], sep=',')# index_col=0)
print(data.head())

#Encoding issue - pd.read_csv assumes UTF-8
#Error 'utf-8' codec can't decode byte 0xa3 in position 34: invalid start byte
#UTF-8 is not the encoding on CSV to check your file encoding:

#with open(path, 'rb') as rawdata:
#    result = chardet.detect(rawdata.read(10000))
#print(result)

#Data Quality Check 
##1. Remove 3 unwanted columns

##Drop columns by column position
data.drop(data.columns[44:48], axis=1, inplace=True)
print(data)

##Drop columns based on string match in drop function
data.drop(data.columns[data.columns.str.contains('named')], axis=1, inplace=True)
print(data)

##Check and drop columns based on string match in sep variable
drop_c=data.columns[data.columns.str.contains('ONS')]
data.drop(drop_c, axis=1, inplace=True)
print(data)

##2. Convert to data types other than object by default in .csv, .xlsx imports

##Quick overview of the data
for col in data:
    print(data[col].unique())

##3. Check for null data
nullstotal=data.isnull().sum()
print(nullstotal)

##Fill blanks with NaN
data=data.fillna('NaN')
print(data.head(20))

#Replace 0, :, ., nan, ' ' with NaN
data=data.replace(['0',':','.','nan'], 'NaN')

##4. Remove whitespace

##Replace ' ' with '_' in columns
data.columns=data.columns.str.replace(' ', '_')
print(data.columns)

##Remove leading whitespace - Strip() not work but lstrip and rstrip work 
data['LA_Name']=data['LA_Name'].str.strip()
data['Region']=data['Region'].str.strip()
print(data[['LA_Name','Region']])

#Find a solution to apply to all columns!!!!

##5. Captialising String Fields

##LA Name - if values does not contain and or - then captialise
data['LA_Name'].str.title().unique()
#or print(data['LA_Name'].str.title().unique())

##Region
print (data['Region']) #no issues with capitals

##Replace *Total/*Total England with Total/Total England
data = data.replace('*Total England', 'Total England')
data = data.replace('*Total', 'Total')
print(data[['Region','LA_Name']])

##8. Separate out totals and yearly data for each region

##Create subset total data
total=data[data['LA_Name'].str.contains ('Total')]
print(total.head())
total.to_csv (r'C:\Users\sarah\OneDrive\Documents\SQL\Flytipping_Total.csv', index = False, header=True)

##Create subset yearly data
yearly=data[data['LA_Name'] != '*Total']
print(yearly.head())
yearly.to_csv (r'C:\Users\sarah\OneDrive\Documents\SQL\Flytipping_Yearly.csv', index = False, header=True)

##7. Create a plot

##Total England
totalEngland=total[total['Region'].str.contains ('Total England')]
totalEngland=totalEngland[['Year','LA_Name','Region','Total_Incidents']]
print(totalEngland)
totalEngland.info()

#plt.plot
x=totalEngland['Year']
y=totalEngland['Total_Incidents']
plt.plot(x, y,'-ok')
plt.xlabel('Year')
plt.ylabel('Total Incidents')
plt.show()

##Total Per Region
TotalPerRegion=data[(data['Region'] != 'Total England') & (data['LA_Name']=='Total')]
TotalPerRegion=TotalPerRegion[['Year','Region','Total_Incidents']]

#Convert data type to numeric -otherwise error TypeError: no numeric data to plot
#See Stackoverflow https://stackoverflow.com/questions/61542097/plotting-pandas-dataframe-using-groupby-typeerror-no-numeric-data-to-plot
TotalPerRegion['Total_Incidents']=TotalPerRegion['Total_Incidents'].astype(int)
print(TotalPerRegion.dtypes)

#Option1: Reformat the dataframe index=year, columns=regions, data=total incidents
#Breaks down steps to view the data
#TotalPerRegion=TotalPerRegion.groupby(['Year','Region'])['Total_Incidents'].sum()
#TotalPerRegion=TotalPerRegion.unstack(level='Region')
#print(TotalPerRegion.head())

#Group By and Plot
#TotalPerRegion=TotalPerRegion.groupby(['Year','Region'])['Total_Incidents'].sum().unstack()

#Define the columns field, other error KeyError: 'Region'
#TotalPerRegion.columns.name = 'Region'

#Plot
#Specific order to the code:
#1. Create your blank figure and axis
#2. Add your formatting 
#3. Plot Ensure .plot(ax=ax)
#4. Legend after the plot

#Option1: Plot using groupby
fig, ax = plt.subplots()

ax.set_xlabel('Year')
ax.set_ylabel('Total Incidents (Count)')
ax.set_title('Total Flytipping Incidents in England 2012-2019')
ax.set_ylim([0,400000])

TotalPerRegion.groupby(['Year','Region'])['Total_Incidents'].sum().unstack(level='Region').plot(ax=ax)

ax.legend(bbox_to_anchor=[1.6,1,0,0], loc='upper right') ##bbox_to_anchor(x0,y0,width,height) - first 2 are positon of box, second 2 size of legend
plt.show()

#Option2: plot using pivottable
#Group=TotalPerRegion=TotalPerRegion.groupby(['Year','Region'])['Total_Incidents'].sum()
fig, ax = plt.subplots()
pd.pivot_table(TotalPerRegion, values='Total_Incidents', index='Year', columns='Region').plot()

#Export to csv
TotalPerRegion.to_csv(r'C:\Users\sarah\OneDrive\Documents\SQL\TotalPerRegion.csv')
data.to_csv(r'C:\Users\sarah\OneDrive\Documents\SQL\All_Flytipping.csv')