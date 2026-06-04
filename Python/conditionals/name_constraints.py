username = input("Enter a username: ")
if len(username) > 12:
    print("A username cannot have more than 12 characters!")
elif len(username) < 4:
    print("A username cannot have less than 4 characters!")
elif not username.find(" ") == -1:
    print("A username cannot have spaces!")
elif not username.isalpha():
    print("A username cannot have numeric values!")
else:
    print(f"Welcome, {username}")
