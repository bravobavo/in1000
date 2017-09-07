# XXX: This is my first project using Python. Only a prototype. Not even alpha.
# TODO: Dog (strongest item)
# BUG: The killing at night because of list

###   THE GAME MODULES   ###
from random import randint as r
from factors import *
from events import *

###   SETUP   ###
nickname = input("You are a farmer, nicknamed ")
user = User(nickname,500,0,200)#nickname,money,enraged,defence
foxes = [Fox() for x in range(0,3)]
naming = input("You wish to name your chickens, "+user.nickname+"? (y/n/u) = ")
chickens = [Chicken(naming,num) for num, i in enumerate(range(10), 0)]
items = [Item('scarecrow',100, 200,"none"),#name, cost, defence, special
         Item('shout',0,100,"none"),
         Item('stereo',1,5,"none"),
         Item('corn',50,0,"yes"),
         Item('drugs',5000,0,"yes"),
         Item('gun',1000,250,"yes")]

game = Game(user,foxes,chickens,items)

###   THE FLOW OF THE GAME   ###
surviving = True
while surviving:
    for i in range(0,15):
        game.dayTime()
        game.nightTime()
