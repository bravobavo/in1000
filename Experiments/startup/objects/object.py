class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount (self):
        print ("Total Employee %d"%Employee.empCount)

    def displayEmployee (self):
        print("Name : ", self.name, ", Salary : ", self.salary)

emp1 = Employee("Zaraa", 2000)
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d"% Employee.empCount)

hasattr(emp1, 'age') #returns false as no age attribute exists
getattr(emp1, 'name') # returns "Manni"
setattr(emp1, 'age', 8) #creates age and adds a value
#getattr(obj,name[,default])   acess attribute of object
#hasattr(obj,name)  Check if attribute exists
#setattr(obj,name,value)  set or create an attribute
#delattr(obj,name) deletes an attribute

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
#__dict__  (class docuumentation)
#__name__  (class name)
#__module__ (module name in which the class is defined)
#__bases__  (A possibly empty tuple containing the base classes)

# issubclass(sub, sup)  retuns trueif True
#isinstance(obj, Class) returns true if True
#Sample Call : obj = className(args)

class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter._JustCounter__secretCount)
