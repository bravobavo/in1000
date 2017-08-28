#ASSIGNMENT 1.12
#VERSION 1
#The main global variables are initialized and declared
questions = ["What was the author's name of the book called \"Menn hater kvinner\"\n",
             "What is \"Tzatziki\"?\n","Who wrote \"Kingskiller chronicles\"?\n"]
answers = ["Stieg Larsson", "Sauce", "Pathrick Rothfuss"]
points = 0

#First round waits for user input
round0 = input(questions[0])
#If input is equivalent with the answer
if round0.lower() == answers[0].lower():
    points += 3
    print(answers[0] + " is correct!\nYou gained three points!")
#Else if one part is mentioned. User gets another chance
elif round0.lower() == "stieg" or round0.lower() == "larsson":
    points += 1
    fullName = input("You gained a point.\nBut what is the full name for two additional points?\n")
    if fullName.lower() == answers[0].lower():
        points += 2
    else:
        print ("Sorry. The answer is " + answers[0])
#If user fails to answer any part of the question...
else:
    print("Not correct.")
#Whatever if-statement is played. A result is given at the end.
print("\nYou currently have " + str(points) + " points.\n")

#The same pattern as last block.
round1 = input(questions[1])
if round1.lower() == answers[1].lower():
    points += 2
    print (answers[1] + " is correct!")
elif round1.lower() == "a sauce":
    points += 2
    print ("A " + answers[1] + " is correct!")
else:
    print("Not correct.")
print("You currently have " + str(points) + " points.\n")

#The exact same pattern as the first block
round2 = input(questions[2])
if round2.lower() == answers[2].lower():
    points += 3
    print (answers[2] + " is correct!")
elif round2.lower() == "patrick" or round0.lower() == "rothfuss":
    points += 1
    fullName = input("You gained a point.\nBut what is the full name for two additional points?\n")
    if fullName.lower() == answers[2].lower():
        points += 2
    else:
        print ("Sorry. The answer is " + answers[2])
else:
    print("Not correct.")
print("You currently have " + str(points) + " points.\n")
