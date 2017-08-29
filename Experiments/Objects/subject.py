class Population:
    def __init__(self):
        self.humans = []
        self.animals = []
        self.totalPopulation = 0

    def log(self):
        newPop = input("What population is this?")
        with open ("data.txt", "a") as myFile:
            myFile.write(newPop + "\nHUMANS:")
            i=0
            while i < len(self.humans):
                myFile.write(str(self.humans[i]))
        #with open("data2.txt", "a") as myfile:
        #myfile.write('%s\n%s\n%s\n' % (round.question, round.answer, round.points))
        #text_file = open(filename, "r")
        #lines = text_file.readlines()
        #text_file.close()
    def getLog(self):
        text_file = open filename("data.txt","r")
        lines = text_file.readlines()
        text_file.close()
        while i <= (len(lines)):
            print(lines)


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
dog = Species("animals", "Boasdbo")
dog = Species("animals", "Bsobo")
dog = Species("animals", "Bosadbo")
dog = Species("animals", "Bsaobo")
human = Species("humans", "obo")
human = Species("humans", "asdaobo")
human = Species("humans", "wobo")

dog.show()
firstPopulation.log()
firstPopulation.getLog()
print(firstPopulation.totalPopulation)
print(firstPopulation.animals)
