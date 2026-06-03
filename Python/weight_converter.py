unit = input("Choose unit (K or L): ").upper()
weight = float(input("Enter your weight: "))
if weight <=0:
    print("Invalid weight.")
elif unit == "K":
    weight = round((weight * 2.205), 2)
    unit = "Lbs."
    print(f" Your weight is {weight} {unit}")
elif unit == "L":
    weight = round((weight / 2.205), 2)
    unit = "Kgs."
    print(f" Your weight is {weight} {unit}")
else:
    print("Unit is invalid.")
