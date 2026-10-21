import re

text = "Dad bought 123 apples and 456 oranges for Anna"

def convert(m):
    w = m.group(0)
    # Rule 1: Exactly 3 digits -> sum them
    if w.isdigit() and len(w) == 3:
        return str(sum(int(d) for d in w))
    # Rule 2: Starts and ends with same letter -> reverse
    if w[0].lower() == w[-1].lower():
        return w[::-1]
    # Rule 3: Otherwise keep unchanged
    return w

result = re.sub(r'\b\w+\b', convert, text)
print(result)