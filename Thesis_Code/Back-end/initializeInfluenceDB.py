import tweepy
from tweepy import OAuthHandler
from itertools import cycle
import time
import pickle
from pymongo import MongoClient

sets = 5
key = 0
key_cycle = cycle(range(0,sets))

#API KEYS
CONSUMER_KEY       =     [
            'IaNc49MSj4BFQCE5txsZGO38C',
            '5Q53ZAFMikFU9qSGeEGhWFMCK',
            'zU5cVXdYWyLRpHWnw4HJ2nMEH',
            'STYydh05pVfg8g3sk3WPl3olO',
            'WQW8XQfgsyMhYprMLhbLDNUMs',
            'UaGCGoELlrcyDdyvBti5Ej35a',
            'ijWJksuc5EUEnVFMQZgwHGxr9',
            'csrsm9PcnevSPxSKHGk0fRDyM',
            'Uca7hOrDp0cDkITmbz9M0rE8N',
            'mTzztjybcdDiMROkP8WTV6viy'
            ]
CONSUMER_SECRET    =     [
            'Mo5LuQlyyxuVM3sb1qqCsvXrKS6DYhNcI09L4tJ4QA1KLfXsRf',
            'DObc6k8QgRitM5K3FUeIbrpe0Us0QaUKXJNkXlySGxCfxxWbRs',
            'GjksjXC3wzf8KwVKlPf61V2h17Bz3enxym14aQs1KypIpefmXH',
            'wk4EYd7apTq9EHOZQBGoMGoNGariT19TLcbsGQEv0q3QVwFbIi',
            'J8vmE6TSkcnCS79WAzXfdAYYucmauEWJrHkDe0bjGTAWuuSX0F',
            'xvdpylM5KSdrZQGV3lDV2yDoo9jQ5qthNXuZBrjXYwrMn0MxNj',
            'wOgeyd52T2jWJJMfXGtaO28CCUEgGhaQmqbsMsDVHFva6I9tCT',
            '6goPwIaqbRPwZYA3Dcyarffid1guhiTT9czgRSuBa3u28ImBXF',
            'mGi9bncEv47X4NYrOsXQTNsaVoBwTtD6K8Z8sGbtcqwk9nE6kT',
            '2NawKGXMrh5XyGeVAFSyTILhEQiKAx2788xF8txuSzsqVbJw21'
            ]	
OAUTH_TOKEN        =     [	
            '743126394432040960-ZNxyQOQvM1MLkzakYL3Nfgo35NP9rMJ',
            '198256534-mJtqR6btkKF5x8YCpMgFhFokZU8abS7hTsy2j4bP',
            '198256534-3FUL51zQtHZnFevGcpTOdgwG8VrB5s4VlG3cwQpC',
            '198256534-UQxRP9D8UZiAlHKOnT3Hf6sEMKwWJet8T8qm9SBD',
            '743465390915919872-HEGyRJfayv3x2dNhN1LnpGB9tIM69NR',
            '743465390915919872-3BJxG7xzpGOaBydnMDNB9LSSNVIOqWc',
            '743465390915919872-Jjt7US7vRdvMhzC1tz8cAIUVAx0z7WG',
            '743465390915919872-mgU0Ju8IiEqO88XJa3XEF2J9oDjEHy3',
            '743465390915919872-lLfJQlzNbLZ67AmtX3B05QRCUASt7Ko',
            '743465390915919872-xXb3wi8vpxPvOPUNxCMLAZdT4n2JIe7'
            ]
OAUTH_TOKEN_SECRET = 	 [      
            'cyKMFUPwDbLj1Ew8pVK1tIpEXOpOwfH8KRtkJxPWTVKHO',
            'oN23zFXNCR73po9VdXNONsfpojNZem9F9poI5OBtVXpTL',
            'TU7Hj0tJ3qmLSVTWZGmuFE8eNCWQvxp7R4R0Rchskc5U5',
            'TSTdQC83ozbTfmmrD4uxBtm8bRHR3ILUgbVIlRNAKOkMY',
            'AfYFtkmAFM9dSpwPyVGB8Xy4ONDorEXcmDku8hu6szHMX',
            'Et6wuHdOJ6irUd9E1tstn5qoltm3HiwgxI8R2SnHPHhaw',
            'bCJELSuI40EPFlevcbEVZ9Pac8Ir0PRfT1CdnX8NcoUdS',
            'Wq9Xht0usAMfLyOoToNFcF3RZFsCtHb13m2r4UDVoiYNT',
            'yZV2TBWwHLPVVtrU917HAznaOW2xpsTLIbFcviMHRCd8N',
            'smhjUJ8wgkyHGKy1Ur0Fj0j4Rk3ximhV4yelghtbhwypv'
            ]
