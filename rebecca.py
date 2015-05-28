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
botnick="Shohmeister"
password=""

### RATE LIMITING
rate = 1.0
per = 5.0
allowance = rate;
last_check=time.time()
apiObject = rbbot.apis()


### SET NICK AND JOIN CHANNEL
bot.set_nick(botnick,password)
bot.join(channel)
bot.join(channel2)


def cunt(text):
        t = text.split()
        t1=t[0]
        to = t1[1:t1.index('!')].strip()
        return to
        
def chan(text):
        t = text.split()
        return t[2]



### START
while bot.connected == True:
        signal.signal(signal.SIGINT, bot.exitGracefully)
        current = time.time()
        time_passedS = current - last_check

        text=bot.ircsock.recv(2048)
        print (text)
        
        if chan(text) == "#crude":
                if text.find(":.bantz") != -1 or text.find(":.BANTZ") != -1:
                        last_check=current
                        allowance += time_passedS * (rate / per)
                        if (allowance > rate):
                                allowance = rate;
                        if (allowance < 1.0):
                                print "allowance under 1"
                        else:
                                cunts = cunt(text).lower()
                                if cunts != "doctordalek":
                                                bot.messg(cunt(text),"c","#crude")
                                else:
                                                bot.messg("Ur a virgin","g","#crude")
                                allowance -= 1.0
        elif chan(text) == "#reddit-sysadmin":
                if text.find("linux") != -1 or text.find("LINUX") != -1:
                        last_check=current
                        allowance += time_passedS * (rate / per)
                        if (allowance > rate):
                                allowance = rate;
                        if (allowance < 1.0):
                                print "allowance under 1"
                        else:
                                bot.messg(cunt(text)" I think you meant GNU/Linux","g","#reddit-sysadmin")
                        allowance -= 1.0


        if text.find ( 'PING' ) != -1:
                bot.messg(text.split()[1],"p","")
