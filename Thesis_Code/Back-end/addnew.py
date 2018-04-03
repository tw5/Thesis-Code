# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:17:24 2016


"""
from pymongo import MongoClient
import time

def report(username, interest, influence):
    
    client = MongoClient()
    user = client.db_users.users.find({'screen_name' : username})
    client.training_db.interest.save({
                        "_id" : user['_id'],
                        "name": user['name'],
                        "screen_name" : user['screen_name'],
                        "verified" : user['verified'],
                        "followers" : user['followers'], 
                        "tweets" : user['tweets'], 
                        "location" : user['location'], 
                        "language" : user['language'], 
                        "time_zone" : user['time_zone'], 
                        "bio" : user['bio'],
                        "brands" : user['brands'],
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "category":  interest
                    })
    client.training_db.influence.save({
                        "_id" : user['_id'],
                        "name": user['name'],
                        "screen_name" : user['screen_name'],
                        "verified" : user['verified'],
                        "followers" : user['followers'], 
                        "tweets" : user['tweets'], 
                        "location" : user['location'], 
                        "language" : user['language'], 
                        "time_zone" : user['time_zone'], 
                        "bio" : user['bio'],
                        "brands" : user['brands'],
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "category":  influence
                    })
        
                    