Set=[CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET]

#Initial Authorization

auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
api = tweepy.API(auth)

limit = api.rate_limit_status()
limit_remaining = limit['resources']['application']['/application/rate_limit_status']['remaining']

print('Key: ', key, 'Requests Remaining: ', limit_remaining )
while(limit_remaining == 0):  
   key = next(key_cycle)
   print("###LIMIT REACHED, SWITCHING KEYS###")
   print('###USING KEY SET #',key)
   auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
   auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
   api = tweepy.API(auth)
   limit = api.rate_limit_status()
   limit_remaining = limit['resources']['application']['/application/rate_limit_status']['remaining']
   

label_count = 7

Normal = [
   ['followsample','masons_dev'],
   ['normal-people','idk'],
   [1],
   ['casual_user']
]
YouTube = [
   ['ijustine'],
   ['youtubers'],
   [0],
   ['youtuber']
]
Journalist = [
   ['followsample'],
   ['journalists'],
   [0],
   ['writer']
]
Celebrity = [
    ['mashable','Jason_Pollock'],
    ['celebrity','twitter-giants'],
    [1],
    ['celebrity']
]
Biz = [
    ['DnBb2b'],
    ['smallbiz-most-influential'],
    [0],
    ['business_expert']
]
Corp = [
   ['jcdundore','mashable'],
   ['brands','brands'],
   [1],
   ['brand_corp']
]
Student = [
   ['LElliottDorans','drfangirlphd','stephanievainer'],
   ['academic-types', 'awesome-academics', 'student-life'],
   [2],
   ['academic']
]


def total_members(api,list_array,list_count):
   list_counter = 0
   total_members = 0
   while (list_counter <= list_count):
      list_info = api.get_list(owner_screen_name = list_array[0][list_counter], slug = list_array[1][list_counter])
      list_member_count = list_info.member_count
      print(list_array[0][list_counter], "has", list_member_count, "members" )
      total_members += list_member_count
      list_counter += 1
   return total_members
did_switch_key = False
userList = []

def users(api,user_array,client):     
   userList = []
   list_counter = 0
   while(list_counter <= user_array[2][0]):
      cursor = tweepy.Cursor(api.list_members, owner_screen_name = user_array[0][list_counter], slug = user_array[1][list_counter])
      print("Getting users from", user_array[0][list_counter])
      for userFromCursor in cursor.items():
         client.training_db.influence.save( {
                        "_id" : userFromCursor.id,
                        "name": userFromCursor.name, 
                        "screen_name" : userFromCursor.screen_name, 
                        "verified" : userFromCursor.verified, 
                        "followers" : userFromCursor.followers_count, 
                        "tweets" : userFromCursor.statuses_count, 
                        "location" : userFromCursor.location, 
                        "language" : userFromCursor.lang, 
                        "time_zone" : userFromCursor.time_zone, 
                        "bio" : userFromCursor.description,
                        "brands" : [],
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "category":  user_array[3][0]
                    })
         
         userDict= {
                        "_id" : userFromCursor.id,
                        "name": userFromCursor.name, 
                        "screen_name" : userFromCursor.screen_name, 
                        "verified" : userFromCursor.verified, 
                        "followers" : userFromCursor.followers_count, 
                        "tweets" : userFromCursor.statuses_count, 
                        "location" : userFromCursor.location, 
                        "language" : userFromCursor.lang, 
                        "time_zone" : userFromCursor.time_zone, 
                        "bio" : userFromCursor.description,
                        "brands" : [],
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "category":  user_array[3][0]
                    }         
         userList.append(userDict)
      list_counter+=1
   return userList


