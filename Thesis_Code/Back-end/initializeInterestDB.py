import tweepy
from tweepy import OAuthHandler
from itertools import cycle
import time
import pickle
from pymongo import MongoClient

sets = 20
key = 0
key_cycle = cycle(range(0,sets))

#API KEYS
CONSUMER_KEY       =     [
            '9XkYgKXCTL6KH0JOws7pkKszG',
            'jwOVv0V5uVdpXTtP5M6DyJv6C',
            'FnBA0hwuwZIhDR1qw0XQFrkla',
            'CZHFL5vpmTdQomW4vIkN9YFx3',
            '869B1o1dObkOCUa6mYK39wLtr',
            'lCUP345500lBRfEHUFFJSnfHC',
            'IaNc49MSj4BFQCE5txsZGO38C',
            '5Q53ZAFMikFU9qSGeEGhWFMCK',
            'zU5cVXdYWyLRpHWnw4HJ2nMEH',
            'STYydh05pVfg8g3sk3WPl3olO',
            'WQW8XQfgsyMhYprMLhbLDNUMs',
            'UaGCGoELlrcyDdyvBti5Ej35a',
            'ijWJksuc5EUEnVFMQZgwHGxr9',
            'csrsm9PcnevSPxSKHGk0fRDyM',
            'Uca7hOrDp0cDkITmbz9M0rE8N',
            'mTzztjybcdDiMROkP8WTV6viy',
            'FXbfn41cvtaSf7lqit497360j',
            'mp0MhtO7xdavD1JDZfGrMSkkH',
            'YP3TpcyqDIGTcaaQ6oCjHSeSy',
            '30TQMX9tqDIoWhepFio2p7MEV'
            ]
CONSUMER_SECRET    =     [
            '7wdo3HpkOlvS9cfxoAqmRKOuyJcAyx9EEuARBRzFKnfX3yhDL5',
            'mEI4IFTj31LmePCNUElz4BxV0fNch069pa5c4t8iNe8jYOsfoL',
            '0slkgdEH3istWudTcfX1BlucCqVBikHmGycjdfmCFO0fm44Rqe',
            'jScXxI48mvhjsl5wKCrIr1Ie1ay6MKMUVR77xYZdZONHZFCgrE',
            'kM5lG4QmKo7adftZH5P54WBojC1ZjffKXuNoeGm3GG99TDmZ1Q',
            'NVrvIMy4F4AyfvzUEpjqQRwYAt4lCr8uZmPzpmQYYixr1Oy4MC',
            'Mo5LuQlyyxuVM3sb1qqCsvXrKS6DYhNcI09L4tJ4QA1KLfXsRf',
            'DObc6k8QgRitM5K3FUeIbrpe0Us0QaUKXJNkXlySGxCfxxWbRs',
            'GjksjXC3wzf8KwVKlPf61V2h17Bz3enxym14aQs1KypIpefmXH',
            'wk4EYd7apTq9EHOZQBGoMGoNGariT19TLcbsGQEv0q3QVwFbIi',
            'J8vmE6TSkcnCS79WAzXfdAYYucmauEWJrHkDe0bjGTAWuuSX0F',
            'xvdpylM5KSdrZQGV3lDV2yDoo9jQ5qthNXuZBrjXYwrMn0MxNj',
            'wOgeyd52T2jWJJMfXGtaO28CCUEgGhaQmqbsMsDVHFva6I9tCT',
            '6goPwIaqbRPwZYA3Dcyarffid1guhiTT9czgRSuBa3u28ImBXF',
            'mGi9bncEv47X4NYrOsXQTNsaVoBwTtD6K8Z8sGbtcqwk9nE6kT',
            '2NawKGXMrh5XyGeVAFSyTILhEQiKAx2788xF8txuSzsqVbJw21',
            't8cdQu8o58I8y7nQfEtwMPLzDw8uyeSY8xadTLfbPxeRlOtRxY',
            'TwNdLCVU30Z3ygnsqlu7GWf9QPFcv7M0vyssOTJCM69I7mF6Jz',
            'BsyrHg8SKHqOaALhltqn7HJraL5iIF3faWoVbaAe1Vwxnw76M0',
            'hqyOjHI6d0j2G1yCLpwR6FnQYGYl7Scldq8sRsxv9BcygPK6q7'
            ]	
