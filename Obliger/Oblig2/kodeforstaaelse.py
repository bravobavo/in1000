#Dette er ikke lovlig kode da det vil bli kastet feilmelding til brukeren.
#Feilmeldingen/problemet: Feil vil bli oppgitt pga. bruk av sammenslåing mellom typer
#Altså, et rent tall og en ren tekst kan ikke bli slått sammen.
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
