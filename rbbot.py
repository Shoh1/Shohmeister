#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
import socket
import ssl
import oauth2 as oauth
import time
import json
import bantsults
import urllib2
from random import randint

class RBbot(object):
        def __init__(self,server,port):
                self.server = server
                self.port = port
                self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.irc.connect((server,port))
                self.ircsock = ssl.wrap_socket(self.irc)

        def set_nick(self,nick,pwd):
                self.nick = nick
                self.pwd = pwd
                self.ircsock.send("USER "+self.nick+" "+self.nick+" "+self.nick+" :Yourmother\n")
                self.ircsock.send("NICK "+self.nick+"\n")
                self.ircsock.send("PRIVMSG NICKSERV :IDENTIFY " + self.nick + " " + self.pwd +"\n")

        def join(self,chan):
                self.chan = chan
                self.ircsock.send("JOIN "+self.chan+"\n")
                self.connected = True

        def getNames(self,chan):
                self.chan = chan
                self.ircsock.send("NAMES "+self.chan+"\n")

        def exitGracefully(self,signal,frame):
                self.ircsock.send("PART "+self.chan+" :west coast nigga\r\n")
                sys.exit(0)

        def chunks(self,l,n):
                self.l = l
                self.n = n
                for i in xrange(0,len(self.l),self.n):
                        yield self.l[i:i+self.n]

        def messg(self,content,mode,target):
                self.mode = mode
                self.content = content
                self.bantsult = bantsults.Bantsults()
                self.target = target


                if self.mode == 'c':
                        self.ircsock.send("PRIVMSG "+self.target+" :"+ self.content + " is " + self.bantsult.Bantjective() + "\r\n")
                elif self.mode == 'p':
                        self.ircsock.send( 'PONG ' + self.chan+ '\r\n' )
                elif self.mode == 'g':
                        self.ircsock.send("PRIVMSG "+self.target+" :"+self.content.encode('utf8')+"\r\n")
