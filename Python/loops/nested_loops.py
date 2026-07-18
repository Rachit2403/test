rows = int(input("Enter the number of rows: "))
while rows <= 0:
    print("Please enter a positive number!")
    rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
while columns <= 0:
    print("Please enter a positive number!")
    columns = int(input("Enter the number of columns: "))

symbol = input("Enter the symbol required: ")
while not len(symbol) == 1:
    print("Please enter a single character!")
    symbol = input("Enter the symbol required: ")   
for x in range (rows):
    for y in range (columns):
        print(symbol, end="")
    print()