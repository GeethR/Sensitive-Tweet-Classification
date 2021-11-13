# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:41:19 2020

@author: GEETHA RAJU
"""

import pandas as pd
import csv
import numpy as np
from numpy import genfromtxt

file = "D:/Geetha/Python_WS/Spyder_WS/Thesis_Evaluation/Clear_HeatMap_Health.csv"

EntityList = ["ORG", "GPE", "PERSON",	"DATE","TIME", "NORP",	"LOCATION", "PRODUCT", "EVENTS", "PERCENT", "ORG-GPE"
              "ORG-PERSON",	"ORG-DATE",	"ORG-TIME", "ORG-NORP", "ORG-LOCATION",	"ORG-PRODUCT",	"ORG-EVENTS",	"ORG-PERCENT",	"GPE-PERSON"	"GPE-DATE",
              "GPE-TIME",	"GPE-NORP",	"GPE-LOCATION",	"GPE-PRODUCT",	"GPE-EVENTS",	"GPE-PERCENT",	"PERSON-DATE",	"PERSON-TIME",	"PERSON-NOPR",
              "PERSON-LOCATION",	"PERSON-PRODUCT",	"PERSON-EVENTS",	"PERSON-PERCENT","DATE-TIME	","DATE-NORP",	"DATE-LOCATION","DATE-PRODUCT",	"DATE-EVENTS",
              "DATE-PERCENT",	"TIME-NOPR",	"TIME-LOCATION",	"TIME-PRODUCT",	"TIME-EVENTS",	"TIME-PERCENT",	"NORP-LOCATION",	"NORP-PRODUCT",	"NORP-EVENTS",	"NORP-PERCENT",
              "LOCATION-PRODUCT",	"LOCATION-EVENT", "LOCATION-PERCENT",	"PRODUCT-EVENTS",	 "PRODUCT-PERCENT",	"EVENTS-PERCENT"]

data = pd.read_csv(file) 
data = data.fillna(0)


my_data = genfromtxt(file, delimiter=',')

my_data_clean = np.nan_to_num(my_data) 
result = np.where(my_data_clean !=0)
#result = np.where(my_data_clean<0 )
print('Tuple of arrays returned : ', result)   
listOfCoordinates= list(zip(result[0], result[1])) 


def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
            
    return unique_list

index_1 = unique(result[0])
index_2 = unique(result[1])

data.head()

#def getEntities(data, index_1, index_2):
#    print("index1:")
#    for i in index_1:
##        print(i)
#        print(data['Entity'].iloc[i])
#    print("index2:")
#    for i in index_2:
##        print(i)
#        print(data['Entity'].iloc[i])
#
#
#getEntities(data, index_1, index_2)
        



def getEntitieCorNames(data, listOfCoordinates):
    one_one_list = []
    one_two_list = []
    two_two_list = []
    one_one_Entitylist = []
    one_two_Entitylist = []
    two_two_Entitylist = []
    entity = ""
    for p in listOfCoordinates:
        
        if(p[0]<=10 and p[1]<=10):
            print('{} : {}'.format(p[0], p[1]))
#            val = data.get_value(p[0]-1, p[1]-1, takeable = True)
            val = data[p[0]][p[1]]
            one_one_list.append(val) 
            entity = EntityList[p[0]] + " " + EntityList[p[1]]
            one_one_Entitylist.append(entity)
        elif(p[0]<=10 and p[1]>10):
            print('{} : {}'.format(p[0], p[1]))
#            val = data.get_value(p[0]-1, p[1]-1,takeable = True)
            val = data[p[0]][p[1]]
            one_two_list.append(val)
            entity = EntityList[p[0]] + " " + EntityList[p[1]]
            one_two_Entitylist.append(entity)
        elif(p[0]>10 and p[1]>10):
            print('{} : {}'.format(p[0], p[1]))
#            val = data.get_value(p[0]-1,p[1]-1, takeable = True)
            val = data[p[0]][p[1]]
            two_two_list.append(val)
            entity = EntityList[p[0]] + " " + EntityList[p[1]]
            two_two_Entitylist.append(entity)
    return one_one_list, one_two_list, two_two_list, one_one_Entitylist, one_two_Entitylist, two_two_Entitylist
            


one, two, three, onelist, twolist, threelist = getEntitieCorNames(my_data_clean, listOfCoordinates)

d1 = {'Entities': onelist,'Values':one}
df1 = pd.DataFrame(d1)

d2 = {'Entities': twolist,'Values':two}
df2 = pd.DataFrame(d2)

d3 = {'Entities': threelist,'Values':three}
df3 = pd.DataFrame(d3)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('D:/Geetha/Python_WS/Spyder_WS/Thesis_Evaluation/NER/HealthPSE.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='one-one')
df2.to_excel(writer, sheet_name='one-two')
df3.to_excel(writer, sheet_name='two-two')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

