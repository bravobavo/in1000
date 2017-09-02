###   THE GAME MODULES   ###
from random import randint as r
from factors import *
from events import *

###   SETUP   ###
username = input("What is your name, farmer?\n")
user = User(username,1000,0,250)#username,money,enraged,defence
foxes = [Fox() for x in range(0,3)]
naming = input("You wish to name your chickens, "+user.username+"? (y/n) = ")
chickens = [Chicken(naming,num) for num, i in enumerate(range(10), 1)]
stage = Stage(user,foxes,chickens)

###   THE FLOW OF THE GAME   ###
surviving = True
while surviving:
    for i in range(0,15):
        stage.dayTime()
        stage.nightTime()
