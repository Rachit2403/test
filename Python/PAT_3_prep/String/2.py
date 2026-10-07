#center(width, fillchar)
#ljust(width, fillchar)
#rjust(width, fillchar)
#zfill(width)
#capitalize()
#title()
#swapcase()
#upper()
#lower()

#<width
#>width
#^width

a = "I love pizza"
b = 25000
c = "25000"
print(a)
print(b)
print(a.center(25, '*'))
print(a.ljust(25, '*'))
print(a.rjust(25, '*'))
print(c.zfill(10))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print("----------------------------------------")
print(f"{b:<10}")
print(f"{b:>10}")
print(f"{b:^10}")