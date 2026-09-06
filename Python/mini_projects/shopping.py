items = []
prices = []
total = 0

while True:
    item = input("Enter the item name (q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of one {item}: $"))
        items.append(item)
        prices.append(price)
print("------YOUR BILL------")
for item in items:
    print(item, end=", ")
for price in prices:
    total += price
print()
print(f"Your total billing amount is: {total}")