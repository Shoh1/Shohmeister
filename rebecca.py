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
cheekyrate = 1.0
cheekyper = 60.0
cheekyallowance = cheekyrate;
allowance = rate;
last_check=time.time()


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
        
        if text.find ( 'PING' ) != -1:
                if '#' not in text.lower():
                        bot.messg(text.split()[1],"p","")
        elif chan(text) == "#crude":
                if text.lower().find(":.bantz") != -1:
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
                elif text.lower().find("nandos") != -1:
                        last_check=current
                        cheekyallowance += time_passedS * (cheekyrate / cheekyper)
                        if (cheekyallowance > cheekyrate):
                                cheekyallowance = cheekyrate;
                        if (cheekyallowance < 1.0):
                                print "cheekyallowance under 1"
                        else:
                                cunts = cunt(text).lower()
                                if cunts == "r_l_n" or cunts == "sp00n" or cunts == "stulander":
                                        bot.messg(cunt(text) + ": fuck off you lemon and herb CUNT","g",chan(text))
                                else:
                                        bot.messg(cunt(text) + ": FANCY A CHEEKY NANDOS?? YEYEYEYEYEYEYEYYEYEYEYEYYEYEYEYEYEY EXTRA HOT ON MY DICK","g",chan(text))
                                cheekyallowance -= 1.0
        elif chan(text) == "#reddit-sysadmin":
                if text.lower().find("linux") != -1 and 'gnu/linux' not in text.lower():
                        last_check=current
                        allowance += time_passedS * (rate / per)
                        if (allowance > rate):
                                allowance = rate;
                        if (allowance < 1.0):
                                print "allowance under 1"
                        else:
                                rand = random.randint(1,2);
                                if rand == 1:
                                        bot.messg(cunt(text) + ": I think you mean GNU/Linux","g","#reddit-sysadmin")   
                                elif rand == 2: 
                                        bot.messg(cunt(text) + ": Linux is just OSx for virgins","g","#reddit-sysadmin")
                        allowance -= 1.0
                elif text.lower().find("unix") != -1:
                        last_check=current
                        allowance += time_passedS * (rate / per)
                        if (allowance > rate):
                                allowance = rate;
                        if (allowance < 1.0):
                                print "allowance under 1"
                        else:
                                bot.messg(cunt(text) + ": I think you mean OSx","g","#reddit-sysadmin")
                        allowance -= 1.0
                elif text.lower().find("osx") != -1:
                        last_check=current
                        allowance += time_passedS * (rate / per)
                        if (allowance > rate):
                                allowance = rate;
                        if (allowance < 1.0):
                                print "allowance under 1"
                        else:
                                bot.messg(cunt(text) + ": OSx is unix for people who get laid","g","#reddit-sysadmin")
                        allowance -= 1.0
