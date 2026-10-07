import re
a = "Your pin is 3041"
hide = re.sub(r"\d", "X", a)
print(hide)