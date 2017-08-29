#fahrenheit
fahrenheit = 10
print(fahrenheit)
#celcius
temperatur = float((fahrenheit - 32)*5/9)
print(temperatur)

def calclulate():
    runEver = True
    while runEver:
        temp = input("Skriv inn tempen\n")
        if isinstance(temp, float) or isinstance(temp, int):
            temp = float((fahrenheit - 32)*5/9)
            print(temp)
        elif temp == "x":
            runEver = False
        else:
            print("Would you please write a number, or exit using x?")
calclulate()
