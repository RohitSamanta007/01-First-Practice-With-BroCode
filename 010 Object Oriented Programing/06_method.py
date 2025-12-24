# Static Method : a method that belongs to a class rather than any object from that class (instance)
# Usually used for general utility functions

# Instance Method : Best for operations on instances of the class (objecs)
# Static Method : Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} : {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Cashier", "Cook"]
        return position in valid_positions

emp1 = Employee("Rohit Samanta", "Developer")
print(emp1.get_info())

print(emp1.is_valid_position(emp1.position))

print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Tester"))

print()

#
# Class Method : Allow operations related to the class itself
# Take (cls) as the first parameter, which represent the class itself
class Student:
    count = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        
    def get_info(self):
        return f"{self.name} : {self.gpa}"
    
    @classmethod
    def getCount(cls):
        return f"Total number of students : {cls.count}"
    

print(Student.getCount())