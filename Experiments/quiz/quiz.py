#VERSION 2
#Contains attributes and function-calling from class Quiz
class Quiz:
    def __init__(self):
        self.rounds = []
        self.highscore = 0
        self.maxPoints = 0

    def appendRound(self,round):
        self.rounds.append(round)
        self.maxPoints += round.points

    def printResults(self):
        for round in self.rounds:
                round.printResults()

    def printRounds(self):
        for round in self.rounds:
            round.printRounds()

    def start(self):
        for round in self.rounds:
            answer = input(round.question+"\n")
            if round.isCorrect(answer):
                self.highscore += round.givenPoints
                print ('You received %s! Current score: %s' % (round.givenPoints, self.highscore))
            else:
                print("Sorry mate, give more effort!")

#Contains attributes and function-calling from class Round
class Round:
    totalRounds = 0
    def __init__(self, question, answer, points):
        Round.totalRounds += 1
        self.ID = Round.totalRounds
        self.question = question.rstrip('\n')
        self.answer = answer.rstrip('\n')
        self.points = int(points.rstrip('\n'))
        self.givenPoints = 0

    def isCorrect(self,answer):
        if self.answer.lower() == answer.lower():
            self.givenPoints = self.points
            return True
        else:
            return False

    def printResults(self):
        print("Round %s: %sp/%sp" % (self.ID,self.givenPoints,self.points))

    def printRounds(self):
        print("%s. Question %s: %s" % (self.ID,self.ID,self.question))

#Reads from txt_file
def getQuizFromFile(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    text_file.close()
    currentQuiz = Quiz()
    i = 0
    while i < len(lines):
        round = Round(lines[i],lines[i+1],lines[i+2])
        currentQuiz.appendRound(round)
        i += 3
    return currentQuiz


#Starts the quiz-questions
while True:
    sheet = input("Which quiz-sheet do you wish to play?\n  0  |  1  |  2\n")
    #Choose sheet to then manipulate
    if sheet == "0" or sheet == "1" or sheet == "2":
        quiz = getQuizFromFile("data"+sheet+".txt")
        action = input("Start quiz! (0) | Add a new round! (1) | Remove a round! (2)")
        #Start quiz
        if action == "0":
            quiz.start()
            quiz.printResults()
        #View and add round
        elif action ==  "1":
            quiz.printRounds()
            round = Round(input("What is the new question? "),
                    input("What is the answer? "),
                    input("How many points should be given? "))
            quiz.appendRound(round)
            with open("data2.txt", "a") as myfile:
                myfile.write('%s\n%s\n%s\n' % (round.question, round.answer, round.points))
        elif action == "2":
            quiz.printRounds()
            remove = input("Choose a round to remove, or press \"x\" to exit.")
            if remove == "x":
                print("Exiting...")
            elif not isinstance(remove, int):
                input("Write a number -.-\n")
            else:
                # QUESTION: how the hell we gonna do this..
                print(remove + "in process...")
        else:
            input("Please write one of the given options...\n")