OAUTH_TOKEN        =     [	
            '745277343736995844-rRDSeonuJbi56e9QkgNpTxLLIJ6zaym',
            '745277343736995844-RYCMDprABDve3CqY2hkCOZOTuWzOcS3',
            '745277343736995844-fsBMNygESaLKxbJbZvhE49l7CoUfUv6',
            '320947567-H5rRzPhUdRIkO7MYeuYxU3pZ0EP8MUJICHHWUM2e',
            '320947567-yLoWHmhe5Dqr3GKNh6hq9raiwgSf6EFWClwPZTCU',
            '320947567-21vMgnoRjemCLYrYlUUvBf8gSyvxzk96uNkSxXqa',
            '743126394432040960-ZNxyQOQvM1MLkzakYL3Nfgo35NP9rMJ',
            '198256534-mJtqR6btkKF5x8YCpMgFhFokZU8abS7hTsy2j4bP',
            '198256534-3FUL51zQtHZnFevGcpTOdgwG8VrB5s4VlG3cwQpC',
            '198256534-UQxRP9D8UZiAlHKOnT3Hf6sEMKwWJet8T8qm9SBD',
            '743465390915919872-HEGyRJfayv3x2dNhN1LnpGB9tIM69NR',
            '743465390915919872-3BJxG7xzpGOaBydnMDNB9LSSNVIOqWc',
            '743465390915919872-Jjt7US7vRdvMhzC1tz8cAIUVAx0z7WG',
            '743465390915919872-mgU0Ju8IiEqO88XJa3XEF2J9oDjEHy3',
            '743465390915919872-lLfJQlzNbLZ67AmtX3B05QRCUASt7Ko',
            '743465390915919872-xXb3wi8vpxPvOPUNxCMLAZdT4n2JIe7',
            '1176891456-f1MgVmWZASgXv3cbEul1E0yvlNxmUddhFUB24PO',
           '1176891456-R4IdAaYGNJ9VnxPBSVfZgl8Ul3A4luHxJiPYOKx',
           '1176891456-gY9ipJFmZgsYrYfZWVocOTLfq7wTJ5PzoNtAGRs',
           '1176891456-3ZNiISR9zrMwMx4bqwEss1SlSDfpAsUaNPjcAki'
            ]
OAUTH_TOKEN_SECRET = 	 [      
            'XlkXHOLAiY7bFUVImAq1qr8qzeWugd5ihbnpnmnlYVMwx',
            'QHOVrvfpki9yj5sZF5x4w4iiQxzKPqZffMvqKGn8CUl6P',
            'AdyGaihD0UAmDIgrsMrtK8ZT0MSgaiPIIDlk8FBI4sFMX',
            'gCKK2e7eLGYUmRK7Wuczxge0NtpFLbvsRDjp6pNvKd15i',
            'A6oSCiCK5ykUfq27V6Fe3EkDTgoJyWiZxBWOGOpkrj7vQ',
            'JEE8Lj8l9nsYibbR73ienudwHo9jdcTdEahQQ8eeMyNIQ',
            'cyKMFUPwDbLj1Ew8pVK1tIpEXOpOwfH8KRtkJxPWTVKHO',
            'oN23zFXNCR73po9VdXNONsfpojNZem9F9poI5OBtVXpTL',
            'TU7Hj0tJ3qmLSVTWZGmuFE8eNCWQvxp7R4R0Rchskc5U5',
            'TSTdQC83ozbTfmmrD4uxBtm8bRHR3ILUgbVIlRNAKOkMY',
            'AfYFtkmAFM9dSpwPyVGB8Xy4ONDorEXcmDku8hu6szHMX',
            'Et6wuHdOJ6irUd9E1tstn5qoltm3HiwgxI8R2SnHPHhaw',
            'bCJELSuI40EPFlevcbEVZ9Pac8Ir0PRfT1CdnX8NcoUdS',
            'Wq9Xht0usAMfLyOoToNFcF3RZFsCtHb13m2r4UDVoiYNT',
            'yZV2TBWwHLPVVtrU917HAznaOW2xpsTLIbFcviMHRCd8N',
            'smhjUJ8wgkyHGKy1Ur0Fj0j4Rk3ximhV4yelghtbhwypv',
            'uwaPy4d9TsIPMFrwjhzryW0N8iWTNbLLsH2T5XfdUo2Uc',
            'nPiyH2jPwFQPJS9LVj85LduI7cW83IblfoDskjjlFRvdZ',
            'yTrMYcxMA0pznOFkeIa3pQMtjH5ItLksUeLNbtOnW58Pw',
            'ucfcrrZhBYjosJ46T0XNliox1zGNlws8gT5g9e54MfKzf'
            ]
