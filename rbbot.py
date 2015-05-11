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
#channel="##dkdelidj"
botnick="rebeccablack"
password="beckyyyyspass"

### TWEET INFO
urljs = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=officialjaden&count=200&include_rts=false"
urlrb = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=100&include_rts=false"
urlrb1 = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MsRebeccaBlack&count=1&include_rts=false"
key = 'key'
secret = 'sekrit'
ytkey = "yourytkey"
urlyt = "https://www.googleapis.com/youtube/v3/search?safeSearch=none&part=snippet&type=video&maxResults=1&key="+ytkey+"&q="

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
apiObject = rbbot.apis()

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
        if text.find(" crudeiasdas") != -1:
                bot.getNames(channel)
        elif text.find("!jaden") != -1 or text.find("JADEN") != -1:
                True
        elif text.find("jaden") != -1 or text.find("JADEN") != -1:
                try:
                        if cunt(text).lower() != "shoh":
                                #bot.messg(tweetjs,"t")
                                gif = apiObject.getAPI("sad")
                                bot.messg(gif,"a")
                except ValueError:
                        print("value error on cunt")
        if text.find("tell me more becky") != -1:
                if cunt(text).lower() != "shoh":
                        bot.messg(tweetrb,"t")
        if text.find("rebecca tell me stuff") != -1:
                if cunt(text).lower() != "shoh":
                        bot.messg(tweetrb1,"t")

        if text.find("IS IT FRIDAY") != -1:
                last_check=current
                allowance += time_passedS * (rate / per)
                if (allowance > rate):
                        allowance = rate;
                if (allowance < 1.0):
                        print "allowance under 1"
                else:
                        cunts = cunt(text).lower()
                        if cunts != "shoh" or cunts != "dong" or cunts != "dongerdong":
                                bot.messg(datetime.datetime.now(),"YT")
                        allowance -= 1.0

        if text.find(":.yt ") != -1 or text.find(":.YT ") != -1:
                last_check=current
                allowance += time_passedS * (rate / per)
                if (allowance > rate):
                        allowance = rate;
                if (allowance < 1.0):
                        print "allowance under 1"
                else:
                        cunts = cunt(text).lower()
                        if cunts == "shoh" or cunts == "dong" or cunts == "dongerdong" or cunts == "rebeccablack":
                                bot.messg("yer a cunt harry","g")
                        else:
                                line = text[text.index(":.yt"):].split()
                                searchterm = []
                                searchterm = "+".join(line[1:]).strip()
                                if searchterm:
                                        urlytube = urlyt+searchterm
                                        result = apiObject.getYT(urlytube)
                                        tellthecunts = result["items"][0]["snippet"]["title"]+" by "+result["items"][0]["snippet"]["channelTitle"]+" -> https://www.youtube.com/watch?v="+result["items"][0]["id"]["videoId"]
                                        bot.messg(tellthecunts,"g")
                                allowance -= 1.0

        if text.find("is it friday") != -1:
                last_check=current
                allowance += time_passedS * (rate / per)
                if (allowance > rate):
                        allowance = rate;
                if (allowance < 1.0):
                        print "allowance under 1"
                else:
                        cunts = cunt(text).lower()
                        if cunts == "shoh" or cunts == "dong" or cunts == "dongerdong":
                                bot.messg("yer a cunt harry","g")
                        else:
                                bot.messg(datetime.datetime.now(),"yt")

                        allowance -= 1.0
        if text.find ( 'PING' ) != -1:
                bot.messg(text.split()[1],"p")
