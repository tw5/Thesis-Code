"""
Created on Wed Jun 29 14:39:12 2016

"""

from twitUser import twitUser
import tweepy
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
from sklearn.linear_model import LogisticRegression


with open('dictSample.pkl', 'rb') as file:
    unflatList=pickle.load(file)
    X= [item for sublist in unflatList for item in sublist]
    countList=pickle.load(file)
    Y=pickle.load(file)




class LemmaTokenizer(object):
     def __init__(self):
         self.wnl = WordNetLemmatizer()
     def __call__(self, doc):
         return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]


X_train=X
Y_train=Y

class NumExtractor(TransformerMixin):
    def __init__(self,model):
        self.model = model

    def transform(self, X, y=None):
        numList=[]
        for user in X:
            numList.append([user.user.followers_count, int(user.user.created_at.year),user.user.friends_count,
                user.user.listed_count, user.user.statuses_count, 
                int(user.user.verified), int(user.user.default_profile_image)])
        return self.model.transform(numList)


    def fit(self, X, y=None):
        numList=[]
        for user in X:
            numList.append([user.user.followers_count, int(user.user.created_at.year),user.user.friends_count,
                user.user.listed_count, user.user.statuses_count, 
                int(user.user.verified), int(user.user.default_profile_image)])
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
                    #('nums',NumExtractor(StandardScaler())),
                    ('locs',LocExtractor(CountVectorizer(binary=True, analyzer='word')))
])

select = SelectPercentile(f_classif,percentile=50)



pipeline = Pipeline([('processing',union),('sel',select),('clf',LogisticRegression())])

pipeline.fit(X_train,Y_train)

with open("dictInterestPipelineTrained.pkl", "wb") as f:
    pickle.dump(pipeline, f)

#print(pipeline.score(X,Y))

