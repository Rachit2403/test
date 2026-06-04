temp = float(input("What is the temperature?: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()
if unit == "C":
    if temp < -273.15:
      print("Invalid temperature.")
    else:
      temp = round((temp * 9) / 5 + 32, 1)
      print(f"The temperature in Fahrenheit is {temp}!")    
    
elif unit == "F":
    if temp < -459.67:
       print("Invalid temperature.")
    else:
       temp = round((temp - 32) * 5 / 9, 1)
       print(f"The temperature in Celsius is {temp}!")
else:
   print("Type either C or F for unit.")
