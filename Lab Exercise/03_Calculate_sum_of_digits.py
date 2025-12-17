n = input("Enter a number : ")

result = 0

for i in n:
    result += int(i)
    
print(f"The value of the sum of digit of number {n} is : {result}")