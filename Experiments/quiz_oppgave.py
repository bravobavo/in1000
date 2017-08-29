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
