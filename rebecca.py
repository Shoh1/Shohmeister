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


def cunt(text):
        t = text.split()
        t1=t[0]
        to = t1[1:t1.index('!')].strip()
        return to


### START
while bot.connected == True:
        signal.signal(signal.SIGINT, bot.exitGracefully)
        current = time.time()

        text=bot.ircsock.recv(2048)
        print (text)
        
        if text.find(":.bantz") != -1 or text.find(":.BANTZ") != -1:
                cunts = cunt(text).lower()
                if cunts != "doctordalek"
                                bot.messg(cunt(text),"c")
                else:
                                bot.messg("Ur a virgin","g")

        if text.find ( 'PING' ) != -1:
                bot.messg(text.split()[1],"p")
