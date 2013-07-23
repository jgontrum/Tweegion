# Twython.
# by Tatjana Scheffler
# A simple example script for corpus collection from Twitter using Tweepy https://github.com/tweepy

# March 18, 2013: Now less breakable by Latin-1 encoded strings.

import sys
import tweepy
import csv
import codecs
import simplejson as json

import time
from datetime import date

from tweepy.models import Status


consumer_key = "dahaJwslsqJzI83H8UtyAA"
consumer_secret = "mUCXVm5yEU2wDzXDhRmyGOLjAuP23NAHL9PqDe29U"
access_key = "1360250492-ISxQgV7JJ7tg43ZxjkIMmnNI414NU8VnMuJjd7b"
access_secret = "9a7MjqqA8wRhCoeMRmEajBWi05TCTa1J6SjanGnKY"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# open log file
logfile = open('twython.log', 'a')

class CustomStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        global old_date
        global writer
        global outfile
        new_date = date.today()
        if not new_date == old_date:
            outfile.close
            outfile = codecs.open("tweets-" + str(new_date) + ".txt", "ab", "utf-8")
            old_date = new_date
	try:
            text = ""
            try:
                status = Status.parse(self.api, json.loads(data))
                text = status.text
            except UnicodeDecodeError, ude:
                logfile.write(str(time.asctime( time.localtime(time.time()) )) + ' Encountered unicode decode error, trying latin-1 ' + "\n")
                status = Status.parse(self.api, json.loads(data,"latin-1"))
                text = status.text
            if status.user.lang == "de": 
                outfile.write( data + "\n" )
	except Exception, e:
            # Catch any unicode errors while printing to console                
            # and just ignore them to avoid breaking application.
            logfile.write(str(time.asctime( time.localtime(time.time()) )) + ' Caught exception: ' + str(e) + "\n" )
            sys.exc_clear()
#                pass                                                           
        return True


    def on_error(self, status_code):
        logfile.write(str(time.asctime( time.localtime(time.time()) )) + ' Encountered error with status code:' + str(status_code) + "\n")
        return True # Don't kill the stream

    def on_timeout(self):
        logfile.write(str(time.asctime( time.localtime(time.time()) )) + ' Timeout...' + "\n")
        return True # Don't kill the stream





localtime = time.asctime( time.localtime(time.time()) )
logfile.write( localtime + " Tracking terms from ../twython-keywords.txt\nStarting stream \n")

stream = tweepy.streaming.Stream(auth, CustomStreamListener())

terms = [line.strip().lower() for line in open('twython-keywords.txt', "r")]

# open output file
old_date = date.today()
outfile = codecs.open ("tweets-" + str(old_date) + ".txt", "ab", "utf-8")
writer = csv.writer(outfile,quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
 

stream.filter(track=terms)
