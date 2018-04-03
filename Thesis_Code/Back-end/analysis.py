from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer
from pymongo import MongoClient
import classifyUserDem
import influenceClassify


#function calssifies followers as journalists or not
def analyze_user(brand_handle):
    client = MongoClient()
    db_users = client.users_db

    cursor = db_users.users.find({"brands" : brand_handle}) # Get all users following the brand
    count = 1
    for document in cursor:
        categories = classifyUserDem.classify(client, document)
        influences = influenceClassify.classify(client, document)
        if (count % 1000 == 0):
            print("Classification for user " + str(count))            
        count = count + 1