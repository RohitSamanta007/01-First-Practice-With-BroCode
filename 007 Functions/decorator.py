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
print()

# another example by BroCode

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print(f"You add sprinkles on {args[0]}")
        func(*args, **kwargs)
    return wrapper

def add_chocolet(func):
    def wrapper(*args, **kwargs):
        print("You add some chocolate")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_chocolet
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream.")

get_ice_cream("vanilla")