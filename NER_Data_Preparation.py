# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:35:54 2020

@author: GEETHA RAJU
"""

import pandas as pd
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")

tweets1 = pd.read_csv(r"D:\Geetha\Analysis\TSP\AMT_Submission\NewDatasetforAMT\ReceivedTest\Analysis_Dataset\HealthTweetAnnotatedSensitive.csv",encoding='latin-1')

nlist = []


#doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for i in range(len(tweets1)) : 
    doc = str(tweets1.loc[i,'Input.text'])
    doc1 = nlp(doc)
    temp = [(word, word.ent_type_) for word in doc1 if word.ent_type_]
    
for i in range(len(tweets1)) : 
    doc = str(tweets1.loc[i,'Input.text'])
    doc1 = nlp(doc)
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc1.ents]
    #print(ents)
    nlist.append(str(ents))
    

    
tweets1['NER_Info'] = nlist
    
tweets1.to_csv('health_nerinfo.csv')
    
