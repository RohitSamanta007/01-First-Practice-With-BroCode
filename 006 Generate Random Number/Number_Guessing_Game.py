import random

low,high = 1, 100
randomNumber = random.randint(low, high)

count = 0
print(f"Guess a number between {low} and {high} : ")
print()
while True:
    myNum = input(f"Enter Your guess between {low} to {high} :  ")
    if(myNum.isdigit()):
        myNum = int(myNum)
    else:
        continue
    
    count = count+1
    if myNum == randomNumber:
        break
    elif myNum > randomNumber:
        high = myNum
    else:
        low = myNum

print(f"Your total attemp : {count}, and the actual number is : {randomNumber}")