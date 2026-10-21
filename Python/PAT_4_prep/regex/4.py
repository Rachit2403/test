import re
nums = "Today's date is 21-10-2026 and yesterday's date was 20-10-2026"
pattern = r"\b\d{2}-\d{2}-\d{4}"
match = re.search(pattern, nums)
print(match.group())