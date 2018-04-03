import tweepy

class twitUser(tweepy.models.User):
    def __init__(self, theUser, userlabel):
        self.label = userlabel
        self.user=theUser


    
    