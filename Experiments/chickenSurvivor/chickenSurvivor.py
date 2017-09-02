###   THE GAME MODULES   ###
from random import randint as r
from factors import *
from stages import *

###   SETUP   ###
username = input("What is your name, farmer?\n")
user = User(username,0,0)
foxes = [Fox() for x in range(0,3)]
naming = "You wish to name your chickens, "+user.username+"? (y/n)\n "
chickens = [Chicken(naming) for num, i in enumerate(range(10), 1)]

###   THE FLOW OF THE GAME   ###
surviving = True
while surviving:
    dayNr = 0
    nightNr = 0
    for i in range(0,15):
        Day()
        Night()
    End()
    surviving = False