normal_counted = False
youtube_counted = False
journalist_counted = False
celebrity_counted = False
biz_counted = False
corp_counted=False
student_counted=False
counted=False

normal_users_acquired = False
youtube_users_acquired = False
journalist_users_acquired = False
celebrity_users_acquired = False
biz_users_acquired = False
corp_users_acquired=False
student_users_acquired=False

client = MongoClient()
while(counted == False):
   try:
      if normal_counted == False:
         normal_count = total_members(api,Normal,Normal[2][0])
         if normal_users_acquired == False:
            userList.append(users(api,Normal,client))
            normal_users_acquired=True
         print("Normal Member count:",normal_count)
         normal_counted = True
      if youtube_counted == False:
         youtube_count = total_members(api,YouTube,YouTube[2][0])
         if youtube_users_acquired == False:
            userList.append(users(api,YouTube,client))
            youtube_users_acquired=True
         print("Youtube Member count:",youtube_count)
         youtube_counted = True
      if journalist_counted == False:
         journalist_count = total_members(api,Journalist,Journalist [2][0])
         if journalist_users_acquired == False:
            userList.append(users(api,Journalist,client))
            journalist_users_acquired=True
         print("Journalist  Member count:",journalist_count)
         journalist_counted = True
      if celebrity_counted == False:
         celebrity_count = total_members(api,Celebrity,Celebrity[2][0])
         if celebrity_users_acquired == False:
            userList.append(users(api,Celebrity,client))
            celebrity_users_acquired=True
         print("Celebrity member count:",celebrity_count)
         celebrity_counted = True
      if biz_counted == False:    
         biz_count = total_members(api,Biz,Biz[2][0])
         if biz_users_acquired == False:
            userList.append(users(api,Biz,client))
            biz_users_acquired=True
         print("Biz member count:",biz_count)
         biz_counted = True  
      if corp_counted == False:    
         corp_count = total_members(api,Corp,Corp[2][0])
         if corp_users_acquired == False:
            userList.append(users(api,Corp,client))
            corp_users_acquired=True
         print("corp member count:",corp_count)
         corp_counted = True  
      if student_counted == False:    
         student_count = total_members(api,Student,Student[2][0])
         if student_users_acquired == False:
            userList.append(users(api,Student,client))
            student_users_acquired=True
         print("corp member count:",student_count)
         corp_counted = True  
      count = [normal_count,youtube_count,journalist_count,celebrity_count,biz_count,corp_count,student_count]
      member_count = sum(count)

      counted = True
      print(member_count)

   except tweepy.TweepError as e:
      print(e.args)
      print("###Rate Limit Exceeded###")
      #check first key
      if (key == (sets - 1)):
         auth = OAuthHandler(Set[0][0],Set[1][0])
         auth.set_access_token(Set[2][0],Set[3][0])
         api = tweepy.API(auth) 
         limit = api.rate_limit_status()
         limit_remaining = limit['resources']['lists']['/lists/members']['remaining']
         if (limit_remaining != 15):
            print("Sleeping for 15 minutes")
            time.sleep(902)
      key = next(key_cycle)      
      print("###LIMIT REACHED, SWITCHING KEYS###")
      print('###USING KEY SET #',key)
      auth = OAuthHandler(Set[0][key],Set[1][key])
      auth.set_access_token(Set[2][key],Set[3][key])
      api = tweepy.API(auth)

classLabels = normal_count*[1]
classLabels.extend([2]*youtube_count)
classLabels.extend([3]*journalist_count)
classLabels.extend([4]*celebrity_count)
classLabels.extend([5]*biz_count)
classLabels.extend([6]*corp_count)
classLabels.extend([7]*student_count)

#a more concise summary of the number of samples and labels
countList = [["casual_user",normal_count],["youtuber",youtube_count],
             ["writer",journalist_count],["celebrity",celebrity_count],
             ["business_expert",biz_count],["brand_corp",corp_count],["academic",student_count]]

with open('influenceSample.pkl','wb') as file:
    pickle.dump(userList,file)
    pickle.dump(countList,file)
    pickle.dump(classLabels,file)
    
print(countList)
print("success")