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

        def messg(self,content,mode):
                self.mode = mode
                self.content = content
                self.bantsult = bantsults.Bantsults()


                if self.mode == 'c':
                        self.ircsock.send("PRIVMSG "+self.chan+" :"+ self.content + " is " + self.bantsult.Bantjective() + "\r\n")
                elif self.mode == 'p':
                        self.ircsock.send( 'PONG ' + self.content + '\r\n' )
                elif self.mode == 'g':
                        self.ircsock.send("PRIVMSG "+self.chan+" :"+self.content.encode('utf8')+"\r\n")


class Tweets(object):
        def __init__(self):
                self.http_method = "GET"
                self.post_body = ""
                self.http_headers= None

        def oauth_req(self,url, key, secret):
                self.url = url
                self.key = key
                self.secret = secret
                self.consumer = oauth.Consumer(key=self.key, secret=self.secret)
                #token = oauth.Token(key=key, secret=secret)
                self.client = oauth.Client(self.consumer)
                self.resp, self.content = self.client.request( self.url, method=self.http_method, body=self.post_body,headers=self.http_headers)
                return self.content

        def getTweet(self,url,key,secret):
                self.url = url
                self.key = key
                self.secret = secret
                self.jstweet = self.oauth_req(self.url,self.key,self.secret)
                self.parsed = json.loads(self.jstweet)
                return self.parsed

class apis(object):
        def __init__(self):
                self.term = ""
        #replygif api
        def getAPI(self,term):
                self.url = "http://replygif.net/api/gifs?tag="+term+"&api-key=39YAprx5Yi"
                self.req = urllib2.Request(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.18 Safari/537.36'})
                self.parsed = json.load(urllib2.urlopen(self.req))
                return self.parsed
        #youtube api
        def getYT(self,url):
                self.url = url
                self.req = urllib2.Request(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.18 Safari/537.36'})
                self.parsed = json.load(urllib2.urlopen(self.req))
                return self.parsed
