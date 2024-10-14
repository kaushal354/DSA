#class and object

#1. define a python class Person with instance object variables name and age.
#set instance object varibales in __init__() method. also define show()
#method to display name and age of a person.
class Person:
    def __init__(self):
        self.name = "KAUSHAL"
        self.age = 95
    
    def getname(self,name):
        self.name = name
    def getage(self,age):
        self.age = age
    def show(self):
        print("name:",self.name,"age:", self.age)

p1 = Person()
p1.setname("kaushalprasad")
p1.setage(85)
p1.show()

#2. Define a class circle with instance object variable radius.
#provide setter and getter for radius. also define
#getArea() and getCircumference()
class circle:
    def __init__(self,radius):
        self.radius = radius

    def setradius(self,radius):
        self.radius = radius
    
    def getradius(self):
        return self.radius

    def getArea(self):
        Area = 3.14 * self.radius ** 2
        print(f"Area:{round(Area,2)}")
    def getCircumference(self):
        Circum = 2 * 3.14 ** 2
        print(f"Circumference: {round(Circum,2)}")

c1= circle(3)
c1.setradius(4)
print(c1.getradius())
c1.getArea()
c1.getCircumference()

#3.Define a class Rectangle with length and breadth as instance
#object variables. provide setDimensions(),showDimensions() and getArea() method in it.
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def setDimensions(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def showDimensions(self):
        print(f"Length:{self.length}")
        print(f"Breadth:{self.breadth}")
    
    def getArea(self):
        Area = self.length * self.breadth
        print(Area)

R1 = Rectangle(23,36)
R1.setDimensions(4,3)
R1.showDimensions()
R1.getArea()

#4. Define a class Book with instance object variable bookid
#,title and price. Initialise them via __init__() method.
#also define method to show book variables.
class Book:
    def __init__(self,bookid,title,price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def showbook(self):
        print(f"bookid:{self.bookid}")
        print(f"title:{self.title}")
        print(f"price:{self.price}")

b1 = Book(42,"jungle book",90)
b1.showbook()

#5. define a class Team with instance object variable a list of team member names.
#provide methods to input member names and display member names.
class Team:
    def __init__(self,vollyball,cricket,football):
        self.vollyball = vollyball
        self.cricket = cricket
        self.football = football


    def inputvollyball(self):
        print(f"total number vacant for vollyball team members: {self.vollyball}")
        self.vollyballteam = []
        for i in range(1,self.vollyball+1):
            membernames = input(f"{i} member name of vollyball:")
            self.vollyballteam.append(membernames)


    def inputcricket(self):
        print(f"total number vacant for cricket team members: {self.cricket}")
        self.cricketteam = []
        for i in range(1,self.cricket+1):
            membersname = input(f"{i} member name of cricket:")
            self.cricketteam.append(membersname)

    def inputfootball(self):
        print(f"total number vacant for football team members: {self.football}")
        self.footballteam = []
        for i in range(1,self.football+1):
            membersname = input(f"{i} member name of football:")
            self.footballteam.append(membersname)

    def displayvollyball(self):
        print("member name for vollyball is:",self.vollyballteam)

    def displaycricket(self):
        print("member name for cricket is:",self.cricketteam)

    def displayfootball(self):
        print("member name for football is:",self.footballteam)



t1 = Team(3,2,4)
t1.inputvollyball()
t1.inputcricket()
t1.inputfootball()
t1.displayvollyball()
t1.displaycricket()
t1.displayfootball()