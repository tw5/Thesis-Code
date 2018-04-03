from pymongo import MongoClient
import time

def total_count(brand):
    client = MongoClient()
    db = client.current_db
    cursor = db.current.find({'brand' : brand})
    result = 0
    for doc in cursor:
        result = doc['total']
    return result
def verified_count(brand):
    client = MongoClient()
    db = client.current_db
    cursor = db.current.find({'brand' : brand})
    result = 0
    for doc in cursor:
        result = doc['verified']
    return result

def tweets_count(brand):
    client = MongoClient()
    db = client.current_db
    cursor = db.current.find({'brand' : brand})
    result = 0
    for doc in cursor:
        result = doc['tweetmean']
    return result

def follower_count(brand):
    client = MongoClient()
    db = client.current_db
    cursor = db.current.find({'brand' : brand})
    result = 0
    for doc in cursor:
        result = doc['followmean']
    return result

def influence_score_count(brand):
    client = MongoClient()
    db = client.current_db
    cursor = db.current.find({'brand' : brand})
    result = 0
    for doc in cursor:
        result = doc['influencemean']
    return result





def getCategoriesPcts(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    pcts = [0,0,0,0,0,0,0,0,0,0,0]
    interests = ['"Tech"','"Sports"','"Art"','"Food"','"Politics"','"Business"','"Unknown"','"Gaming"','"Fashion"','"Music"']
    timestamp = [0]
    for doc in cursor:

        pcts[0] = (float(doc['tech']))#/ float(doc['total']))
        pcts[1] = (float(doc['sports']) )#/ float(doc['total']))
        pcts[2] = (float(doc['art']) )#/ float(doc['total']))
        pcts[3] = (float(doc['food']))# / float(doc['total']))
        pcts[4] = (float(doc['politics']))# / float(doc['total']))
        pcts[5] = (float(doc['business']))# / float(doc['total']))
        pcts[6] = (float(doc['unknown']))# / float(doc['total']))
        pcts[7] = (float(doc['gaming']))# / float(doc['total']))
        pcts[8] = (float(doc['fashion']) )#/ float(doc['total']))
        pcts[9] = (float(doc['music']) )#/ float(doc['total']))
        
    catcount = []
    for item in zip(interests,pcts):
        catcount.append(item)
    print(pcts)

    return pcts

def getTotal(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    total = 0
    for doc in cursor:
        total = (doc['tech']) + (doc['sports']) + (doc['art']) + (doc['food']) + (doc['politics']) + (doc['business']) + (doc['unknown']) + (doc['gaming']) + (doc['fashion']) + (doc['music'])

    return total

def getBoth(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    influencerCount = []
    for doc in cursor:
        influencerCount = doc['both']
    print(influencerCount)

    
    return influencerCount



def getProfessionPcts(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    pcts = [0,0,0,0,0,0,0]

    for doc in cursor:
        total = float(doc['casual_user']) + float(doc['youtuber']) + float(doc['writer']) + float(doc['celebrity']) + float(doc['business_expert']) + float(doc['brand_corp'])
        pcts[0] = round(float(doc['casual_user']) / total*100, 2)
        pcts[1] = round(float(doc['youtuber']) / total*100, 2)
        pcts[2] = round(float(doc['writer']) / total*100, 2)
        pcts[3] = round(float(doc['celebrity']) / total*100, 2)
        pcts[4] = round(float(doc['business_expert']) / total*100, 2)
        pcts[5] = round(float(doc['brand_corp']) / total*100, 2)
        pcts[6] = round(float(doc['academic']) / total*100, 2)
   # pcts = [int(i) for i in pcts]

    return pcts

def getLanguagePCts(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    pcts = [0,0,0,0,0]

    for doc in cursor:
    	en = (float(doc['en'])+float(doc['en-gb']))
    	sp = (float(doc['sp']))
    	other = (float(doc['total']) - (en + sp))
    	pcts[0] = en / float(doc['total'])*100
    	pcts[1] = sp / float(doc['total'])*100
    	pcts[2] = other / float(doc['total'])*100
    pcts=  [int(i) for i in pcts]

    return pcts

def getBrands():
    client = MongoClient()
    db = client.brands_db
    collections = sorted(db.collection_names(), key=str.lower)
    
    print(collections)
    return collections

def getUsernames(brand, num, interest, profession):
    num = int(num)
    client = MongoClient()
    db = client.users_db
    if(profession =="all" and interest == "all"):
        print("profession and interest is all")
        cursor = db.users.find({"$and" : [{'brands': brand}, {'flag' : False}]}).limit(num)
    elif(interest == "all"):
        print("interest is all")
        cursor = db.users.find({"$and" : [{'brands': brand}, {"highestInfluence" : profession}, {'flag' : False}]}).limit(num)
    elif(profession =="all"):
        print("profession is all")
        cursor = db.users.find({"$and" : [{'brands': brand}, {"highestInterest" : interest}, {'flag': False}]}).limit(num)
    else:
        print("both")
        cursor = db.users.find({"$and" : [{'brands': brand}, {"highestInterest" : interest}, {"highestInfluence" : profession}, {'flag': False}]}).limit(num)
    doc_array = []
    for doc in cursor:
        name = doc["screen_name"]
        bio = doc["bio"]
        array1 = [name, bio]
        doc_array.append(array1)

        
    print(doc_array)
    return doc_array

def report(username, interest, influence):

    print(username)
    client = MongoClient()
    cursor = client.users_db.users.find({'screen_name' : username})
    print(cursor.count())
    for user in cursor:
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

def flagUser(username):
    client = MongoClient()
    client.users_db.users.update(
        { 'screen_name': username },
          {
            '$set': {
              "flag": True
            }
          }
    )

def getDis(brand):
    client = MongoClient()
    db_current = client.current_db
    cursor = db_current.current.find({'brand': brand})
    dists=[0,0,0,0,0,0,0,0,0,0,0]
    for doc in cursor:
        dists[0] = (doc['nobiodist'])
        dists[1] = (doc['techdist'])
        dists[2] = (doc['fashiondist'])
        dists[3] = (doc['gamingdist'])
        dists[4] = (doc['artdist'])
        dists[5] = (doc['sportsdist'])
        dists[6] = (doc['fooddist'])
        dists[7] = (doc['poldist'])
        dists[8] = (doc['bizdist'])
        dists[9] = (doc['musicdist'])
        dists[10] = (doc['fulldist'])
    return dists
