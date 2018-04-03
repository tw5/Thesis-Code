# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:39:12 2016

Creates and trains a machine learning model to classify users with an influence type.
"""

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
import numpy as np
from sklearn import cross_validation
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2, f_classif
import pickle
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from pymongo import MongoClient
from sklearn.linear_model import LogisticRegression


#with open('influenceSample.pkl', 'rb') as file:
#    unflatList=pickle.load(file)
#    X= [item for sublist in unflatList for item in sublist]
#    countList=pickle.load(file)
#    Y=pickle.load(file)
client = MongoClient()
cursor = client.training_db.influence.find()
X = []
Y = []
for user in cursor:
    X.append(user)
    Y.append(user["category"])

X_train=X
Y_train=Y


class LemmaTokenizer(object):
     def __init__(self):
         self.wnl = WordNetLemmatizer()
     def __call__(self, doc):
         return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]




class NumExtractor(TransformerMixin):
    def __init__(self,model):
        self.model = model

    def transform(self, X, y=None):
        numList=[]
        for user in X:
            numList.append([user['verified'],user['followers'],user['tweets']])
        return self.model.transform(numList)


    def fit(self, X, y=None):
        numList=[]
        for user in X:
            numList.append([user['verified'],user['followers'],user['tweets']])
        self.model.fit(numList)
        return self 


class BioExtractor(TransformerMixin):
    def __init__(self,model):
        self.model = model

    def transform(self, X, y=None):
        bioList=[]
        for user in X:
            bioList.append((user['bio'] + " "+user['language']+" ").encode('utf-8'))
        return self.model.transform(bioList)

    def fit(self, X, y=None):
        bioList=[]
        for user in X:
            bioList.append((user['bio'] + " "+user['language']+" ").encode('utf-8'))
        self.model.fit(bioList)
        return self  
        
class LocExtractor(TransformerMixin):
    def __init__(self,model):
        self.model = model

    def transform(self, X, y=None):
        locList=[]
        for user in X:
            try:
                userLoc=user['location']
            except:
                userLoc=" "
            locList.append(userLoc.encode('utf-8'))
        return self.model.transform(locList)

    def fit(self, X, y=None):
        locList=[]
        for user in X:
            try:
                userLoc=user['location']
            except:
                userLoc=" "
            locList.append(userLoc.encode('utf-8'))
        self.model.fit(locList)
        return self  


union=FeatureUnion([('bios',BioExtractor(CountVectorizer(binary=True, analyzer='word',stop_words='english',tokenizer=LemmaTokenizer()))),
                    ('nums',NumExtractor(StandardScaler())),
                    ('locs',LocExtractor(CountVectorizer(binary=True, analyzer='word')))],
                    transformer_weights={'bios':1,'nums':2,'locs':1}
)

select = SelectPercentile(f_classif,percentile=50)


pipeline = Pipeline([('processing',union),('sel',select),('clf',LogisticRegression())])

pipeline.fit(X_train,Y_train)

with open("influenceTrained.pkl", "wb") as f:
    pickle.dump(pipeline, f)

#print(pipeline.score(X,Y))

#scores = cross_validation.cross_val_score(pipeline, X, Y, cv=5)
#print(scores)
#print(np.mean(scores)) 
