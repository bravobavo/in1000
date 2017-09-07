#fahrenheit
fahrenheit = 10
print("Temperatur i fahrenheit er %s" % (fahrenheit))
#celcius
temperatur = float((fahrenheit - 32)*5/9)
print("Temperatur i celcius er %s" % (temperatur))


def inputNumber(message):
    while True:
        try:
           number = int(input(message))
        except ValueError:
           print("Not an integer! Try again.")
           continue
        else:
           return number
           break

def calculate ():
    looping = True
    while looping:
        number = inputNumber("Skriv inn temperatur i fahrenheit : ")
        convTemp = float((number - 32)*5/9)
        print("Your temperatue in celcius is "+str(convTemp))
        choice = input("Press x to exit")
        if choice == "x":
            looping = False
        else:
            print("Starting over again")

calculate()
