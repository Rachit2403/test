import re
a = "My phone number is 70692-13567"
pattern = r"\d{5}-\d{5}"
match = re.search(pattern, a)
print(match.group())