# Recursion is a common mathematical and programing concept where a fuction calls iteself. 

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    

print("The value of factorial 5 is : ",factorial(5))


# Python has a limit on how deep recursion can go. The default limit is ususally 1000 recursive calls
import sys
print(sys.getrecursionlimit())
# if you need deeper rucursion. you can increase the limit, be carefull as this can cause crashes
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
