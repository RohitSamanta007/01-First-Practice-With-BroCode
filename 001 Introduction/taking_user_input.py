# input() : a function that prompts the user to enter data . Returns the entered data as a string

name = input("Whats is your name? : ")

# age = input("How old are you? : ")
# age = int(age)

# we can take input and typecast it immediately
age = int(input("How old are you? : "))
age += 1

print("\n")
print(f"Hello {name}!")
print("HEPPY BIRTHDAY!!")
print(f"You are now {age} years old")
