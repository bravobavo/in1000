from random import randint
class User:
    def __init__(self, username, currency, enraged):
        self.username = username
        self.currency = currency
        self.enraged = enraged

class Chicken:
    def __init__(self, option):
        if option == "y":
            name = input("Name for chicken nr."+num)
            self.name = name
        elif option == "n":
            self.name = "chicken"+str(num)
        else:
            surviving = False

    def produceEggs(self):
        eggs = 0
        for i in range (self.chickenList):
            egg = r(0,1)
        return eggs


class Fox:
    agility = 0
    wisdom = 0
    alertness = 0
    def __init__(self):
        self.agility=randint(0,100)
        self.wisdom=randint(0,100)
        self.alertness=randint(0,100)
