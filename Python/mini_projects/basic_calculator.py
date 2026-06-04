operator = input("Enter the operator required ( + - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    if num2 == 0:
       print("Cannot divide by 0!")
    else:
       result = num1 / num2
       print(round(result, 2))
else:
    print(f"Selected operator is invalid!")
