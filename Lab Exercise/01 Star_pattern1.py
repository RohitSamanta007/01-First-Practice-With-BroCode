# n = int(input("Enter the value of n : "))
n = 4 

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()