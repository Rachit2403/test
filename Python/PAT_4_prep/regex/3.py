import re
text = "there are 4 cats, 12 bananas and 328947 moles of atoms in this container"
pattern = r"[a-zA-Z,]+"
match = re.search(pattern, text)
#match = re.findall(pattern, text)
print(match)