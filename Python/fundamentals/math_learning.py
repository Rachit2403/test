import math
print("Hello there!")
name = input("What is your name? ")
print(f" So {name}, you want to know the hypotenuse of a triangle, when you give me two of its sides? ")
a = float(input(f"{name}, give me side A: "))
b = float(input(f"{name}, give me side B: "))
c = int(math.sqrt(pow(a, 2) + pow(b, 2)))
print(f"The hypotenuse of the triangle is {c}, {name}.")