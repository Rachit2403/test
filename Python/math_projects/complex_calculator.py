operator = input("Choose your operator (+, -, *, /, **, %): ")
while operator not in ["+", "-", "*", "/", "**", "%"]:
    print("Enter a valid operator!")
    operator = input("Choose your operator (+, -, *, /, **, %): ") 
num1 = float(input("Provide the first number: "))
num2 = float(input("Provide the second number: "))
if operator == "+":
        print(f"Your required number is: {num1 + num2}!")
elif operator == "-":
        print(f"Your required number is {num1 - num2}!")
elif operator == "*":
        print(f"Your required number is {num1 * num2}!")
elif operator == "/":
        while num2 == 0:
               print("Cannot divide by 0!")
               num2 = float(input("Provide the second number: "))
        print(f"Your required number is {num1 / num2}!")
elif operator == "**":
        print(f"Your required number is {num1 ** num2}!")
elif operator == "%":
        while num2 == 0:
               print("Cannot divide by 0!")
               num2 = float(input("Provide the second number: "))
        print(f"Your required number is {num1 % num2}!")