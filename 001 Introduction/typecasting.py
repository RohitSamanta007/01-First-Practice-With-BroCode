#
# Typecasting : is the process of converting a variable from one data type to another
# we have various function to do : str(), int(), float(), bool()
name = "Rohit Samanta"
age = 24
gpa = 4.1
is_student = True

age += 1

# type() function is used to get datatype of a variable 
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
print("\n")

# typecast float to integer
print("typecast float to integer")
print(id(gpa))
gpa = int(gpa)
print(f"Type of gpa : {type(gpa)}")
print(gpa)
print(id(gpa))
print("\n")

# typecast integer to float
print("typecast integer to float")
age = float(age)
print(type(age))
print(age)

# typecast integer to string
print("typecast integer to string")
age = str(age)
# age += 1 # this line gives error as addtion can only done with intergers not with strings
age += "1" # this will be fine as it concat the string with another string
print(type(age))
print(age)

# typecast string to boolean
print("typecast string to boolean")
name = bool(name) # if it is a empty string then its boolean value will be false otherwise it will be true
print(type(name))
print(name)