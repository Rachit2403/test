import re
i = input()
def emailsplicer(i):
    pattern = r"^([a-zA-Z0-9_%+-]+)@([a-zA-Z0-9.-]+)\.[a-zA-Z0-9]{2,}$"
    match = re.search(pattern, i.strip())
    if match:
        username = match.group(1)
        domain = match.group(2)
        print("Your username is:", username)
        print("Your domain is:", domain)
    else:
        print('Invalid email')
emailsplicer(i)