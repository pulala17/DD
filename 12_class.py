class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")    

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()   

point2 = Point()
point2.x = 4
print(point2.x)

#------------------
class Point:
    def __init__(self ,x,y):
        self.x = x #self refer to the current object
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")    

point = Point(18,20)
print(point.x)
point.x = 33
print(point.x)

#----------------------------
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")


John = Person("John Smith")
#print(John.name)
John.talk()

Bob = Person("Bob Smith")
Bob.talk()

#----------------------------------------
class Mammal:
    def walk(self):
        print("walk")

class dog(Mammal):
    def bark(self):
        print("bark!")

class cat(Mammal):
    pass 

dog1 = dog()
dog1.walk()
dog1.bark()







