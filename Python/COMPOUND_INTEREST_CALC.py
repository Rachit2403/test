#Priniciple, Interest, Time.

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter Principle amount: "))
    if principle <=0:
        print("Principle cannot be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Enter Rate of interest in percent: "))
    if rate <=0:
        print("Rate cannot be less than or equal to zero!")

while time <= 0:
    time = int(input("Enter Time in years: "))
    if time <=0:
        print("Time cannot be less than or equal to zero!")
    
print(f"So, your principle is {principle:,}!")
print(f"And the rate of interest is {rate}% p.a.!")
print(f"While the time is {time} years!")

total = round((principle * pow(1 + rate / 100, time)), 2)
interest_gained = round(total - principle, 2)
print(f"Your total balance after {time} years will be {total:,}!")
print(f"You will earn {interest_gained:,} in {time} years!")
