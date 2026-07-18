#len(xyz) = gives number of characters in the variable xyz
#xyz.find("a") = gives first position of character 'a' in the variable xyz. [PS: Starts with 0]
#xyz.rfind("a") = gives last position of the character 'a' in the variable xyz. [PS: Starts with 0]
# find and rfind give result = "-1" if the specified character is not in the variable
#xyz.capitalize() = capitalises the first letter of the string
#xyz.upper() = makes all string characters uppercase
#xyz.lower() = makes all string characters lowercase
#xyz.isdigit() = gives true/false output for the presence/absence of digits in all placeholders.
#xyz.isalpha() = gives true/false output for the presence/absence of alphabets in all placeholders.
#FOR CAPITALIZE, UPPER, LOWER, ISDIGIT, ISALPHA, WE DO NOT WRITE INSIDE THE BRACKETS, BUT TYPE THE BRACKETS.
#xyz.count("a") = gives the number of occurences of the letter 'a' in the variable.
#xyz.replace("a", "b") = replaces all occurences of the character 'a' with the character 'b'.


#no spaces, no digits, not more than 12 characters.
usrnme = input("Please enter your username: ")
if len(usrnme) > 12:
    print("Username is too long.")
elif len(usrnme) < 3:
    print("Username is too short.")
elif not usrnme.find(" ") == -1:
    print("Your username cannot contain spaces.")
elif not usrnme.isalpha():
    print("Your username must contain only alphabets.")
else:
    print(f"Welcome, {usrnme}!")