#!/usr/bin/python
# -*- coding: utf-8 -*-

import rbbot
from pprint import pprint
import datetime
import signal
import time

### IRC INFO
server = "irc.freenode.net"
port = 6697
bot = rbbot.RBbot(server,port)
channel="#crude"
channel2="#reddit-sysadmin"
botnick="rebeccablack"
password="password"

### TWEET INFO
urljs = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=officialjaden&count=200&include_rts=false"
urlrb = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=100&include_rts=false"
urlrb1 = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=1&include_rts=false"
key = 'twitterkey'
secret = 'twittersecret'

### SET NICK AND JOIN CHANNEL
bot.set_nick(botnick,password)
bot.join(channel)
#bot.join(channel2)

### GET THE TWEET
tweetObject = rbbot.Tweets()
tweetrb = tweetObject.getTweet(urlrb,key,secret)
tweetrb1 = tweetObject.getTweet(urlrb1,key,secret)
tweetjs = tweetObject.getTweet(urljs,key,secret)


### RATE LIMITING
rate = 1.0
per = 5.0
allowance = rate;
last_check=time.time()
tweet_check = time.time()

def cunt(text):
        t = text.split()
        t1=t[0]
        to = t1[1:t1.index('!')].strip()
        return to


### START
while bot.connected == True:
        signal.signal(signal.SIGINT, bot.exitGracefully)
        current = time.time()
        time_passed = current - tweet_check
        time_passedS = current - last_check
        if (time_passed > 14400):
                tweet_check = current
                tweetrb = tweetObject.getTweet(urlrb,key,secret)
                tweetjs = tweetObject.getTweet(urljs,key,secret)

        text=bot.ircsock.recv(2048)
        print (text)
        if text.find(" crude") != -1:
                bot.getNames(channel)
        elif text.find("!jaden") != -1 or text.find("JADEN") != -1:
                True
        elif text.find("jaden") != -1 or text.find("JADEN") != -1:
                if cunt(text).lower() != "Shoh":
                        bot.messg(tweetjs,"t")

        if text.find("tell me more becky") != -1:
                if cunt(text).lower() != "Shoh":
                        bot.messg(tweetrb,"t")
        if text.find("rebecca tell me stuff") != -1:
                if cunt(text).lower() != "Shoh":
                        bot.messg(tweetrb1,"t")

        if text.find("IS IT FRIDAY") != -1:
                last_check=current
                allowance += time_passedS * (rate / per)
                if (allowance > rate):
                        allowance = rate;
                if (allowance < 1.0):
                        print "allowance under 1"
                else:
                        if cunt(text).lower() != "Shoh":
                                bot.messg(datetime.datetime.now(),"YT")
                        allowance -= 1.0

        if text.find("is it friday") != -1:
                last_check=current
                allowance += time_passedS * (rate / per)
                if (allowance > rate):
                        allowance = rate;
                if (allowance < 1.0):
                        print "allowance under 1"
                else:
                        if cunt(text).lower() != "Shoh":
                                bot.messg(datetime.datetime.now(),"yt")
                        else:
                                bot.messg("yer a cunt harry","g")

                        allowance -= 1.0
        if text.find ( 'PING' ) != -1:
                bot.messg(text.split()[1],"p")
