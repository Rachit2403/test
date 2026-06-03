# X is condition else Y


num1 = float(input("Enter number A: "))
num2 = float(input("Enter number B: "))
if num1 == num2:
    print("Both numbers are equal!")
else:
    max_num = num1 if num1 > num2 else num2
    print(f"The greater number is {round(max_num)}!")