# Inheritance allows us to define a class that inherits all the methods and prorerties from another class.
# Parent class : is the class being inherited from, also called base class
# Child Class: is the class that inherits from another class, also called derived class.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        return(f"{self.fname} {self.lname}")

p1 = Person("Rohit", "Samanta")
# Create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class Student(Person):
    # when we add the __init__() function , the child class will no longer inherit the parent's __init()__ function
    # The child's __init__() function overrides the inheritance of the parent's __init__() function
    # To Keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    def __init__(self, fname, lname, course="MCA"):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname) # we can also use "super()"
        self.course = course
    
    def printStudentInfo(self):
        print(f"{self.printname()} , Course : {self.course}")

s1 = Student("Rohit", "Samanta")
s1.printStudentInfo()

s2 = Student("Agni", "Banarjee", "BCA")
s2.printStudentInfo()


# 
# Multiple Inheritance : inherit from more than one parent class
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()