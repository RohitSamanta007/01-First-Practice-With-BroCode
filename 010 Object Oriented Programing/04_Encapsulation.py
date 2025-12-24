# Encapsulation is about protecting data inside a class. while controlling how the data can be accessed from outside the class
# This prevents accidental changes to your data and hides internal details of how your class works

# Private Properties: we can make properties private by using a double underscore "__" prefix
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

p1 = Person("Rohit Samanta", 24)
print(p1.name)
# print(p1.age) # this will cause an error

# Private property cannot be accessed directly from outside the class
# To access private property, we can create a getter and setter method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age>0:
            self.__age = age
        else:
            print("Age must be positive")

    def printInfo(self):
        print(f"Hello, my name is {self.name}, and my age is {self.__age}")

p2 = Person("Rohit Samanta", 24)
p2.printInfo()
p2.set_age(23)
p2.printInfo()
print(f"Access private properties of a class using getMethod : value is :{p2.get_age()}")

# Protected Properties:
# Using single underscore "_" prefix
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # protected property
    
    def printInfo(self):
        print(f"Name : {self.name}, Salary : {self._salary}")

p3 = Person("Rohit Samanta", "40LPA")
p3.printInfo()

#
# Private methods: make methods private by using the double underscore "__" prefix
# Private methods cannot be called directly from outside the class. this method can only be used by other methods inside the class
class Calculator:
    def __init__(self):
        self.result = 0
        
    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        else:
            return True
        
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

clac = Calculator()
clac.add(10)
clac.add(5)
print(clac.result)


# 
# Name Mangling: is how python implements private properties and methods.
# When we use double underscore "__", pyton automatically renames it internally by adding "_ClassName" in front
# Example :(in previous) "__age" becomes "_Person__age". [_ClassName__PropertyName]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
p4 = Person("Rohit", 24)
# Mangle the name
print(p1._Person__age)

# While you can access the private properties using the mangled name, it is not recommended. it defeats the purpose of encapsulation.

        
#
# Getter and setter Method : Using "@Property"
# @property : Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit : Add additional logic when read, write or delete attribute
# Gives we getter, setter and deleter methods
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    @property
    def width(self): # get value
        return f"{self.__width}cm"
    
    @property
    def height(self): # get value
        return f"{self.__height}cm"

    @width.setter
    def width(self, new_width):
        if new_width> 0:
            self.__width = new_width
        else:
            print("width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height> 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero")
    
    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")
    
rect = Rectangle(10, 20)

print(rect.width)
print(rect.height)

rect.width = 100
rect.height = 200

print(rect.width)
print(rect.height)

del rect.width
del rect.height
