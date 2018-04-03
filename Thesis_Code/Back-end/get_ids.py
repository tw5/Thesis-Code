import tweepy
from tweepy import OAuthHandler
from itertools import cycle
from pymongo import MongoClient

def get_ids(screen_name):
   client = MongoClient()
   db = client.brands_db
   collectionName = db[screen_name]
   collectionName.update({}, {"$set" : {"active" : False}}, multi = True)  # Set all previous followers as inactive
   # API KEYS
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
            '30TQMX9tqDIoWhepFio2p7MEV',
            'IcCauSBiHOndf90D8FoYunq8o' 
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
            'hqyOjHI6d0j2G1yCLpwR6FnQYGYl7Scldq8sRsxv9BcygPK6q7', 
            'WlUYHdotJW4yYLborbG7Y79VvNJphGUKcO4SkctvK7V5kqIpni'
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
           '1176891456-3ZNiISR9zrMwMx4bqwEss1SlSDfpAsUaNPjcAki',
           '1176891456-5zpoa0a3FvpsAapUtmF1aqsRmBKlqcJjUDe1CUg'
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
            'ucfcrrZhBYjosJ46T0XNliox1zGNlws8gT5g9e54MfKzf',
            'xu7iDJiep46myVzIo7pkObICL9DpYdXW1MBfWMtSywGe3'
            ]
   Set=[CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET]
   sets = len(CONSUMER_KEY)
   key = 0
   key_cycle = cycle(range(0,sets))
   # Initial Authorization
   auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
   auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
   api = tweepy.API(auth)

   limit = api.rate_limit_status()
   limit_remaining = limit['resources']['followers']['/followers/ids']['remaining']
   print('Key: ', key, 'Requests Remaining: ', limit_remaining ) 
   while(limit_remaining == 0): # Start at first key that has calls left    
      key = next(key_cycle)
      print("###LIMIT REACHED, SWITCHING KEYS###")
      print('###USING KEY SET #',key)
      auth = OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
      auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
      api = tweepy.API(auth)
      limit = api.rate_limit_status()
      limit_remaining = limit['resources']['followers']['/followers/ids']['remaining']

   numFollowers = api.get_user(screen_name).followers_count
   print(screen_name, "has", numFollowers)
   counter = 1
   did_switch_key = False
   cursor = tweepy.Cursor(api.followers_ids,screen_name)
   # Returns 5000 user IDs per call, with 15 calls a key.
   # We can get a total of 75,000 user IDs per key before waiting for 15 minutes.
   # However, we have 21 keys, so we cycle to the next one instead of waiting for the
   # key to replenish.
   while(counter <= (numFollowers/5000 + 1)): # Gets 5000 IDs per iteration
      try:   
         # Makes sure that the new key starts where the previous key left off
         if(did_switch_key == True):
            current_cursor = cursor.iterator.next_cursor
            cursor = tweepy.Cursor(api.followers_ids, screen_name, cursor = current_cursor)
            did_switch_key = False        
         for followerid in cursor.pages():                    
            limit = api.rate_limit_status()
            limit_remaining = limit['resources']['followers']['/followers/ids']['remaining']    
            for oneId in followerid: # Store in mongodb
               collectionName.save({"_id" : oneId, "active" : True})      
            if(counter == (numFollowers/5000 +1)): # DONE
               break
            print(str(counter * 5000) + " user IDs gathered") # Show Current Progress           
            counter = counter + 1
      except tweepy.TweepError as e: # Occurs when the rate limit is exceeded. Switches to next key.
         key = next(key_cycle)      
         did_switch_key = True
         print("###LIMIT REACHED, SWITCHING KEYS###")
         print('###USING KEY SET #',key)
         auth = OAuthHandler(Set[0][key],Set[1][key])
         auth.set_access_token(Set[2][key],Set[3][key])
         api = tweepy.API(auth) 