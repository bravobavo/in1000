#OPPGAVETEKSTEN:
#Lag et spørsmål der brukeren for valget til å endre oppgitt spørsmål
import sys
while True:
    favoritt = input("Hva er ditt favorittband?\n")
    valg = input("Du svarte "+favoritt+", vil du endre svaret? (y/n)")
    if valg == "y":
        print("Supert!")
    elif valg == "n":
        print("Den er grei. Du får endre på det")
        sys.exit()
    else:
        print("Skriv enten y/n, De skrev: " + valg)
