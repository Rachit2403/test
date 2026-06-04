food = input("Enter a food that you like (q to quit): ")
while not food == "q":
    print(f"You like {food}!")
    food = input("Enter another food that you like (q to quit): ")
else:
    print("Okay, bye!")