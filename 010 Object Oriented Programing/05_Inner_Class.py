# Inner Class : is a class defined inside another class.
# The inner class can access the properties and methods of the outer class
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.

class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def display(self):
            print("This is the inner class method")

o1 = Outer()
print(o1.name)

# To access the inner class, create an object of the outer class, and then create an object of the inner class
i1 = o1.Inner()
i1.display()

# Accessing Outer class fom Inner class: Inner classes do not automatically have access to the outer class instance.
# we need to pass the outer class instance as a parameter
class Outer:
    def __init__(self):
        self.name = "Rohit"
    
    class Inner:
        def __init__(self, outer):
            self.outer = outer
        
        def display(self):
            print(f"Outer class name : {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()