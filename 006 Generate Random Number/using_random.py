import random
import math

# random integer
number = random.randint(1,  6)
print(number)

low = 2
high = 100
number = random.randint(low,  high)
print(number)

# random floating point number 
floatNum = random.random() # it only genetate floating point number between 0 to 1
print(floatNum)
number = float(number) + round(floatNum, 2)
print(number)

# choice between options
options = ("rock", "paper", "scissors")
computerChoice = random.choice(options)
print(computerChoice)

# suffle the sequence
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)