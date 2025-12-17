# This is my first python programe (and this is a comment)
print("Hello from Rohit Samanta")
print("I am learning python from BroCode")

#
# Variable = A container for a value (string, integer, float, boolean)
# A Variable behaves as if it was the value it contains
first_name = "Rohit"
print(first_name)

# f-string: to use formatted string literals, being starting with f or F before the opening quotation mark or triple quotation mark, inside this string, you can write a python expression between { and } characters that can refer to variables or literal values
print(f"Hello {first_name}")

# Integers
age = 24
print(f"You are {age} years old")

# float
price = 12.45
print(f"Price of laptop is ${price}")

# Boolean (only two options)
# is_student = True # start with capital latter
is_student = False # start with capital latter
print(f"Are you a student? : {is_student}")
# mostly used for comparisons
if is_student:
    print("You are a student")
else:
    print("You not a registered student")