Set=[CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET]

#Initial Authorization
auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
api = tweepy.API(auth)
limit = api.rate_limit_status()
limit_remaining = limit['resources']['application']['/application/rate_limit_status']['remaining']

print('Key: ', key, 'Requests Remaining: ', limit_remaining )
while(limit_remaining == 0): # Go to first available key   
   key = next(key_cycle)
   print("###LIMIT REACHED, SWITCHING KEYS###")
   print('###USING KEY SET #',key)
   auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
   auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
   api = tweepy.API(auth)
   limit = api.rate_limit_status()
   limit_remaining = limit['resources']['application']['/application/rate_limit_status']['remaining']
   
label_count = 9
# 1 - Creators of the lists; 2 - Titles of the Lists; 3 - Last index; Category that the lists fall under
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
   ['bigtrix36','Christine_Ng_01'],
   ['food-people','culinary'],
   [1],
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
Unknown = [
   ['masons_dev'],
   ['idk'],
   [0],
   ['Unknown']
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

def users(api,user_array):
   userList = []
   list_counter = 0
   while(list_counter <= user_array[2][0]):
      cursor = tweepy.Cursor(api.list_members, owner_screen_name = user_array[0][list_counter], slug = user_array[1][list_counter])
      print("Getting users from", user_array[0][list_counter])
      for userFromCursor in cursor.items():
          client.training_db.interest.save( {
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
food_counted = False
politics_counted = False
biz_counted = False
unknown_counted = False
counted = False

tech_users_acquired = False
fashion_users_acquired=False
arts_users_acquired = False
music_users_acquired=False
fitness_users_acquired = False
gaming_users_acquired=False
food_users_acquired = False
politics_users_acquired = False
biz_users_acquired = False
unknown_users_acquired = False
client = MongoClient()
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
      if food_counted == False:
         food_count = total_members(api,Food,Food[2][0])
         if food_users_acquired == False:
            userList.append(users(api,Food))
            food_users_acquired==True
         print("Food member count:",food_count)
         food_counted = True
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
      if unknown_counted == False:
         unknown_count = total_members(api,Unknown,Unknown[2][0])
         if unknown_users_acquired == False:
            userList.append(users(api,Unknown))
            unknown_users_acquired=True
         print("Unknown member count:", unknown_count)
         unknown_counted = True

      
      count = [unknown_count,tech_count,gaming_count,fashion_count,arts_count,music_count,fitness_count,food_count,politics_count,biz_count]
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
classLabels.extend([10]*unknown_count)

#a more concise summary of the number of samples and labels
countList = [["Tech",tech_count],["Gaming",gaming_count],
             ["Fashion",fashion_count],["Arts",arts_count],
             ["Music",music_count],["Fitness",fitness_count],
             ["Food",food_count],["Politics",politics_count],
             ["Biz",biz_count],["Unknown", unknown_count]]

with open('dictSample.pkl','wb') as file:
    pickle.dump(userList,file)
    pickle.dump(countList,file)
    pickle.dump(classLabels,file)
    
print(countList)
print("success")     