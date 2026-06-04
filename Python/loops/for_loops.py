# for "VARIABLE" in range ( , )
# for "VARIABLE" in reversed(range ( , ))
# for "VARIABLE" in ----( , , )
# continue : skips a particular value/string
# break : ignores the particular value/string and the following strings.

for x in range (1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range (1, 21):
    if x == 13:
        break
    else:
        print(x)