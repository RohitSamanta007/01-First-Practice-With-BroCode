principle = 0
interest_rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the loan ammout : "))
    if(principle <= 0):
        print("Principle ammount can not be zero or less then zero")

while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate : "))
    if(interest_rate <= 0):
        print("Interest rate can not be zero or less then zero")

while time <= 0:
    time = float(input("Enter the time in years : "))
    if(time <= 0):
        print("Time can not be zero or less then zero")

# finalAmmount = principle * pow((1 + interest_rate/100), time)
finalAmmount = principle * ((1 + interest_rate/100)**time)
print(f"The total ammout of principle of {principle} after {time} years of {interest_rate} : {finalAmmount:.2f}")