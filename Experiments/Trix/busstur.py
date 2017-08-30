
class Bus:
    def __init__(self, maxPassangers, currentPassangers, ditched):
        self.maxPassangers = int(maxPassangers)
        self.currentPassangers = int(currentPassangers)
        self.ditched = int(ditched)

    def action(self):
        action = input("The bus stopped. People getting on or off (on/off/show)?")
        amount = int(input("How many are we talking about?"))
        if action == "on":
            self.getOn(amount)
        elif action == "off":
            self.getOff(amount)
        elif action == "show":
            self.show()
        else:
            print("Error, please try again...\n")

    def getOn(self, amount):
        for i in range(0,int(amount)):
            if bus.currentPassangers < bus.maxPassangers:
                bus.currentPassangers += 1
                new = Passanger(bus.currentPassangers)
            else:
                bus.ditched += 1

    def getOff(self,amount):
        for i in range(0,int(amount)):
            if (self.currentPassangers - amount) >= 0:
                self.currentPassangers - amount
            else:
                print("Some shit hit the fan")
    def show(self):
        print("The bus has "+str(self.currentPassangers)+" passangers")
        print("And "+str(bus.ditched)+" are walking")


class Passanger:
    def __init__(self, id):
        self.id = id


bus = Bus(30,0,0)
driving = True
while driving:
    #Main loop
    input("Driving... Driving... Driving...\n")
    bus.action()
