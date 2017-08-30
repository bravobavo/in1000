import random
#DIFFERENT FACTORS INCLUDED
class Chicken:
    count = 0
    def __init__(self):
        Chicken.count += 1
        self.id = Chicken.count


class Fox:
    agility = 0
    wisdom = 0
    alertness = 0
    def __init__(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == 0:
            self.agility=random.randint(0,30)
            self.wisdom=random.randint(0,30)
            self.alertness=random.randint(0,30)
        elif self.difficulty == 1:
            self.agility=random.randint(0,50)
            self.wisdom=random.randint(0,30)
            self.alertness=random.randint(0,30)
        else:
            self.agility=random.randint(0,100)
            self.wisdom=random.randint(0,100)
            self.alertness=random.randint(0,100)


class User:
    def __init__(self, username, currency, enraged):
        self.username = username
        self.currency = currency
        self.enraged = enraged


#STAGES
class Day:
    nr = 0
    def __init__(self):
        #Preparation
        Day.nr += 1
        print("D A Y T I M E {0} o_o".format(self.nr))

    def choices(self):

        print("")


class Night:
    nr = 0
    def __init__(self, base):
        Night.nr += 1
        print("The sun goes down. {0} night pops up...\n".format(self.nr))
        input("And so does the fox")
        self.chickensRemaining = Chicken.count
        self.base = base
        self.id = Night.nrNight


class End():
    def __init__(self):
        print("RESULT")


#Intro
input("Far, far, far...\nIn the woods of a farmer...\n"+
      "A sly fox lurks from underneath the many trees...")
input("Ready to kill!")
print("Your goal is to stop the fox from killing all your precious chickens...")
help = input("Are you ready?\n\"help\" ==> some tips and advise")
if help == "h" or help =="help":
    with open("help.txt","r") as helpTxt:
        lines = helpTxt.readlines()
        i = 0
        while i < len(lines):
            print(lines[i].rstrip("\n"))
            i += 1

difficulty = input('Difficulty?\n{0:14}==>{1:5}\n{2:14}==>{3:5}\n{4:14}==>{5:5}'
.format("F.N.G",0,"S.S.D.D",1,"Juggernaut!",2))
if difficulty == 0:
    user.currency = 10000
elif difficulty == 1:
    user.currency = 1000
elif difficulty == 2:
    user.difficulty = 100
else:
    input("Write 0,1 or 2 depending on preferred difficulty")
    surviving = False
for i in range(0,10):
    r = random.random()*10
    Chicken()
fox = Fox(difficulty)
username = input("You are a farmer. But, what is your name?\n")
user = User(username,0,0)


###   THE FLOW OF THE GAME   ###
surviving = True
while surviving:
    for i in range(0,15):
        Day()
        Night()
    End()
    surviving = False
