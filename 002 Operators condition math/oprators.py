count = 5

print(f"Type of count : {type(count)}")
print(f"Memory address of count : {id(count)}")

count = count/2
print(f"The value of count is : {count}")
print(f"Type of count : {type(count)}")
print(f"Memory address of count : {id(count)}")

count = count ** 2
print(f"The value of count is : {count}")

#
# Logical operators : evaluate multiple conditions (or, and , not)
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


# and operator
is_sunny = False

if temp >=28 and is_sunny:
    print("It is hot outside")
# elif temp < 28 and temp > 0 and is_sunny:
elif 0 < temp < 28 and is_sunny: # we can write the above expression like this
    print("It is good time to play football")
# not operator
elif 28>temp>0 and not is_sunny:
    print("It is warm outside and not sunny")
    

#
# conditional expression (not a operator) : A one-line shortcut for the if-else statement(ternary operator), print or assign one of two values based on a condition
# syntex: X if condition else Y

num = -5
num = 11

print("Positive" if num>0 else "Negative")
print("Even" if num%2==0 else "Odd")
