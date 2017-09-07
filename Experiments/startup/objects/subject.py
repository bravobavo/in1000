class Population:
    def __init__(self):
        self.humans = []
        self.animals = []
        self.totalPopulation = 0

    def addSpecies(self):
        # QUESTION:
        print("Yohooo")

    def log(self):
        newPop = input("What population is this?")
        with open("data.txt", "a") as myFile:
            myFile.write(newPop + "\nHUMANS:")
            for i in self.humans:
                myFile.write(i.name)

    def getLog(self):
        text_file = open("data.txt","r")
        lines = text_file.readlines()
        text_file.close()
        i = 0
        while i < len(lines):
            print(lines[i])
            i += 1

class Species:
    def __init__(self, species, name):
        self.name = name
        if species == "animals":
            firstPopulation.animals.append(self)
        elif species == "humans":
            firstPopulation.humans.append(self)
        firstPopulation.totalPopulation += 1

    def show (self):
        print("Er en hund")
#INPUT
firstPopulation = Population()
dog = Species("animals", "Bobo")
dog1 = Species("animals", "Boasdbo")
dog2 = Species("animals", "Bsobo")
dog3 = Species("animals", "Bosadbo")
dog4 = Species("animals", "Bsaobo")
human1 = Species("humans", "obo")
human2 = Species("humans", "asdaobo")
human3 = Species("humans", "wobo")

dog.show()
firstPopulation.log()
firstPopulation.getLog()

class Transport:
    count = 0
    def __init__(self, transportType, maxSpeed):
        Transport.count += 1
        self.count = Transport.count
        self.transportType = transportType
        self.maxSpeed = maxSpeed

    def showSpeed(self):
        print("My speed is: "+ self.maxSpeed)

vehicle = Transport("car", "90km" )
vehicle.showSpeed ()
print(Transport.count)
