name = input("Enter your name: ")
if name == "":
    print("Type in your name dumbo!")
else:
    print(f"Hello there, {name}!")
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("Age invalid.")
else:
    print("You must be 18+ to apply.")
response = input("Would you like some food? (Y/N): ")
if response == "Y":
    print("Then go have some!")
elif response == "N":
    print("Fine! No food for you!")