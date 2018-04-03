import pickle
import tweepy
from influencePipeline import LemmaTokenizer, NumExtractor, BioExtractor, LocExtractor
from pymongo import MongoClient
import statistics

debugging=False

CONSUMER_KEY = 'eHbNJTM3quCWQgVCrIKy981qg'
CONSUMER_SECRET = 'uC6fEGPEhhoZ8FK8WtMMfvPZIX3jh4X2LJ5myhsCtSjtjOA9jX'
OAUTH_TOKEN = '2602319010-E5wYia6QonXEP2SS2mACDvf9tfwvPXjNYnYuP8f'
OAUTH_TOKEN_SECRET = 'bNAvfqKn0uhJNzPxAMhG9OHYrdYsT5vH47Q7bsO2DCZLt'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)



varianceThreshold = .05

with open('influenceTrained.pkl', 'rb') as file:
    clf = pickle.load(file)
"""
categories = {1 : "Normal",
           2: "Youtube",
           3: "News & Journalism",
           4 : "Celeb",
           5 : "Biz",
           6 : "Brand/Corporate",
           7 : "Student"
}"""
 

def classify(client, username):
    db_users = client.users_db
    
    category = clf.predict([username])
    cat = clf.predict_proba([username])
    #print(cat)
    #print(categories[int(category)])

        
        
    var = statistics.variance(cat[0]) 
    influenceClassification = 'casual_user'
    if(var > .02 ): 
        influenceClassification = category.tolist()[0]
     
     
     
    if(debugging):
        print (category.tolist()[0])
        print (influenceClassification)
        print (type(category.tolist()[0]))
        print(username['screen_name'])
        print(username['bio'])
       # print(categories[int(category)])
        print(cat)
        print(statistics.variance(cat[0]))    
        print("\n")     
     
    db_users.users.update(
    {"_id" : username["_id"]},
    {'$set':
        {
        "casual_user" : cat[0][0],
        "youtuber": cat[0][1],
        "writer" : cat[0][2],
        "celebrity" : cat[0][3],
        "business_expert": cat[0][4],
        "brand_corp" : cat[0][5],
        "academic" : cat[0][6],
        "highestInfluence" : influenceClassification
    }})
    return cat

