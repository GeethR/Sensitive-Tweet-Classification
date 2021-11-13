# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:49:39 2020

@author: GEETHA RAJU
"""

import pandas as pd
import numpy as np

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

tweets1 = pd.read_csv(r"D:\Geetha\Analysis\TSP\AMT_Submission\NewDatasetforAMT\ReceivedTest\Analysis_Dataset\PersonalTweetAnnotatedSensitive.csv",encoding='latin-1')


ner_list = []
for i in range(len(tweets1)) : 
    ner_tags = nlp(tweets1.loc[i,'Input.text'])
    temp = str([(X.text, X.label_) for X in ner_tags.ents])  
    ner_list.append(temp)
    print([(X, X.ent_iob_, X.ent_type_) for X in tweets1.loc[i,'Input.text']])   
   # print([(ent.temp, ent.start_char, ent.end_char, ent.label_) for ent in nlp(temp).ent])
    
df = pd.DataFrame(tweets1['Input.text'])
print(df)

def extract_named_entities(text):
    return [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in nlp(text).ent]

def add_name_ents(df):
    df['named_ents'] = df['text'].apply(extract_named_entities)
    
add_name_ents(df)


for i in range(len(tweets1)):
    ner_tags = nlp(tweets1.loc[i,'Input.text'])
    extract_named_entities(tweets1.loc[i,'Input.text'])
    

    
    
tweets1['NER_Info'] = ner_list
    
tweets1.to_csv('personal_nerinfo.csv')
