import re
email = input()
match = re.search(r"^([a-zA-Z0-9._]+)@([a-zA-Z.-]+\.[a-zA-Z]{2,})$", email)
print("Your mail is:", match.group())
print("Your username is:", match.group(1))
print("Your domain is:", match.group(2))