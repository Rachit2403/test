import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\\.(com|edu|net)"
enter = input("")
if re.search(pattern, enter):
    print("valid")
else:
    print("invalid")