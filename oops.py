

### class
class Person:
    #attributes
    name=""
    age=0
    place=""

    #methods
    def setdetails(self,n,a,p):  #self keyword ---- reference of current object
        self.name=n
        self.age=a
        self.place=p
    def displaydetails(self):
        print(self.name,self.age,self.place)

obj1=Person()
obj2=Person()

obj1.setdetails('arun',25,'ekm')
obj1.displaydetails()



##using dynamic
### class
class Person:
    # attributes
    name = ""
    age = 0
    place = ""

    # methods
    def setdetails(self):
        self.name = input("Enter the name")
        self.age = int(input("Enter the age"))
        self.place = input("Enter the place")

    def displaydetails(self):
        print(self.name, self.age, self.place)


obj1 = Person()
obj2 = Person()

obj1.setdetails()
obj1.displaydetails()

obj2.setdetails()
obj2.displaydetails()



#Personn using __init__ function
class Person:
    # attributes
    name = ""
    age = 0
    place = ""

    # methods
    def __init__(self):
        self.name = input("Enter the name")
        self.age = int(input("Enter the age"))
        self.place = input("Enter the place")

    def displaydetails(self):
        print(self.name, self.age, self.place)


obj1 = Person()
obj1.displaydetails()

obj2 = Person()
obj2.displaydetails()


#create a class named circle with attribute radius and method getarea() and getperimeter()
class Circle:
    radius=0
    def __init__(self):
        self.radius=int(input("Enter the radius"))
    def getarea(self):
       
        self.area=3.14*(self.radius **2)
        print(self.area,"area of circle")
    def getperimeter(self):
        
        self.perimeter=2*3.14*self.radius
        print(self.perimeter ,"perimeter of a circle")

circle1=Circle()
circle2=Circle()
circle1.getarea()
circle1.getperimeter()
circle2.getarea()
circle2.getperimeter()









