import datetime

date = datetime.date(2002, 3, 10) # year, month, day
today = datetime.date.today()

print(date)
print(today)

time = datetime.time(12, 30, 24) # hours , minutes, seconds
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y")

print(time)
print(now)

target_datetime = datetime.datetime(2026, 1, 2, 12, 30, 1) # year, month, day, hours, minutes, seconds
current_date = datetime.datetime.now()

if target_datetime < current_date :
    print(f"Target {target_datetime} date has passed")
else:
    print("Target date has not passed")
