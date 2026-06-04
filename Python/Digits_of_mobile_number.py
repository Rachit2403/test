# [start : end : step]
mob_num = input("Enter your mobile number: ")
ffd = mob_num[:4]
lfd = mob_num[-4:]
rev = mob_num[::-1]
if len(mob_num) < 10 or len(mob_num) > 10:
    print("Invalid mobile number!")
elif not mob_num.isdigit():
    print("Invalid mobile number!")
else:
    print(f"Your mobile number is {mob_num}")
    print(f"The first four digits of your mobile number are {ffd}******!")
    print(f"The last four digits of your mobile number are ******{lfd}!")
    print(f"The reverse of your mobile number is {rev}!")