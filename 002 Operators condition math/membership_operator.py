# Membership operator is used to test weather a value or variable is found in a sequence(string, list, tuple, set or dictionary)
# it uses : "in" and "not in"

# use with string
# name = "Rohit Samanta"
# char = input("Enter a character to check : ")

# if char in name:
#     print(f"The character {char} is present in name '{name}'")
# else:
#     print(f"The character {char} is not present")
    
    
# use with dictionary
studentGrades = {
    "Rohit" : "A",
    "Agni" : "B",
    "Gourabh" : "C",
    "Pankaj" : "D"
}

student = input("Enter a student name: ")

if student in studentGrades: # it search within key
    print(f"{student}'s grade is {studentGrades[student]}")
else:
    print(f"{student} is not found")

