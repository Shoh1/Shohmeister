#!/usr/bin/python

from random import randint

class Bantsults(object):
        def __init__(self):
                self.test="test"

        def Bantjective(self):
                baj = [
                        "the arch bishop of Banterbury",
                        "Banton dubec",
                        "a Bantomime",
                        "a Bantlepiece",
                        "Bantony Hopkins",
                        "Banterberry tales",
                        "a Bantagonist",
                        "the Banti-christ",
                        "a Bantelope",
                        "a user of Banti aging cream",
                        "using Bantidote",
                        "living in a Bantasy",
                        "Bantastic",
                        "the Bantom of the opera",
                        "wearing Sweat bants",
                        "very Robantic" 
                ]
                rand = randint(1,len(baj)-1)
                return baj[rand]
