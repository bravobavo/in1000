### FUNCTIONS ###
from random import randint, uniform
import time
from factors import Item
import helpMe
class Game:
    def __init__(self, user, foxes, chickens, items):
        self.eMagnitude = 0
        self.dayNr = 0
        self.nightNr = 0
        self.user = user
        self.foxes = foxes
        self.chickens = chickens
        self.items = items
        self.stash = []

### CHECKERS ###
    ### EGGS AND CHICKS ###
    eggs = 0
    def newEggs(self):
        eggs = 0
        for i in range (len(self.chickens)):
            egg = randint(0,1)
            eggs += egg
        self.eggs += eggs

    def eggPay(self):
        payment = self.eggs*5*self.eMagnitude
        print('You receive {}$'.format(payment))
        self.user.currency += payment

    def newChicken(self):
        if self.eggs > 10 and self.eMagnitude > 2.2:
            self.chickens.append(Chicken("y",1))
        else:
            print("\nNo chicken born today")

    ### ATTACK AND DEFENCE ###
    foxesAttackTotal=0
    def foxesAttack(self):
        foxesAttack = 0
        for i in self.foxes:
            foxesAttack += i.agility + i.wisdom + i.alertness
            self.foxesAttackTotal = foxesAttack

    totalDefence = 0
    def calcDefence(self, u):
        constant = self.user.defence
        protection = 0
        for i in self.stash:
            protection += i.defence
        self.totalDefence = protection + constant + (u.enraged*10)

### OPTIONS ###
    ### HELP ###
    def help(self, where):
        print('\nH O M E - H E L P')
        if where == 'home':
            helpMe.home()
        elif where == 'stats':
            pass
        elif where == 'market':
            pass



    ### STATS ###
    def stats(self, user, eggs, chickens, stash):
        print('\nS T A T S\n'+
              'Currency: '+str(user.currency)+'$\n'+
              'Constant defence: '+str(user.defence)+'¤\n'+
              'Current defence: '+str(self.totalDefence)+'¤\n'+
              'Enraged bonus: '+str(user.enraged)+' >:(')
        print('Collected eggs: '+str(eggs)+
              '\nAs of today: {0:.2f}$ per egg'.format(5*self.eMagnitude))
        print('\nChicken roaster:')
        for i in chickens:
            print('> '+i.name)
        print('\nYour stash:')
        for i in stash:
            print('> {} = {}¤ (special={})'.format(i.name,i.defence,i.special))

    ### MARKET ###
    def buy(self, item, u):
        if item.price <= u.currency:
            agreement = input('{} buys {}? (y/n)\n'.format(u.nickname, item.name))
            if agreement == "y":
                print('Buying and adding '+item.name+' to your stash...')
                time.sleep(1.5)
                u.currency -= item.price
                self.stash.append(item)
                self.calcDefence(self.user)
            else:
                print("Cancelling transaction...")
        else:
            print('You don\'t have enough money...'+
                  'Item: {}$\nYou have: {}'.format(item.price, u.currency))

    def market (self, u, i, e):
        shopping = True
        while shopping:
            print('\nM A R K E T')
            time.sleep(0.5)
            category = input(' buy | sell | help | leave\n>>>')

            if category == 'buy':
                print('\nM A R K E T - B U Y')
                for x in i:
                    print('> {} = {}$, {}¤'.format(x.name,x.price,x.defence))
                itemChoice = input("You choose to buy: ")
                if itemChoice == "scarecrow":
                    self.buy(i[0], u)
                elif itemChoice == "shout":
                    self.buy(i[1], u)
                elif itemChoice == "stereo":
                    self.buy(i[2], u)
                elif itemChoice == "corn":
                    self.buy(i[3], u)
                elif itemChoice == "drugs":
                    self.buy(i[4], u)
                elif itemChoice == "gun":
                    self.buy(items[5], u)
                else:
                    print(itemChoice+' is not a valid option')

            elif category == 'sell':
                print('\nM A R K E T - S E L L')
                payment = round(e*5*self.eMagnitude,2)
                answer = input('Sell your {} eggs ({}$)?'.format(e,payment))
                if answer == 'y':
                    self.eggPay()
                else:
                    print("You refused to sell your eggs")

            elif category == "help":
                self.help('market')

            elif category == 'leave':
                print('Returning home...')
                shopping = False
    line = 0
### STAGES ###
    ### DAYTIME ###
    def dayTime(self):
        self.eMagnitude = round(uniform(0.5, 2.2),2) + self.line
        self.dayNr += 1
        self.foxesAttack()
        self.newEggs()
        self.newChicken()
        self.calcDefence(self.user)
        print('''\n\n---------->  {}. Day  <----------'''.format(self.dayNr))
        awake = True
        while awake:
            print('\nH O M E')
            time.sleep(0.5)
            option = input(' help | stats | market | sleep\n>>> ')
            if option == 'help':
                self.help('home')
            elif option == 'stats':
                self.stats(self.user, self.eggs, self.chickens, self.stash)
            elif option == 'market':
                self.market(self.user, self.items, self.eggs)
            elif option == 'sleep':
                awake = False
            else:
                print('Thats not a valid option')

    ### NIGHTITME ###
    def nightTime(self):
        victims = []
        self.nightNr += 1
        self.calcDefence(self.user)
        print('''\n\n---------->  {}. Night  <----------'''.format(self.nightNr))
        for item in self.stash:
            if item.special == 'yes':
                if(item.name == "corn"):
                    self.line += 1
                elif(item.name == "gun"):
                    for i in self.foxes:
                        if i.attention < 20:
                            print("You killed a fox that wasn't paying attention!")
                            pop(i)
                        else:
                            print("The foxes saw you and went into hiding...")

        trouble = True
        while trouble:
            if self.dayNr >= 15:
                self.end()
            killX = randint(1,len(self.chickens)-1)
            print(self.chickens[killX].name+' is in danger!')
            time.sleep(1.5)
            if self.totalDefence < self.foxesAttackTotal:
                lucky = randint(0,10)
                if lucky < 9:
                    victims.append(self.chickens[killX].name)
                    self.chickens.pop(killX)
                    self.foxesAttackTotal -= 100
                else:
                    print(self.chickens[killX].name+' got away!')
            else:
                print("Out of the dark, the sun rises. And the foxes retreat")
                trouble = False
            self.stash = []
        print('\nV I C T I M S')
        for i in victims:
            print(i)
        self.user.enraged += len(victims)

    ### ENDING ###
    def end(self):
        print('You survived!')
