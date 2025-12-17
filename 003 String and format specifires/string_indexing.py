# indexing = accessing elements of a sequence using [] (indexing operator)
# [start: end: step] -> start inclusive and end exclusive

name = "Rohit Samanta"

print(name[4])
print(name[:4])
print(name[1:4])
print(name[:4:-2]) 
print(name[-1]) # print the last character of the string
print(name[::-1]) # reverse a string
print(name[::2]) 

credit_number = "1234-5678-9012-3456"

print(f"The last 4 digits of credit card is : {credit_number[-4:]}")
