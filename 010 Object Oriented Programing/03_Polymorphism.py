# Polymorphism refers to methods/functions/operators with the same name that can be executed on many objects or classes

# Class Polymorphism : we can have multiple classes with the same method name
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
print()  

# Inheritance class Polymorphism:
# we can override the methods of parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Car Running")

class Boat(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Boat Sailing")

class Plane(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Plane Flying")

c1 = Car("Mercedes", "AMG G63")
c1.move()

b1 = Boat("Lamborgini", "Tourning 20")
b1.move()

p1 = Plane("Boeing", "747")
p1.move()

# Because of polymorphism we can execute the same method for all classes


# abstruct Method : method declared in an abstruct class that has a declaration but no implementation
from abc import ABC, abstractmethod

class Shape:
  
  @abstractmethod
  def area(self):
    pass
  
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return 3.143 * self.radius ** 2

class Squre(Shape):
  def __init__(self, side):
    self.side = side
  
  def area(self):
    return self.side ** 2

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
    
  def area(self):
    return self.base * self.height * 0.5

shapes = [Circle(4), Squre(5), Triangle(6,7)]
 
for shape in shapes:
  print(f"{shape.area()}cm²") # superscript ^2 : Windows : Alt + 0178 , Mac : Control + window + space