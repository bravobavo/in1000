class Vare:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris
varer = [Vare("brød",25),Vare("melk",15), Vare("ost",78),Vare("yoghurt",12)]

sum=0
for i in varer:
    current = input("Vare: {0}. Pris: {1}. Hvor mange?".format(i.navn, i.pris))
    sum += int(current) * int(i.pris)
print(sum)

#Oppgavelinjer : 15.   Personlig : 10 (desto flere produkter, desto fære linjer)
