import re
a = "I have 4 pizzas, 4 burgers and 7 cold drinks"
matches = re.findall(r"\d", a)
print(matches)