'''persons = []
class Person:
        def __init__(self):
            navn = input()
            self.name = navn
            persons.append(self)

        def my_name_is(self):
            print("My name is "+ self.name)

for i in range(0,10):
    Person()

print(persons[2].my_name_is())
'''
#Even better...
class Person:
    def __init__(self):
        navn = input()
        self.name = navn
    def my_name_is(self):
        print(self.name)

objs = [Person() for x in range(10)]
objs[2].my_name_is()
