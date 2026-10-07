import re
say = input()
pattern = r"^([a-zA-Z0-9._-]+)@([a-zA-Z0-9._-]+)\.([a-zA-Z]){2,}$"
match = re.search(pattern, say)
print("Your email is", match.group())
print("Your username is", match.group(1))
print("Your domain is", match.group(2))