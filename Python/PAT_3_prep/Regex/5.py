import re
a = "The date is 07-10-2026"
date = re.search(r"(\d{2})-(\d{2})-(\d{4})", a)
print("The date is:", date.group(0))
print("The day is:", date.group(1))
print("The month is:", date.group(2))
print("The year is:", date.group(3))