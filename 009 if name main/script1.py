# if __name__ == __main__ : (this script can be imported or run standalone)
# Functions and classes is this module can be reused without the main block of code executeing
# Good practice (Code is modular, healps readibility, leaves no global variables, avoid unintended execution)


# from script2 import *
# print(__name__)

def favourite_food(food):
    print(f"Your favourite food is : {food}")

def main():
    print("This is script1")
    favourite_food("Chicken Curry")
    print("Goodbye!")

if __name__ == '__main__':
    main()