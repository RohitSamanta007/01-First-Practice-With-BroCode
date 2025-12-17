# function = A block of reusable code
# place () after the function name to invoke it
# if a function doesn't have a return statement , it returns None by default
def happy_birthday(name="", age=18):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} year old")
    print(f"Happy birthday to {name}!")
    print()

# The code inside the function must be indented. Python uses indentation to define code blocks.
# A function name can only contain letters, numbers, and underscores
happy_birthday("Rohit Samanta", 24)
happy_birthday()

# Function defination cannot be empty, if you need to create a function without any code, use the "pass" statement
def myFunction():
    pass
# "pass" statement is ofter used when developing, allowing you to define the strucutre first and implementing details later

# returning fron a function : used to end a function and send a result back to the caller
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def add(a, b):
    return a+b

print("The value of the addition is : ",add(10, 20))
print()

# pass by value and pass by reference
def swapValue(a, b):
    temp = a
    a = b
    b = temp
    print("The value of a inside function is : ", a, " , and the value of b inside function is : ", b)
    
a = 10
b = 20
print("The value of a is : ", a, " , and the value of b is : ", b)
swapValue(a, b)
print("The value of a is : ", a, " , and the value of b is : ", b)
print()

#
# Keyword Argument(kwargs) : an argument preceded by an identifier, helps us with readability, order of arguments doesn't matter
def printHello(greeting, title, firstName, lastName):
    print(f"{greeting}, {title} {firstName} {lastName}")

printHello("Hello", title="Mr.", lastName="Samanta", firstName="Rohit") # positional argument must be in first position then after the keyword argument comes, no matter the positions

# Positional-Only Argument : add ",/" after the parameters
def myFunction(name, /):
    print("Hello ", name)
myFunction("Rohit")
# myFunction(name="Rohit") # this line throw an error as the function takes only positional arguments

#
# "*args" and "**kwargs" : By default, a function must be called with the correct number of arguments. However, sometimes you may not know how many arguments that will be passed into your function.
#   *args and **kwargs allow function to accept a unknown number of arguments

# *args : allow function to accept any number of positional arguments.
# Inside the funtion, "args" becomes a tuple containing all the passed arguments.
def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(10, 20, 30))
print(add(10))
# we can combine regular parameter with *args
def func(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")
    print()
    
func("Hello", "Rohit", "Rahul")
func("Hello", "Rohit", "Sourabh")

# The "**kwargs" parameter allows a function to accept any number of keyword arguments.
# inside a function, "kwargs" becomes a dictionary containing all the keyword arguments
def func1(**kwargs):
    print("Type: ", type(kwargs))
    print("Name: ", kwargs["name"])
    print("Age: ", kwargs["age"])
    print("All Data: ", kwargs)

func1(name="Rohit Samanta", age=24, course="MCA")

# Combination of *args and **kwargs in the same function.
# The order must be : 1. regular parameters, 2. *args, 3. **kwargs
def combineFunction(title, *args, **kwargs):
    print("Title: ", title)
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)
    print()

combineFunction("User Info", "Email", "Rohit", age=24, city="Kolkata")

# Unpacking Arguments
# The "*" and "**" operators can also be used when calling functions to unpack(expand) a list or dictionary into a separate arguments
# if you have values stored in a list, you can use "*" to unpack them into individual arguments
def addFunc(*items):
    result = 0
    for item in items:
        result += item
    return result

numbers = [10, 20, 30, 40, 50]
ans = addFunc(*numbers)
print("The value of addition using * is : ", ans)
# if you have keyword arguments stored in a dictionary, we can use ** to unpack them into keyword arguments
def my_function(fname, lname):
    print("Hello ", fname, " ", lname)

person = {"fname": "Rohit", "lname": "Samanta"}
my_function(**person)


