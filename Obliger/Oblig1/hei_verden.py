#ASSIGNMENT 1.04a
print("Hei verden!")
#ASSIGNMENT 1.04b
alder = 4
print("Alder: ", alder)

alder = 19
#OBS! Value of age is changed.

reader = input("Hva er navnet ditt?")
print ("""
       Hello, %(reader)s
       Sincerely, %(user)s
       """ % {'reader': reader, 'user': "Bavo"})
