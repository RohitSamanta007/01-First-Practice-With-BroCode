 
# age = int(input("Enter your age : "))
age = 18

if age >=18:
    print("Now your are eligible for vote")
elif age < 0:
    print("Invalid age")
else:
    print("You must be 18+ for vote")


# Shorthand if-else statement as the ternary operator or a conditional expression
# Syntex : <value_if_True> if <condition> else <value_if_false>
print("Eligible to vote" if age>=18 else "Not eligible to vote")

# Match-case statement (switch) : an alternative of using many "elif" statements. Execute some code if  a value matches a "case"

day = int(input("Enter the number for day : "))

match day:
    case 1:
        print("Its is Monday.")
    case 2:
        print("Its is Tuesday.")
    case 3:
        print("Its is Wednesday.")
    case 4:
        print("Its is Thursday.")
    case 5:
        print("Its is Friday.")
    case 6:
        print("Its is Saturday.")
    case 7:
        print("Its is Sunday.")
    case _: # if no matching case . it will execute
        print("Not a valid day")
