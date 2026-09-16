a1 = int(input())
a1_4 = (a1)**4
a2_4 = (a1 + 1)**4
a3_4 = (a1 + 2)**4
a4_4 = (a1 + 3)**4
avg = (a1_4 + a2_4 + a3_4 + a4_4)/4
prod = (a1)*(a1 + 3)
constant = avg - prod
print(constant)