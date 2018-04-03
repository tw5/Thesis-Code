import pickle
import tweepy
from twitUser import twitUser
import pymongo
from pymongo import MongoClient
from treePipelinesDem import LemmaTokenizer, NumExtractor, BioExtractor, LocExtractor
import statistics

CONSUMER_KEY = 'eHbNJTM3quCWQgVCrIKy981qg'
CONSUMER_SECRET = 'uC6fEGPEhhoZ8FK8WtMMfvPZIX3jh4X2LJ5myhsCtSjtjOA9jX'
OAUTH_TOKEN = '2602319010-E5wYia6QonXEP2SS2mACDvf9tfwvPXjNYnYuP8f'
OAUTH_TOKEN_SECRET = 'bNAvfqKn0uhJNzPxAMhG9OHYrdYsT5vH47Q7bsO2DCZLt'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)


varianceThreshold = .012

with open('dictInterestPipelineTrained.pkl', 'rb') as file:
    clf = pickle.load(file)

categories = {1 : "Tech",
              2: "Gaming",
           3 : "Fashion/Beauty",
           4 : "Arts/Culture",
           5 : "Music",
           6 : "Sports/Fitness",
           7 : "Food",
           8 : "Politics",
           9 : "Biz",
           10: "Unknown",
}
 

def classify(client, user):
    
    db_users = client.users_db
    
    category = clf.predict([user])
    cat = clf.predict_proba([user])
    
    interest = categories[int(category)]

    if (statistics.variance(cat[0])<varianceThreshold):
        interest = "Unknown"
        
                    
    db_users.users.update(
    {"_id" : user["_id"]},
    {'$set':
        {
        "tech" : cat[0][0],
        "gaming": cat[0][1],
        "fashion" : cat[0][2],
        "art" : cat[0][3],
        "music": cat[0][4],
        "sports" : cat[0][5],
        "pol" : cat[0][7],
        "food" : cat[0][6],
        "biz" : cat[0][8],
        "unknown": cat[0][9],
        "highestInterest" : interest
    }})
    return cat
    
    

