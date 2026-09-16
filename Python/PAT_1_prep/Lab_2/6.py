a, b = map(int, input().split())
X = (a**2) + (b**2)
Y = (a+b)*(a - b)+(a*b)
if X == Y:
    result = "equal"
else:
    result = "not equal"
print(f"Left side sum: {X}")
print(f"Right side sum: {Y}")
print(f"The sums are {result}")
