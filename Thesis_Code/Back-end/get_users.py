import tweepy
import time
from twitter import OAuth, Twitter
from pymongo import MongoClient
from itertools import cycle
import string
import re
from influenceScore import getScore

debugging=False
def get_user_info(twitter_handle):
    #mongodb stuff:
    client = MongoClient()
    db = client.users_db
    db_brands = client.brands_db
    key = 0   
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
    sets = len(CONSUMER_KEY)
    key_cycle = cycle(range(0,sets)) 
    Set=[CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET]
    auth = tweepy.OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
    auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
    api = tweepy.API(auth)
    limit = api.rate_limit_status()
    limit_remaining = limit['resources']['users']['/users/lookup']['remaining']
    print('Key: ', key, 'Requests Remaining: ', limit_remaining )
    # Go to first key that has calls left
    while(limit_remaining == 0):      
       key = next(key_cycle)
       print("###LIMIT REACHED, SWITCHING KEYS###")
       print('###USING KEY SET #',key)
       auth = tweepy.OAuthHandler(CONSUMER_KEY[key], CONSUMER_SECRET[key])
       auth.set_access_token(OAUTH_TOKEN[key],OAUTH_TOKEN_SECRET[key])
       api = tweepy.API(auth)
       limit = api.rate_limit_status()
       limit_remaining = limit['resources']['users']['/users/lookup']['remaining']
    total = db_brands[twitter_handle].count()
    n = total
    count = 0
    while n >= 0: # Run through 100 followers at a time. Switch keys each time the current one reaches its rate limit.
        while True:
            try:
                ids_100 = db_brands[twitter_handle].find().skip(total - n).limit(100)
                ids_100_list = []
                for document in ids_100:
                    ids_100_list.append(document["_id"])
                users = api.lookup_users(ids_100_list)
                n = n - 100
            except tweepy.TweepError as e:
                print("###Rate Limit Exceeded###")
                #check first key
                if (key == (sets - 1)):
                 print("key thing")
                 auth = tweepy.OAuthHandler(Set[0][0],Set[1][0])
                 auth.set_access_token(Set[2][0],Set[3][0])
                 api = tweepy.API(auth) 
                 limit_remaining = limit['resources']['users']['/users/lookup']['remaining']
                 if (limit_remaining != 180):
                    print("Sleeping for secs")
                    time.sleep(30)
                key = next(key_cycle)      
                print("###LIMIT REACHED, SWITCHING KEYS###")
                print('###USING KEY SET #',key)
                auth = tweepy.OAuthHandler(Set[0][key],Set[1][key])
                auth.set_access_token(Set[2][key],Set[3][key])
                api = tweepy.API(auth)
                limit = api.rate_limit_status()
                continue
            #print("Done with row")
            break
        # Notify every time 1000 users have their info pulled
        count = count + 100
        if (count % 1000 == 0):
            print(str(count) + " users have their info extracted")        
        # Get user information              
        for user in users:          
            user_id = user.id
            user_exists = db.users.find({'_id' : user_id}).count() > 0
            name = user.name
            screen_name = user.screen_name
            verified = user.verified
            followers = user.followers_count
            friends = user.friends_count
            location = user.location
            bio = user.description
            lang = user.lang
            time_zone = user.time_zone
            tweets = user.statuses_count
            listedCount = user.listed_count
            if(user.friends_count==0):
                user.friends_count +=1
            followRatio = user.followers_count/user.friends_count 
            lastTweetReactions = 0
            if (user.statuses_count >1 and not(user.protected)):
                try:                    
                    lastTweetReactions = user.status.favorite_count + user.status.retweet_count
                except:
                    lastTweetReactions = 0
            # Get each user's influence score
            influenceScore = getScore(listedCount,followers,friends,lastTweetReactions,verified)     

            if(debugging):
                print(screen_name)               
                print(listedCount)
                print(followRatio)
                print(lastTweetReactions)                
                print(verified)
                print(influenceScore)                
                print('\n')
            brand = twitter_handle            
            #Filter users (flag):
            flag = False
            # Check follower to friends ratio first:
            if(friends>0):                
                if((followRatio) < 0.01):
                    flag = True
            else:
                flag = True
            if(flag == False): # Then check bio for swear words
                bio_lower = bio.lower() # Lowercase
                bio_striped = bio_lower.translate(bio_lower.maketrans("","", string.punctuation)) #get rid of punctuation
                # Words to filter:
                words = [                    '2g1c',                    '2 girls 1 cup',                    'acrotomophilia',                    'anal',                    'anilingus',                    'anus',                    'arsehole',                    'ass',                    'asshole',                    'assmunch',                    'auto erotic',                    'autoerotic',                    'babeland',                    'baby batter',                    'ball gag',                    'ball gravy',                    'ball kicking',                    'ball licking',                    'ball sack',                    'ball sucking',                    'bangbros',                    'bareback',                    'barely legal',                    'barenaked',                    'bastardo',                    'bastinado',                    'bbw',                    'bdsm',                    'beaver cleaver',                    'beaver lips',                    'bestiality',                    'bi curious',                    'big black',                    'big breasts',                    'big knockers',                    'big tits',                    'bimbos',                    'birdlock',                    'bitch',                    'black cock',                    'blonde action',                    'blonde on blonde action',                    'blow j',                    'blow your l',                    'blue waffle',                    'blumpkin',                    'bollocks',                    'bondage',                    'boner',                    'boob',                    'boobs',                    'booty call',                    'brown showers',                    'brunette action',                    'bukkake',                    'bulldyke',                    'bullet vibe',                    'bung hole',                    'bunghole',                    'busty',                    'butt',                    'buttcheeks',                    'butthole',                    'camel toe',                    'camgirl',                    'camslut',                    'camwhore',                    'carpet muncher',                    'carpetmuncher',                    'chocolate rosebuds',                    'circlejerk',                    'cleveland steamer',                    'clit',                    'clitoris',                    'clover clamps',                    'clusterfuck',                    'cock',                    'cocks',                    'coprolagnia',                    'coprophilia',                    'cornhole',                    'cum',                    'cumming',                    'cunnilingus',                    'cunt',                    'darkie',                    'date rape',                    'daterape',                    'deep throat',                    'deepthroat',                    'dick',                    'dildo',                    'dirty pillows',                    'dirty sanchez',                    'dog style',                    'doggie style',                    'doggiestyle',                    'doggy style',                    'doggystyle',                    'dolcett',                    'domination',                    'dominatrix',                    'dommes',                    'donkey punch',                    'double dong',                    'double penetration',                    'dp action',                    'eat my ass',                    'ecchi',                    'ejaculation',                    'erotic',                    'erotism',                    'escort',                    'ethical slut',                    'eunuch',                    'faggot',                    'fecal',                    'felch',                    'fellatio',                    'feltch',                    'female squirting',                    'femdom',                    'figging',                    'fingering',                    'fisting',                    'foot fetish',                    'footjob',                    'frotting',                    'fuck',                    'fucking',                    'fuck buttons',                    'fudge packer',                    'fudgepacker',                    'futanari',                    'g-spot',                    'gang bang',                    'gay sex',                    'genitals',                    'giant cock',                    'girl on',                    'girl on top',                    'girls gone wild',                    'goatcx',                    'goatse',                    'gokkun',                    'golden shower',                    'goo girl',                    'goodpoop',                    'goregasm',                    'grope',                    'group sex',                    'guro',                    'hand job',                    'handjob',                    'hard core',                    'hentai',                    'homoerotic',                    'honkey',                    'hooker',                    'hot chick',                    'how to kill',                    'how to murder',                    'huge fat',                    'humping',                    'incest',                    'intercourse',                    'jack off',                    'jail bait',                    'jailbait',                    'jerk off',                    'jigaboo',                    'jiggaboo',                    'jiggerboo',                    'jizz',                    'juggs',                    'kike',                    'kinbaku',                    'kinkster',                    'kinky',                    'knobbing',                    'leather restraint',                    'leather straight jacket',                    'lemon party',                    'lolita',                    'lovemaking',                    'make me come',                    'male squirting',                    'masturbate',                    'menage a trois',                    'milf',                    'missionary position',                    'motherfucker',                    'mound of venus',                    'mr hands',                    'muff diver',                    'muffdiving',                    'nambla',                    'nawashi',                    'negro',                    'neonazi',                    'nig nog',                    'nigga',                    'nigger',                    'nimphomania',                    'nipple',                    'nipples',                    'nsfw images',                    'nude',                    'nudity',                    'nympho',                    'nymphomania',                    'octopussy',                    'omorashi',                    'one cup two girls',                    'one guy one jar',                    'orgasm',                    'orgy',                    'paedophile',                    'panties',                    'panty',                    'pedobear',                    'pedophile',                    'pegging',                    'penis',                    'phone sex',                    'piece of shit',                    'piss pig',                    'pissing',                    'pisspig',                    'playboy',                    'pleasure chest',                    'pole smoker',                    'ponyplay',                    'poof',                    'poop chute',                    'poopchute',                    'porn',                    'porno',                    'pornography',                    'prince albert piercing',                    'pthc',                    'pubes',                    'pussy',                    'queaf',                    'raghead',                    'raging boner',                    'rape',                    'raping',                    'rapist',                    'rectum',                    'reverse cowgirl',                    'rimjob',                    'rimming',                    'rosy palm',                    'rosy palm and her 5 sisters',                    'rusty trombone',                    's&m',                    'sadism',                    'scat',                    'schlong',                    'scissoring',                    'semen',                    'sex',                    'sexo',                    'sexy',                    'shaved beaver',                    'shaved pussy',                    'shemale',                    'shibari',                    'shit',                    'shota',                    'shrimping',                    'slanteye',                    'slut',                    'smut',                    'snatch',                    'snowballing',                    'sodomize',                    'sodomy',                    'spic',                    'spooge',                    'spread legs',                    'strap on',                    'strapon',                    'strappado',                    'strip club',                    'style doggy',                    'suck',                    'sucks',                    'suicide girls',                    'sultry women',                    'swastika',                    'swinger',                    'tainted love',                    'taste my',                    'tea bagging',                    'threesome',                    'throating',                    'tied up',                    'tight white',                    'tit',                    'tits',                    'titties',                    'titty',                    'tongue in a',                    'topless',                    'tosser',                    'towelhead',                    'tranny',                    'tribadism',                    'tub girl',                    'tubgirl',                    'tushy',                    'twat',                    'twink',                    'twinkie',                    'two girls one cup',                    'undressing',                    'upskirt',                    'urethra play',                    'urophilia',                    'vagina',                    'venus mound',                    'vibrator',                    'violet blue',                    'violet wand',                    'vorarephilia',                    'voyeur',                    'vulva',                    'wank',                    'wet dream',                    'wetback',                    'white power',                    'women rapping',                    'wrapping men',                    'wrinkled starfish',                    'xx',                    'xxx',                    'yaoi',                    'yellow showers',                    'yiffy',                    'zoophilia',                    'youre lonely'                    ]
                for word in words:
                    if(re.compile(r'\b({0})\b'.format(bio_striped), flags=re.IGNORECASE).search == True):
                        flag = True
                        break            
            # Insert into mongodb database:
            if(user_exists == False):
                db.users.insert(
                    {
                        "_id" : user_id,
                        "name": name, 
                        "screen_name" : screen_name, 
                        "verified" : verified, 
                        "followers" : followers, 
                        "tweets" : tweets, 
                        "location" : location, 
                        "language" : lang, 
                        "time_zone" : time_zone, 
                        "bio" : bio,
                        "brands" : [brand],
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "flag" : flag,
                        "listedCount": listedCount,
                        "followRatio": followRatio,
                        "lastTweetReactionCount": lastTweetReactions,
                        "influenceScore": influenceScore
                    }
            	)
            else:
                db.users.update(
                    { '_id' : user_id },
                    { '$set' :
                        {
                        "name": name, 
                        "screen_name" : screen_name, 
                        "verified" : verified, 
                        "followers" : followers, 
                        "tweets" : tweets, 
                        "location" : location, 
                        "language" : lang, 
                        "time_zone" : time_zone, 
                        "bio" : bio,
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "listedCount": listedCount,
                        "followRatio": followRatio,
                        "lastTweetReactionCount": lastTweetReactions,
                        "influenceScore": influenceScore
                        }
                    },
                    upsert=False	            
                )

                db.users.update(
                                    { '_id': user_id },
                                    { '$addToSet': { "brands" : brand } }
                            )     
    # For users no longer following the specific brand, remove the brand from the array of brands that they follow
    cursor = db_brands[twitter_handle].find({"active": False})        
    for document in cursor:
        id_to_remove_brand = document["_id"]
        db.users.update({"_id" : id_to_remove_brand}, {"$pull": {"brands" : twitter_handle}})