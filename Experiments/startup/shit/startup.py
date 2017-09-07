"""This is a calculator"""
##### CALCULATOR ######
import time
import datetime
# Functions
def plus(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
# Cool Loop 2
while True:
    # Variables
    index = 0
    tall1 = ""
    tall2 = ""
    metode = ""
    forrige = 0
    inputShit = input("Gi oss et regnestykke paa formen x[*,/,+,-]y\n")
    for value in inputShit:
        try:
            # Er det et tall?
            int(value)
        except ValueError:
            # Det er ikke et tall, da sjekker vi om det er en operator
            if value == "+" or value == "-" or value == "*" or value == "/":
                metode = value
                tall1 = int(inputShit[0:index])
                forrige = index
            else:
                # SHIT det er ikke en operator, vi maa avslutte
                error = "Sorry {} er ikke et stottet tegn".format(value)
                raise ValueError(error)
        index = index + 1

    tall2 = int(inputShit[forrige+1:])
    print("%s %s %s ER..." % (tall1, metode, tall2))
    time.sleep(2)

    if metode == "+":
        print( plus(tall1, tall2))
    elif metode == "-":
        print(subtract(tall1, tall2))
    elif metode == "*":
        print(multiply(tall1, tall2))
    elif metode == "/":
        print(divide(tall1, tall2))


##### STARTUP #####
from random import randint as r
#Inserts values
ray = []
for i in range(0,10):
    ray.append(r(0,50))
print(ray)
nRay = []
print(nRay)


def risingOrder(z):
    nRay = input("Name of new array?\n")
    a = 0
    while a < (len(z)-1):
        b=0
        while b < len(z)-1
            if ray[a] = ray[b]:
                value = ray[b].pop()
                nRay.append(value)
                break

        check all other items...
        then put in if smallest
        start over again with new number or try other number
        a += 1

risingOrder(ray)


###### AADNE ######
#Lag et program som fyller disse kravene:
#1. programmet skal vaere en quiz med 5 sporsmaal
#2. det skal vaere et poengsystem, ett poeng for hver oppgave
#3. programmet skal komme med positive tilbakemeldinger underveis
poeng = 0

sporsmaal = ["Hvor mange farger er det i regnbuen?\n",
 "Hvor mange grader er det i en sirkel?\n",
 "Hvilken vei peker den rode pekeren paa ett kompass? (nord/sor/ost/vest)",
 "Hvor mange strenger har en cello?\n",
 "Hvem er den kuleste personen i verden?\n"]

fasit = ["7","360","nord", "4", "meg"]

tilbakemelding = {
"positiv":["Dette gaar kjempebra",
"DAMN!!! du er god ass, viste du ville klare det",
"Du har et sjeldent talent innen orientering, lukter jeg en toppidretsutdover?",
"Lukter jeg en fremtidig musikker. Helt riktig svar!",
"Ja, det er deg det."],
"negativ":["awwww, det er desverre feil, riktig svar er 7. men jeg er sikker paa at du faar riktig paa neste, kjor paa trooper",
"Det sporsmaalet var litt i vanskeligste laget, jeg maatte faktisk google det for aa finne riktig svar.",
"Ikke mist motet, neste sporsmaal tar du<3",
"riktig svar var 4. Saanne musikk greier er for nerder uansett",
"Du, er den kuleste personen i verden."]
}
,
#Selve spørringen
a = 0
for i in sporsmaal:
    svar = input(i)
    if str(svar) == fasit[a]:
        print(tilbakemelding["positiv"][a])
    else:
        print(tilbakemelding["negativ"][a])
    a += 1
print("Du fikk " + str(poeng) + " av 5 riktige. Unasett hva resultatet er saa definerer det ikke deg paa noen maate.")
