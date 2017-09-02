from random import randint
class User:
    def __init__(self, username, currency, enraged, defence):
        self.username = username
        self.currency = currency
        self.enraged = enraged
        self.defence = defence

class Chicken:
    def __init__(self, option,num):
        if option == "y":
            name = input("Name for chicken nr."+str(num) + ": ")
            self.name = name
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
