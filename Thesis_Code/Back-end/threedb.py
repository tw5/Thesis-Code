from pymongo import MongoClient
import time
import statistics
import numpy

def createThird(screenName):

    varianceThreshold = .021

    unknownCount =0
    gamingCount = 0
    techCount=0
    fashionCount=0
    artCount=0
    sportsCount=0
    foodCount=0
    polCount=0
    bizCount=0
    musicCount = 0

    normal = [0,0,0,0,0,0,0,0,0,0,0]
    youtube = [0,0,0,0,0,0,0,0,0,0,0]
    journal = [0,0,0,0,0,0,0,0,0,0,0]
    celeb = [0,0,0,0,0,0,0,0,0,0,0]
    biz = [0,0,0,0,0,0,0,0,0,0,0]
    brand = [0,0,0,0,0,0,0,0,0,0,0]
    student = [0,0,0,0,0,0,0,0,0,0,0]

    nobiodist = []
    techdist = []
    fashiondist = []
    gamingdist = []
    artdist = []
    sportsdist = []
    fooddist = []
    poldist = []
    bizdist = []
    musicdist = []
    fulldist = []
    for x in range(0,101):
        nobiodist.append([0,[]])
        techdist.append([0,[]])
        fashiondist.append([0,[]])
        gamingdist.append([0,[]])
        artdist.append([0,[]])
        sportsdist.append([0,[]])
        fooddist.append([0,[]])
        poldist.append([0,[]])
        bizdist.append([0,[]])
        musicdist.append([0,[]])
        fulldist.append([0,[]])

    normalCount = 0
    youtubeCount =0
    journalCount=0
    celebCount=0
    bizinfCount=0
    brandCount=0
    studentCount=0

    verifiedCount = 0
    enCount = 0
    spCount = 0
    zhtwCount = 0
    zhcnCount = 0
    frCount = 0
    itCount = 0
    heCount = 0
    deCount = 0
    engbCount = 0

    client = MongoClient()
    db_brands = client.brands_db
    db_users  = client.users_db
    db_results = client.results_db
    db_current = client.current_db

    cursor = db_users.users.find({"brands":screenName})

    #cursor = db_brands[screenName].find({"active": True})
    count = 0
    tweetCount = []
    followCount = []
    influenceCount = []
    for user in cursor:
        #print(celebCount)
        #documentID = document["_id"]
        #user = db_users.users.find_one({"_id" : documentID} )
        #print(count)


        #print(user["screen_name"]+" is "+user["highestInterest"])
        #print(user["bio"])
        #print("\n")
        fulldist = distappend(fulldist, user)
        probabilityArray = [user["tech"],user["gaming"],user["fashion"],
                            user["art"],user["music"],user["sports"],user["pol"],
                            user["food"],user["biz"],user["unknown"]]

        tweetCount.append(user['tweets'])
        followCount.append(user['followers'])
        influenceCount.append(user['influenceScore'])

        if(user["bio"] == "" or user["highestInterest"] == "Unknown"):
            unknownCount+=1
            i=9
            nobiodist = distappend(nobiodist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user["highestInterest"] == "Tech"):
            techCount+=1
            i=0
            techdist = distappend(techdist, user)
            ## Add the users tweets, followers, and influence for tech
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Fashion/Beauty"):
            fashionCount+=1
            i=1
            fashiondist = distappend(fashiondist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Arts/Culture"):
            artCount+=1
            i=2
            artdist = distappend(artdist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Sports/Fitness"):
            sportsCount+=1
            i=3
            sportsdist = distappend(sportsdist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Food"):
            foodCount+=1
            i=4
            fooddist = distappend(fooddist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Politics"):
            polCount+=1
            i=5
            poldist = distappend(poldist,user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Biz"):
            bizCount+=1
            i=6
            bizdist = distappend(bizdist,user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Gaming"):
            gamingCount+=1
            i=7
            gamingdist = distappend(gamingdist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1
        elif(user['highestInterest'] == "Music"):
            musicCount+=1
            i=8
            musicdist = distappend(musicdist, user)
            if(user['highestInfluence'] == 'casual_user'):
                normalCount +=1
                normal[i]+=1
            elif(user['highestInfluence'] == 'youtuber'):
                youtubeCount +=1
                youtube[i]+=1
            elif(user['highestInfluence'] == 'writer'):
                journalCount+=1
                journal[i]+=1
            elif(user['highestInfluence'] == 'celebrity'):
                celebCount+=1
                celeb[i] +=1
            elif(user['highestInfluence'] == 'business_expert'):
                bizinfCount+=1
                biz[i]+=1
            elif(user['highestInfluence'] == 'brand_corp'):
                brandCount+=1
                brand[i]+=1
            elif(user['highestInfluence'] == "academic"):
                studentCount+=1
                student[i]+=1


        if(user["verified"] == True):
              verifiedCount+=1

        if(user["language"] == 'en'):
            enCount+=1        ## English - American
        elif(user['language'] == 'sp'):
            spCount+=1        ## Spanish
        elif(user['language'] == 'zh-tw'):
            zhtwCount += 1    ## Traditional Chinese
        elif(user['language'] == 'zh-cn'):
            zhcnCount += 1    ## Simplified Chinese
        elif(user['language'] == 'fr'):
            frCount += 1      ## French
        elif(user['language'] == 'it'):
            itCount += 1      ## Italian
        elif(user['language'] == 'he'):
            heCount+= 1       ## Hebrew
        elif(user['language'] == 'en-gb'):
            engbCount+=1
        elif(user['language'] == 'de'):
            deCount+=1        ## German

        count = count+1
    normal[10] = normalCount
    youtube[10] = youtubeCount
    journal[10] = journalCount
    celeb[10] = celebCount
    biz[10] = bizinfCount
    brand[10] = brandCount
    student[10] = studentCount
    total = [techCount, fashionCount, artCount, sportsCount,
             foodCount, polCount, bizCount, gamingCount, musicCount,unknownCount, count]
    both = [normal, youtube, journal, celeb, biz, brand, student, total]
    print(both)

    tweetmean = numpy.mean(tweetCount)
    followmean = numpy.mean(followCount)
    influencemean = numpy.mean(influenceCount)

    db_results[screenName].insert(
                    {
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "tech" : techCount,
                        "fashion" : fashionCount,
                        "art" : artCount,
                        "sports" : sportsCount,
                        "food" : foodCount,
                        "politics" : polCount,
                        "business" : bizCount,
                        "gaming" : gamingCount,
                        "music" : musicCount,
                        "unknown" : unknownCount,
                        "verified" : verifiedCount,
                        "en" : enCount,
                        "sp" : spCount,
                        "zh-tw" : zhtwCount,
                        "zh-cn" : zhcnCount,
                        "fr" : frCount,
                        "it" : itCount,
                        "he" : heCount,
                        "en-gb" : engbCount,
                        "de" : deCount,
                        "total" : count,
                        "casual_user" : normalCount,
                        "youtuber" : youtubeCount,
                        "writer" : journalCount,
                        "celebrity" : celebCount,
                        "business_expert" : bizinfCount,
                        "brand_corp" : brandCount,
                        "academic" : studentCount,
                        "both" : both,
                        "nobiodist" : nobiodist,
                        "techdist" : techdist,
                        "fashiondist" : fashiondist,
                        "gamingdist" : gamingdist,
                        "artdist" : artdist,
                        "sportsdist" : sportsdist,
                        "fooddist" : fooddist,
                        "poldist" : poldist,
                        "bizdist" : bizdist,
                        "musicdist" : musicdist,
                        "fulldist" : fulldist,
                        "tweetmean" : tweetmean,
                        "followmean" : followmean,
                        "influencemean" : influencemean*10

                    }
                    )
    print(fulldist)
    db_current.current.update(
                    { 'brand' : screenName },
                    { '$set' :
                        {
                        "time_stamp" : time.strftime("%m/%d/%Y"),
                        "tech" : techCount,
                        "fashion" : fashionCount,
                        "art" : artCount,
                        "sports" : sportsCount,
                        "food" : foodCount,
                        "politics" : polCount,
                        "business" : bizCount,
                        "gaming" : gamingCount,
                        "music" : musicCount,
                        "unknown" : unknownCount,
                        "verified" : verifiedCount,
                        "en" : enCount,
                        "sp" : spCount,
                        "zh-tw" : zhtwCount,
                        "zh-cn" : zhcnCount,
                        "fr" : frCount,
                        "it" : itCount,
                        "he" : heCount,
                        "en-gb" : engbCount,
                        "de" : deCount,
                        "total" : count,
                        "casual_user" : normalCount,
                        "youtuber" : youtubeCount,
                        "writer" : journalCount,
                        "celebrity" : celebCount,
                        "business_expert" : bizinfCount,
                        "brand_corp" : brandCount,
                        "academic" : studentCount,
                        "both" : both,
                        "nobiodist" : nobiodist,
                        "techdist" : techdist,
                        "fashiondist" : fashiondist,
                        "gamingdist" : gamingdist,
                        "artdist" : artdist,
                        "sportsdist" : sportsdist,
                        "fooddist" : fooddist,
                        "poldist" : poldist,
                        "bizdist" : bizdist,
                        "musicdist" : musicdist,
                        "fulldist" : fulldist,
                        "tweetmean" : tweetmean,
                        "followmean" : followmean,
                        "influencemean" : influencemean*10
                        }

                    },
                    upsert=True
                )



def distappend(distlist, user):
    indx = int(user['influenceScore'] * 10)
    distlist[indx][0] = distlist[indx][0] + 1
    distlist[indx][1].append(user['screen_name'])
    return distlist
