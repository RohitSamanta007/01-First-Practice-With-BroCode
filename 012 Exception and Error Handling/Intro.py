# Exception : An event thats interrupts the flow of a programe (like : ZeroDivisionError, TypeError, ValueError)
# Method of handeling: try, except, finally

# print(1 + "1") # TypeError
# a = int("Pizza") # ValueError : when we typecast a value to a wrong datatype

# handle error : 
# try:
#     number = int(input("Enter a number for division : "))
#     print(1/number)
# except ZeroDivisionError:
#     print("You can not divide by zero")
# except ValueError:
#     print("Enter only numbers.")

# print("End of the programe")

# another way to handle all exception
try:
    number = int(input("Enter a number for division : "))
    print(1/number)
except Exception:
    print("You enter some wrong input")
finally:
    print("Do some clenup here")

print("End of the programe")