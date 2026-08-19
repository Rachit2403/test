n = int(input())
m = int(input())
old_base = 50
old_rate = 5
young_base = 30
young_rate = 3
old_allowance = 50 + 5*n
young_allowance = 30 + 3*m
print(f"Older child allowance is: Rs. {old_allowance}")
print(f"Younger child allowance is: Rs. {young_allowance}")
print(f"Total allowance is: {old_allowance + young_allowance}")