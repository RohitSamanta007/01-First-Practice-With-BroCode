name = input("Enter your full name : ")

result = len(name) # return the length of the sting (integer), it does not include space characters
result = name.find("a") # find the first occurrence of the matching characters using zero indexing, if not found return -1
print(result)

result = name.rfind("a") # find the last occurrence of the matching characters using zero indexing, if not found return -1
print(result)

name = name.capitalize() # it capitalize the first latter of the string
print(name)
name = name.upper() # it do uppercase all of the latters of the string
print(name)
name = name.lower() # it do lowercase all of the latters of the string
print(name)

isNumber = name.isdigit() # returns true if string contains only numbers , return false: mix of numbers and characters
print(isNumber)
result = name.isalpha() # returns true if string contains only alphabetical characters , return false: mix of numbers and characters or contains space
print(result)

result = name.count("a") # count the number of occurrence of a string
print(result)

phone_number = "123-345-678-101"
print(phone_number)
phone_number = phone_number.replace("-", " ")
print(phone_number)

# to get all methods
print(help(str))