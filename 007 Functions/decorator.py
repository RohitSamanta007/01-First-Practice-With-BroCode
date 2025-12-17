# A decorator is a function that takes another function as input and returns a new function
# Define the decorator first, then apply it with "@decorator_name" above the function
def changeCase(func):
    def myinner():
        return func().upper()
    return myinner

@changeCase
def myfunction():
    return "Hello Rohit"

print(myfunction())