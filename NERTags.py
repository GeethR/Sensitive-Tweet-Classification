# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:34:44 2020

@author: GEETHA RAJU
"""

import pandas as pd
import csv

#keywords_list = ['blood', 'baby', 'birth', 'breast', 'medical', 'diagnosis', 'accident', 'vaccine', 'therapy', 'death',
#                 'mental', 'hospital', 'treatment', 'pain', 'life', 'cancer', 'injury', 'weight', 'influenza', 'natural', 'alcohol', 'report']

#keywords_list = ['call record', 'car', 'chat', 'children', 'family', 'fingerprint', 'hobby', 'home', 'house', 'identification', 'location', 'marriage', 'mobile phone', 'my photo', 'nation', 'party', 'phone book', 'phone number', 'religion','shopping', 'spouse', 'travel']
keywords_list = ['affiliation', 'bank account', 'booking hotel', 'company address', 'credit card', 'credit score', 'criminal record', 'driver license', 'email address', 'insurance', 'investment', 'IP', 'job', 'msn', 'online record', 'passport', 'password', 'position', 'property','salary', 'stock', 'address book']
#keywords_list = ['accident', 'age', 'allergy', 'ambulance', 'blood type', 'death', 'diagnosis', 'disease', 'drug use', 'height', 'hospital', 'immunity', 'infection', 'medical', 'mental', 'nursing', 'surgery', 'therapy', 'treatment','vaccine', 'weight', 'viral']

named_entities_list = ['ORG', 'GPE', 'PERSON', 'DATE', 'TIME', 'NORP', 'LOC', 'PRODUCT', 'EVENTS', 'PERCENT']

# Create the barebones simple pandas dataframe
table = pd.DataFrame(data=[[0]*len(named_entities_list)]*len(keywords_list),
                     index=keywords_list, columns=named_entities_list)

# Read the xlsx file
file_table = pd.read_excel('D:/Geetha/Python_WS/Spyder_WS/Thesis_Evaluation/professional_nerinfo.xlsx')
# print(file_table['text']) # Contains the tweets column
# print(file_table['named_ents']) # Contains the named entities column
for row in file_table.itertuples():
    # 0 - index, 1 - text, 19 - entites
    for i in keywords_list:
        if i in row[1]:
            # Row 19 is a string of list of tuples
            for j in named_entities_list:
                if j in row[2]:
                    table[j][i] += 1

table.to_csv('D:/Geetha/Python_WS/Spyder_WS/Thesis_Evaluation/professionalthesisBook1.csv')
# Table updates successfully
print("Single Entity Table")
print(table)

# Need to do two combination entities
for i in range(len(named_entities_list)):
    for j in range(i + 1, len(named_entities_list)):
        new_key = str(named_entities_list[i]+' '+named_entities_list[j])
        table[new_key] = table[named_entities_list[i]] * \
            table[named_entities_list[j]]

print("Final Combination Entity Table")
print(table)

table.to_csv('D:/Geetha/Python_WS/Spyder_WS/Thesis_Evaluation/professionalthesisBook2.csv')
