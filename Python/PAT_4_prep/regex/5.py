import re
text = "Today's date is 21-10-2026 and yesterday's date was 20-10-2026 and there are 4 cats, 12 bananas and 328947 moles of atoms in this container."
pattern = r"[a-zA-Z',.\s]+"
match = re.sub(pattern, " ", text)
print(match)