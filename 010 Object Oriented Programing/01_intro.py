# Object : is a bundle of related attributes (variables) and methods (functions) Ex: phone, laptop, book
# You need a "class" to create many objects
# class : (blueprint) used to design the structure and layout of an  object
class MyClass:
    x = 10
    
o1 = MyClass()
print(o1.x)

# delete object using the "del" keyword
del o1
# print(o1.x)

# Class defination cannot be empty, but if you for some reason have a class defination with no content, put in the "pass" statement to avoid getting error.
class Person:
    pass  

# The "__init__()" Method : 
# All class have a built-in method called "__init__()", which is always executed when the class is being initiated.
# It is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Rohit Samanta", 24)
print("Name : ",p1.name, " , Age: ", p1.age)
# The "__init__()" method is called automatically every time the class is being used to create new object

# Default values in __init__()
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

p2 = Person("Agni", 22)
p3 = Person("Gourabh")
print(p2.name , "  ", p2.age)
print(p3.name , "  ", p3.age)

# The "self" Parameter : 
# The "self" parameter is a reference to the current instance of the class
# It is used to access properties and methods that belongs to the class
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name}, and my age is {self.age}")

p4 = Person("Rohit Samanta", 24)
p4.greet()
# "self" parameter must be the first parameter of any method in the class
# It does not have to be named "self", you can call it whatever you like, but it have to be the first paramenter of any method in the class.
class Person:
    def __init__(myObject, name, age):
        myObject.name = name
        myObject.age = age
    
    def greet(abc):
        print(f"Hello, my name is : {abc.name}, my age is : {abc.age}")

p5 = Person("Agni Banarjee", 22)
p5.greet()
# it is strongly recomended to use "self" as it is the convention in python and makes your code more readable to others

# calling method using "self"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return "Hello, "+self.name
    
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to out website")

p6 = Person("Rahul Kar", 26)
p6.welcome()


# Class Properties
# you can delete properties from object using the "del" keyword
del p1.name
# print(p1.name) # This gives error
print(p1.age)

# Class Properties VS Object Properties
# Properties defined inside __init__() belongs to each object (instance properties)
# Properties defined outside methods belong to the class itself(class properties) and are shared by all objects
class Person:
    species = "Human" # class Properties
    lastName = ""
    
    def __init__(self, name):
        self.name = name # Object Instance properties
    
p7 = Person("Rohit")
p8 = Person("Sourabh")
print(p7.name)
print(p7.species)
print(p8.name)
print(p8.species)

# when we modify a class property, it affects all objects
print(p7.lastName)
print(p8.lastName)

Person.lastName = "Samanta"

print(p7.lastName)
print(p8.lastName)

# another example of class variables
class Student:
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Rohit Samanta", 24)
student2 = Student("Agni Banerjee", 22)
print(Student.num_students)

# Add new Property to an object
class Person:
    def __init__(self, name):
        self.name = name

p9 = Person("Rohit")
p9.age = 24
p9.course = "MCA"
print(p9.name)
print(p9.age)
print(p9.course)
# Adding Properties this way only adds them to that specific object, not all objects of the class

# Class Methods : 
# all methods must have "self" as the first parameter


# Magic Methods : (__eq__, __str__) : They are automatically called by many of python built-in operations. They allow developers to define or customize the behavior of objects
# The "__str__()" method: is a special method that controls what is returned when the object is printed
print(p9)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self): # print(p10)
        return f"Name : {self.name}, age:{self.age}"
    
    def __eq__(self, other): # check equal : print(p10 == p11 )
        return self.name == other.name 
    
    def __lt__(self, other): # check less than : print(p10 < p11)
        return self.age < other.age

    def __gt__(self, other): # check greater than : print(p10 > p11)
        return self.age > other.age

    def __add__(self, other): # Add two : print(p10 + p11)
        return self.age + other.age
        
    def __contains__(self, keyword): # print("Rohit" in p12)
        return keyword in self.name
    
    def __getitem__(self, key): # get an item using index : print(p10["name"])
        if key =="name":
            return self.name
        elif key =="age":
            return self.age
        else:
            return f"Key {key} is not found"

            
    def greet(self):
        print(f"Hello {self.name}! How are you today?")
        
p10 = Person("Rohit Samanta", 24)
p11 = Person("Rohit Samanta", 22)
p12 = Person("Agni Samanta", 22)

print(p10)
print(p11)
print(p10 == p11 )
print(p10 < p11)
print(p10 > p11)
print(p10 + p11)
print("Rohit" in p12)
print(p10["name"])
print(p10["course"])

p10.greet()

# delete methods from class using "del" keyword
del Person.greet
# p10.greet() # This gives error as "greet" method from class is already removed.

