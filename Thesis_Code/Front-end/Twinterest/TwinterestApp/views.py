from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import pymongo 
from pymongo import MongoClient
import json
from . import accessMongo


# Create your views here.
def load(request):
    print("load menu")
    array = accessMongo.getBrands()
    return HttpResponse(
        json.dumps(array),
        content_type="application/json"
    )

def index(request):
    #interests = ['Tech','Sports','Art','Food','Politics','Business','Unknown','Gaming','Fashion','Music']
    interests = ['Technology & Science','Sports & Fitness','Arts & Culture','Food & Drink','News & Politics','Business & Finance','Unknown','Gaming','Fashion & Beauty','Music']
    professions = ['Casual User','Youtubers','Writer or Journalist','Celebrity','Business Expert', 'Brand or Corporation', 'Academic']
    brand = ""
    if(request.GET.get('dropdown')):
        print("dropdown detected")
        brand = request.GET.get('dropdown')
        global current_brand 
        current_brand = brand
    
    if (brand == ""):
        pcts = [0,0,0,0,0,0,0,0,0,0]
    #return pcts
	#jsonDoc = json.dumps(pcts)
    categoriesPcts = accessMongo.getCategoriesPcts(brand)
    professionPcts = accessMongo.getProfessionPcts(brand)
    totalCount = accessMongo.getTotal(brand)
    influ = accessMongo.getBoth(brand)
    getdists = accessMongo.getDis(brand)
    
    catCount = json.dumps(categoriesPcts)
    profCount = json.dumps(professionPcts)
    influencerCount = json.dumps(influ)
    dists = json.dumps(getdists)
    catDoc = []
    profDoc=[]
    unknownDoc=[]
    
    for item in zip(categoriesPcts,interests):
        print(item[0])
        if (item[1] != 'Unknown'):
            catDoc.append(item)
        else:
            unknownDoc.append(item)
    for item in zip(professions,professionPcts):
        profDoc.append(item)

    catDoc.sort()

    print(catDoc)
    interCount = json.dumps(catDoc)
    unknownCount = json.dumps(unknownDoc)
    profChecker = json.dumps(profDoc)
    total = json.dumps(totalCount)
    print(interCount)
    print(unknownCount)

    total_count = accessMongo.total_count(brand)
    verified_count = accessMongo.verified_count(brand)
    tweets_count = accessMongo.tweets_count(brand)
    follower_count = accessMongo.follower_count(brand)
    influence_score_count = accessMongo.influence_score_count(brand)

    if brand == "":
        site_url = 'TwinterestApp/home_page.html'
    else:
        site_url = 'TwinterestApp/blocks.html'
   
    return render(request, site_url, {'influCount':influencerCount,'categoriesPcts':catCount, 'professionPcts':profCount, 
        'professionsChecker':profChecker, 'total':total, 'total_count':total_count, 'verified_count':verified_count, 'interCount':interCount,
        'tweets_count':tweets_count, 'follower_count':follower_count, 'influence_score_count':influence_score_count, 'getdists': dists, 'unknownCount':unknownCount})

def get_usernames(request):
    if request.method == 'GET':
        num = request.GET.get('number')
        interest = request.GET.get('interest')
        profession = request.GET.get('profession')
        #brand = request.GET.get('brand')
        brand =  current_brand
        #brand = request.GET.get('dropdown')
        array = accessMongo.getUsernames(brand=brand, num=num, interest=interest, profession=profession)
        return HttpResponse(
            json.dumps(array),
            content_type="application/json"
        )

def flag(request):
    if request.method == 'GET':
        username = request.GET.get('name')
        accessMongo.flagUser(username)
        return HttpResponse(username)

def report(request):
    if request.method == 'GET':
        username = request.GET.get('name')
        interest = request.GET.get('interest')
        influence = request.GET.get('profession')
        print("working????")
        accessMongo.report(username=username, interest=interest, influence=influence)
        return HttpResponse("Your feedback has been saved!")

def color(request):
    if request.method =='GET':
        brand = current_brand
        return HttpResponse(brand) 

