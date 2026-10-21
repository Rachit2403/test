import re
text = "Contact me at contact@example.com"
pattern = r"([a-zA-Z0-9_%+-]+)@([a-zA-Z]+)\.([a-zA-Z]{2,})"
out = re.sub(pattern, "[EMAIL]", text)
print(out)