item = input("What would you like to buy? ")
rate = float(input("What is the rate of the item? "))
quant = int(input("How many of those items do you want to buy? "))
total = quant * rate
print(f"You have bought {quant} of the {item}/(s)")
print(f"Your total bill is of ${total}")
