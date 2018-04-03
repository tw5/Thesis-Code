# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:54:13 2016

Creates the training set for the interest model. 

"""

import tweepy
from tweepy import OAuthHandler
import csv
from itertools import cycle
import time
from twitUser import twitUser
import pickle

sets = 5
key = 0
key_cycle = cycle(range(0,sets))



#API KEYS
CONSUMER_KEY       =     [
	'FXbfn41cvtaSf7lqit497360j',
	#'LxeV1hu5SpRd3tOm3jrfe9PhS', MShare Demo API not working
	'mp0MhtO7xdavD1JDZfGrMSkkH',
	'YP3TpcyqDIGTcaaQ6oCjHSeSy',
	'30TQMX9tqDIoWhepFio2p7MEV',
	#'WU8iHREqeG7lgHXoUQQBr7jv8' Not Working
	'IcCauSBiHOndf90D8FoYunq8o'
	#'Jl51VCRydcXnFLg3oKxuQvjWz'  
	]
CONSUMER_SECRET    =     [
	't8cdQu8o58I8y7nQfEtwMPLzDw8uyeSY8xadTLfbPxeRlOtRxY',
   	#'ShkSpKciB70ZNwbQeGDVIOhmQhnSV4HdnrYrklW6prvF28MLWq'
   	'TwNdLCVU30Z3ygnsqlu7GWf9QPFcv7M0vyssOTJCM69I7mF6Jz',
   	'BsyrHg8SKHqOaALhltqn7HJraL5iIF3faWoVbaAe1Vwxnw76M0',
   	'hqyOjHI6d0j2G1yCLpwR6FnQYGYl7Scldq8sRsxv9BcygPK6q7',
   	#'N616YJkzJjHjTvn7bO7devUH2WeIrlLXhI3qrnfgOLwIgG2byC',  
    'WlUYHdotJW4yYLborbG7Y79VvNJphGUKcO4SkctvK7V5kqIpni'
   	#'MKkJ24t3Rzlwugafmu3JNJZKYxbkPSti92e7rbt3SxT7hSTT3n'
   	]	
OAUTH_TOKEN        =     [	
   	'1176891456-f1MgVmWZASgXv3cbEul1E0yvlNxmUddhFUB24PO',
   	#'1176891456-IjQ3fOwbIpfMvJTHOOQ8RJ00ejtheI0M46zh3gZ',
   	'1176891456-R4IdAaYGNJ9VnxPBSVfZgl8Ul3A4luHxJiPYOKx',
   	'1176891456-gY9ipJFmZgsYrYfZWVocOTLfq7wTJ5PzoNtAGRs',
   	'1176891456-3ZNiISR9zrMwMx4bqwEss1SlSDfpAsUaNPjcAki',
   	#'745277343736995844-mJljXBfxvztSLxICB4NKNAMiUlGwyWR'
   	'1176891456-5zpoa0a3FvpsAapUtmF1aqsRmBKlqcJjUDe1CUg',
   	#'1176891456-h9DqbQJHl5mommocxJTslR7Jx3vqhXABVjaTGoX'
   	]
OAUTH_TOKEN_SECRET = 	 [      
   	'uwaPy4d9TsIPMFrwjhzryW0N8iWTNbLLsH2T5XfdUo2Uc',
   	#'M71Es3XEs91zlZ8udRTBnHUq5lOpwgX9DJW2rPYK1qEUS',
   	'nPiyH2jPwFQPJS9LVj85LduI7cW83IblfoDskjjlFRvdZ',
   	'yTrMYcxMA0pznOFkeIa3pQMtjH5ItLksUeLNbtOnW58Pw',
   	'ucfcrrZhBYjosJ46T0XNliox1zGNlws8gT5g9e54MfKzf',
   	#'oJjsnxoy1mt4ymCMJcCIBoZsZY83Uz6hnNPB2BZGfMEdq',
   	'xu7iDJiep46myVzIo7pkObICL9DpYdXW1MBfWMtSywGe3',
   	#'ZjT4f85jXAnwDc9G7mxLbXs7r785fA9Vz63SEpAjPTGET'
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
   

label_count = 9

Tech = [
   ['cramklop','chadundrwood','benthos4','masons_dev'],
   ['it-professionals','people-tech','tech-stuff','tech'],
   [3],
   ['Tech']
]
Gaming = [
   ['markthomson','MVPsportslife','sigriffiths_','mike_T010','masons_dev'],
   ['videogames','gaming','gaming','video-games','gaming'],
   [4],
   ['Gaming']
]
Fashion = [
   ['ninatypewriter','LisaBain','masons_dev'],
   ['fashion','beauty','beauty-fashion'],
   [2],
   ['Fashion']
]
Arts = [
    ['kerrybtone'],
    ['creatives'],
    [0],
    ['Arts']
]
Music = [
    ['masons_dev','ARtalentmgmt','SpunnOne'],
    ['music','indie-bloggers-reviews','music1'],
    [2],
    ['Music']
]
Fitness = [
   ['fitpronowapp','Billy_Shmurda','masons_dev'],
   ['fitness','athletes1','sports-fitness'],
   [2],
   ['Fitness/Sports']
]
Food = [
   ['bigtrix36','Christine_Ng_01','FoodieRegistry','DrewHunter33'],
   ['food-people','culinary','restaurants-7','food'],
   [3],
   ['Food']
]
Politics = [
   ['verified','scottbeedy','masons_dev'],
   ['us-congress','politics','politics-fans'],
   [2],
   ['Politics']
]
Biz = [
   ['dnbb2b','masons_dev'],
   ['small-biz-owners','business-finance'],
   [1],
   ['Biz']
]

def total_members(api,list_array,list_count):
   counter_mem = 0
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

def users(api,user_array):
   userList = []
   list_counter = 0
   did_switch_key = False
   while(list_counter <= user_array[2][0]):
      cursor = tweepy.Cursor(api.list_members, owner_screen_name = user_array[0][list_counter], slug = user_array[1][list_counter])
      print("Getting users from", user_array[0][list_counter])
      if(did_switch_key == True):
         current_cursor = cursor.iterator.next_cursor
         cursor = tweepy.Cursor(api.list_members, owner_screen_name = user_array[0][list_counter], slug = user_array[1][list_counter], cursor = current_cursor)
         did_switch_key = False
      for userFromCursor in cursor.items():
         userDict = {
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

tech_counted = False
gaming_counted=False
arts_counted = False
music_counted=False
fitness_counted = False
fashion_counted = False
#normal_counted = False
#celeb_counted = False
#youtube_counted = False
food_counted = False
#journalist_counted = False
#sports_counted = False
politics_counted = False
biz_counted = False
counted = False

tech_users_acquired = False
fashion_users_acquired=False
arts_users_acquired = False
music_users_acquired=False
fitness_users_acquired = False
gaming_users_acquired=False
#normal_users_acquired = False
#celeb_users_acquired = False
#youtube_users_acquired = False
food_users_acquired = False
#journalist_users_acquired = False
#sports_users_acquired = False
politics_users_acquired = False
biz_users_acquired = False

while(counted == False):
   try:
      if tech_counted == False:
         tech_count = total_members(api,Tech,Tech[2][0])
         if tech_users_acquired == False:
            userList.append(users(api,Tech))
            tech_users_acquired=True
         print("Tech Member count:",tech_count)
         tech_counted = True
      if gaming_counted == False:
         gaming_count = total_members(api,Gaming,Gaming[2][0])
         if gaming_users_acquired == False:
            userList.append(users(api,Gaming))
            gaming_users_acquired=True
         print("Gaming Member count:",gaming_count)
         gaming_counted = True
      if fashion_counted == False:
         fashion_count = total_members(api,Fashion,Fashion[2][0])
         if fashion_users_acquired == False:
            userList.append(users(api,Fashion))
            fashion_users_acquired=True
         print("Fashion  Member count:",fashion_count)
         fashion_counted = True
      if arts_counted == False:
         arts_count = total_members(api,Arts,Arts[2][0])
         if arts_users_acquired == False:
            userList.append(users(api,Arts))
            arts_users_acquired=True
         print("Art member count:",arts_count)
         arts_counted = True
      if music_counted == False:
         music_count = total_members(api,Music,Music[2][0])
         if music_users_acquired == False:
            userList.append(users(api,Music))
            music_users_acquired=True
         print("Music member count:",music_count)
         music_counted = True
      if fitness_counted == False:
         fitness_count = total_members(api,Fitness,Fitness[2][0])
         if fitness_users_acquired == False:
            userList.append(users(api,Fitness))
            fitness_users_acquired=True
         print("Fitness memeber count:",fitness_count)
         fitness_counted = True
#      if normal_counted == False:
#         normal_count = total_members(api,Normal,Normal[2][0])
#         if normal_users_acquired == False:
#            userList.append(users(api,Normal))
#            normal_users_acquired=True
#         print("Normal member count:",normal_count)
#         normal_counted = True
#      if celeb_counted == False:
#         celeb_count = total_members(api,Celeb,Celeb[2][0])
#         if celeb_users_acquired == False:
#            userList.append(users(api,Celeb))
#            celeb_users_acquired=True
#         print("Celeb member count:",celeb_count)
#         celeb_counted = True
#      if youtube_counted == False:
#         youtube_count = total_members(api,Celeb,Celeb[2][0])
#         if youtube_users_acquired == False:
#            userList.append(users(api,Youtube))
#            youtube_users_acquired=True
#         print("Youtube member count:",youtube_count)
#         youtube_counted = True
      if food_counted == False:
         food_count = total_members(api,Food,Food[2][0])
         if food_users_acquired == False:
            userList.append(users(api,Food))
            food_users_acquired==True
         print("Food member count:",food_count)
         food_counted = True
#      if journalist_counted == False:  
#         journalist_count = total_members(api,Journalist,Journalist[2][0])
#         if journalist_users_acquired == False:
#            userList.append(users(api,Journalist))
#            journalist_users_acquired=True
#         print("Journalist member count:",journalist_count)
#         journalist_counted = True 
#      if sports_counted == False:
#         sports_count = total_members(api,Sports,Sports[2][0])
#         if sports_users_acquired == False:
#            userList.append(users(api,Sports))
#            sports_users_acquired=True
#         print("Sports member count:",sports_count)
#         sports_counted = True
      if politics_counted == False:  
         politics_count = total_members(api,Politics,Politics[2][0])
         if politics_users_acquired == False:
            userList.append(users(api,Politics))
            politics_users_acquired=True
         print("Politics member count:",politics_count)
         politics_counted = True
      if biz_counted == False:    
         biz_count = total_members(api,Biz,Biz[2][0])
         if biz_users_acquired == False:
            userList.append(users(api,Biz))
            biz_users_acquired=True
         print("Biz member count:",biz_count)
         biz_counted = True  

      
      count = [tech_count,gaming_count,fashion_count,arts_count,music_count,fitness_count,food_count,politics_count,biz_count]
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

classLabels = tech_count*[1]
classLabels.extend([2]*gaming_count)
classLabels.extend([3]*fashion_count)
classLabels.extend([4]*arts_count)
classLabels.extend([5]*music_count)
classLabels.extend([6]*fitness_count)
classLabels.extend([7]*food_count)
classLabels.extend([8]*politics_count)
classLabels.extend([9]*biz_count)

#a more concise summary of the number of samples and labels
countList = [["Tech",tech_count],["Gaming",gaming_count],
             ["Fashion",fashion_count],["Arts",arts_count],
             ["Music",music_count],["Fitness",fitness_count],
             ["Food",food_count],["Politics",politics_count],
             ["Biz",biz_count]]

with open('dictSample.pkl','wb') as file:
    pickle.dump(userList,file)
    pickle.dump(countList,file)
    pickle.dump(classLabels,file)
    
print(countList)
print("success")

      