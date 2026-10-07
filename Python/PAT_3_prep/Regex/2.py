import re
a = "My phone number is 70692-13567"
match = re.search(r"\d{5}-\d{5}", a)
print(match.group())