import math
print("Hello there!")
name = input("What is your name? ")
print(f" So {name}, you want to know the hypotenuse of a triangle, when you give me two of its sides? ")
a = float(input(f"{name}, give me side A: "))
b = float(input(f"{name}, give me side B: "))
c = int(math.sqrt(pow(a, 2) + pow(b, 2)))
print(f"The hypotenuse of the triangle is {c}, {name}.")
# a + b : addition between a and b
# a - b : subtracts b from a
# a * b : multiplies a to b
# a / b : divides a by b
# a ** b : raises a to bth power
# a % b : gives remainder received by dividing a by b
# round(a, b) : rounds a to b digits after the decimal; if b is left untyped, it is rounded off to the nearest integer
# abs(a) : gives absolute values of integers
# pow(a, b) : raises a to its bth power
# max(a, b, c) : gives the max value among a, b and c
# min(a, b, c) : gives the min value among a, b and c
# math.sqrt(a) : gives the square root of a
# math.pi : gives the value of pi
# math.ceil : rounds the decimal containing number to the closest higher integer
# math.floor : rounds the decimal containing number to the closest lesser integer