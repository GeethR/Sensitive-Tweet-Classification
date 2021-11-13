# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:28:18 2020

@author: GEETHA RAJU
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
from pprint import pprint

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

from bs4 import BeautifulSoup
import requests
import re

import collections

import pandas as pd
import numpy as np

tweets1 = pd.read_csv(r"D:\Geetha\Analysis\TSP\AMT_Submission\NewDatasetforAMT\ReceivedTest\Analysis_Dataset\Personal_NER\Sensitive_Personal\family-sens.csv",encoding='latin-1')

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

tweets1['Input.text']
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

for i in range(len(tweets1)) : 
    sent = preprocess(tweets1.loc[i,'Input.text'])
    sent
    tweets1['NER'] = sent
#    tweets1.insert(i, 'NER', sent, True)


    

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

ne_tree = ne_chunk(pos_tag(word_tokenize(tweets1.loc[i,'Input.text'])))
print(ne_tree)



#Entitiy Extraction

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])

def combine_ners(temp):
    d = {}
    for k in temp.keys():
        d[k] = tuple(d[k] for d in temp)
        print(d)
    return d

for sub in test_list: 
    for key, val in sub.items():  
        res.setdefault(key, []).append(val)

def merge_by_key(ts):

    d = {}
    for t in ts:
        key = t[0]
        values = t[1]
        if key not in d:
            d[key] = values[:]
        else:
            d[key].extend(values)

    return d.items()


ner_list = []
for i in range(len(tweets1)) : 
    ner_tags = nlp(tweets1.loc[i,'Input.text'])
    temp = [(X.text, X.label_) for X in ner_tags.ents]
    result = merge_by_key(temp)
    ner_list.append(str(result))
#    list_2 = []
#    i = {}
#    for k, s in temp:
#        if k not in i:
#            list_2.append((k, s))
#            i[k] = len(i)
#        else:
#            list_2[i[k]][1].extend(s)
#            
#    for sub in temp: 
#        for key, val in sub.__iter__:  
#            res.setdefault(key, []).append(val)
#            print(res)
    #temp = str([(X.text, X.label_) for X in ner_tags.ents])  
   
    
tweets1['NER_Info'] = ner_list
    
tweets1.to_csv('family_nerinfo.csv')
    
pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
len(article.ents)

labels = [x.label_ for x in article.ents]
Counter(labels)

items = [x.text for x in article.ents]
Counter(items).most_common(3)

sentences = [x for x in article.sents]
print(sentences[20])

displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')
displacy.render(nlp(str(sentences[20])), style='dep', jupyter = True, options = {'distance': 120})

[(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(str(sentences[20])) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]

dict([(str(x), x.label_) for x in nlp(str(sentences[20])).ents])

print([(x, x.ent_iob_, x.ent_type_) for x in sentences[20]])
