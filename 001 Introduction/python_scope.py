# Global Keyword: if you need to create a global variable, but are stuck in the local scope, then we can use the "global" keyword
# The "global" keyword makes the variable global

def myFunc():
    global x
    x = 300

myFunc()
print(x)

# To change the vlaue of the global variable inside a function, refer to the variable by using the "global" keyword
x = 300
def my_func():
    global x
    x = 500

my_func()
print(x)