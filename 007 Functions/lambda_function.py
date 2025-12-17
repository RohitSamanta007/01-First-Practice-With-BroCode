# Lambda Function : is a samll anonymous function.
# A lambda function can take any number of arguments, but can only have one expression
# Syntax :  lambda arguments: expression (this expression is executed and the result is returned)
x = lambda a: a+10
print(x(5))

x = lambda a, b: a * b
print(x(10, 20))

# why use : lambda is better shown when you use them as an anonymous function inside another function
# Let say : you have a fucntion defination that takes one atgument, and that argument will be multiplied with an unknown number.
def myFunc(n):
    return lambda a: a * n
# use that function definition to make a function that always dobules the number you send in
myDoubler = myFunc(2)
print(myDoubler(10))
myTripler = myFunc(3)
print(myTripler(10))

# Lambda function are commonly used with built-in functions like : map(), filter() and sorted()

# Using with "map()" : applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# using with "filter()" : create a list of items for which a  function returns True
oddNumbers = list(filter(lambda x: x%2 != 0, numbers))
print(oddNumbers)

# using with "sorted()" : use as a key for custom sorting
students = [("Rohit", 24), ("Sourabh", 23), ("Agni", 20), ("Gourav", 21)]
sorted_Students = sorted(students, key=lambda x: x[1])
print(sorted_Students)
