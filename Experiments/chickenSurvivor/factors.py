from random import randint
class User:
    def __init__(self, nickname, currency, enraged, defence):
        self.nickname = nickname
        self.currency = currency
        self.enraged = enraged
        self.defence = defence

class Chicken:
    def __init__(self, option,num):
        if option == "y":
            name = input("Name for chicken nr."+str(num) + ": ")
            self.name = name
        elif option == "u":
            with open("survivors.txt","r") as survivors:
                lines = survivors.readlines()
                self.name = lines[num].rstrip("\n")
        else:
            self.name = "chicken"+str(num)

class Fox:
    agility = 0
    wisdom = 0
    alertness = 0
    def __init__(self):
        self.agility=randint(0,100)
        self.wisdom=randint(0,100)
        self.alertness=randint(0,100)


class Item:
    def __init__(self,name,price,defence,special):
        self.name = name
        self.price = price
        self.defence = defence
        self.special = special
