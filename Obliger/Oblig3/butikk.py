'''ASSIGNMENT 2'''
class Butikk:
    def __init__(self):
        self.content = {}
    def addItem (self, i, p):
        self.content[str(i)] = float(p)
    def showItems(self):
        for poop, value in self.content.items():
            print('{0:15} => {1:5}kr'.format(str(poop), value))
b = Butikk()
b.addItem('melk',14.90)
b.addItem('yoghurt',24.90)
b.addItem('pizza',39.90)
b.showItems()
b.addItem('tiramisu',100.90)
b.addItem('Franzs first price',12.90)
b.showItems()
