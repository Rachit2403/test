# instead of typecasting as integer, use "//" instead of just "/".

import time
duration = (input("Enter the duration of countdown in seconds: "))
tim = int(duration)
while tim <=0:
    print("Time can't be negative or zero, dumbo!")
    duration = int(input("Enter a possible value of time in seconds: "))

    print("Please enter a valid duration!")
    duration = int(input("Enter a valid duration of countdown in seconds: "))
while tim < 1:
    print("Enter a longer duration!")
    duration = int(input("Enter a valid duration of countdown in seconds: "))
    tim = int(duration)
for x in range(tim, 0, -1):
    seconds = x % 60
    minutes = int(x // 60) % 60
    hours = int(x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")