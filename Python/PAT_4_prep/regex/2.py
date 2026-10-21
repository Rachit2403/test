import re
text = "there are 4 cats, 12 bananas and 328947 moles of atoms in this container"
pattern = r"\d+"
#match = re.search(pattern, text)
#match = re.findall(pattern, text)
#match = re.sub(pattern, "a number of", text)
match = re.split(pattern, text)
print(match)