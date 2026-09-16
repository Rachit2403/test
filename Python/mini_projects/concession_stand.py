menu = {"Popcorn": 220,
        "Samosa": 50,
        "Tea": 55,
        "Coke": 60,
        "Sprite": 50,
        "Pepsi": 60,
        "Burger": 180,
        "Pizza": 200}
cart = []
total = 0
print("----------------------")
for key, val in menu.items():
    print(f"{key:10} : {val:.2f}")
print("----------------------")
while True:
    food = input("Select an item (Q to quit): ").capitalize()
    if food == "Q":
        print("Thank you!")
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food, end = ", ")
print()
print(f"Total: {total:.2f}")