### FUNCTIONS ###
from random import randint as r
class Stage:
    def __init__(self, user, foxes, chickens):
        self.dayNr = 0
        self.nightNr = 0
        self.user = user
        self.foxes = foxes
        self.chickens = chickens

    ### EGGS ###
    eggsTotal = 0
    def produceEggs(self):
        eggs = 0
        for i in range (len(self.chickens)):
            egg = r(0,1)
            eggs += egg
            self.eggsTotal = eggs*5

    def balance(self, userBalance, eggsBalance):
        print("$$$ BALANCE $$$")
        print("You currently have "+str(userBalance)+"$")
        print(str(eggsBalance)+"$ for your eggs waiting to be collected.")

    def eggPayment(self):
        if collectDay == day:
            eggs = 0
            for i in range (len(self.chickens)):
                egg = r(0,1)
                eggs += egg
                return eggs

    ### BATTLE ###

    ### ATTACK ###
    #Everyday, amount of foxes and their combined attack is calculated
    foxesAttackTotal=0
    def foxesAttack(self):
        foxesAttack = 0
        for i in self.foxes:
            foxesAttack += i.agility + i.wisdom + i.alertness
        self.foxesAttackTotal = foxesAttack

    ### DEFENCE ###
    # QUESTION: CHECK IF WORKS
    tricks = []
    def defenceTotal(self):
        totalDefence = 0
        constant = self.user.defence
        protection = 0
        for i in tricks:
            protection += i.protection
        totalDefence += protection + constant

    ### SHOP ###
    def buy(self, item, price):
        pass

    shop = {"scare":[],
            "special":["dog"]
            }

    def shop (self):
        shopping = True
        print("Beyond many woods, you arrive at the local shop...")
        print("$$$ SHOP $$$")
        while shopping:
            category = input("scare | special | leave\n>>> ")
            if category == "scare":
                print(category.upper())
                subCategory = input("scarecrow 50$ | shout 0$ | stereo run outside $1")
                if subCategory == ("scarecrow" or "shout" or "stereo"):
                    buy(subCategory)
                else:
                    print("returning to shop...")
            elif category == "special":
                subCategory = input("drugs 5000$ | gun 1000$\n>>> ")
                if subCategory == ("drugs" or "gun"):
                    buy(subCategory)
                else:
                    print("returning to shop...")
            elif category == "leave":
                shopping = False
            else:
                print("loooolz")


    ### STAGES ###
    dayHelp = {'help':'Prints out a help.txt-file',
               'balance':'Current money and money waiting',
               'shop':'Go to the shop'
               }
    def dayTime(self):
        self.dayNr += 1
        self.foxesAttack()
        self.produceEggs()
        print('''\n---->    {0}. Day    <----'''.format(self.dayNr))
        awake = True
        while awake:
            option = input("\nhelp | balance | shop\n>>> ")
            #option = input("Waiting for input... (press \"help\" for help)\n")
            if option == "help":
                print('\n### HELP ###')
                for command, description in self.dayHelp.items():
                    print('{0:10} ==> {1:10}'.format(command, description))
            elif option == "balance":
                self.balance(self.user.currency,self.eggsTotal)
            elif option == "shop":
                self.shop()
            elif option == "x":
                awake = False
            else:
                print("Thats not a valid option")

    nightHelp = {'Info':'info'}
    def nightTime(self):
        self.nightNr += 1
        print('''---->    {}. Night    <----'''.format(self.nightNr))
        print(self.user.currency)


    def end(self):
        pass
