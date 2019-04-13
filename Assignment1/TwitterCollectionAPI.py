# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:13:26 2018

@author: Yigao
"""

import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys

## Twitter API keys and secrets (API key hide on purpose
consumer_key = '*************************'
consumer_secret = '**************************************************'
access_token = '**************************************************'
access_secret = '********************************************'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

## Twitter listener
class Listener(StreamListener):
    print("In Listener...") 
    tweet_number=0
    #__init__ runs as soon as an instance of the class is created
    def __init__(self, max_tweets, hfilename, rawfile):
        self.max_tweets=max_tweets
        print(self.max_tweets)     
    #on_data() is a function of StreamListener as is on_error and on_status    
    def on_data(self, data):
        self.tweet_number+=1 
        print("In on_data", self.tweet_number)
        try:
            print("In on_data in try")
            with open(hfilename, 'a') as f:
                with open(rawfile, 'a') as g:
                    tweet=json.loads(data)
                    tweet_text=tweet["text"]
                    print(tweet_text,"\n")
                    f.write(tweet_text) # the text from the tweet
                    json.dump(tweet, g)  #write the raw tweet
        except BaseException:
            print("NOPE")
            pass
        if self.tweet_number>=self.max_tweets:
            sys.exit('Limit of '+str(self.max_tweets)+' tweets reached.')
    #method for on_error()
    def on_error(self, status):
        print("ERROR")
        if(status==420):
            print("Error ", status, "rate limited")
            return False

## ask user to enter query
hashname=input("Enter the hash name, such as #womensrights: ") 
numtweets=eval(input("How many tweets do you want to get?: "))
if(hashname[0]=="#"):
    nohashname=hashname[1:] #remove the hash
else:
    nohashname=hashname
    hashname="#"+hashname

## Create a file for any hash mine    
#hfilename="file_"+nohashname+".txt"
#rawfile="file_rawtweets_"+nohashname+".txt"
hfilename="file.txt"
rawfile="file_rawtweets.txt"
twitter_stream = Stream(auth, Listener(numtweets, hfilename, rawfile))
#twitter_stream.filter(track=['#womensrights'])
twitter_stream.filter(languages = ["en"], track=[hashname])
