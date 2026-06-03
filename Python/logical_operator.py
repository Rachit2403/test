temp = float(input("Enter temperature: "))
weather = input("The weather is (Cloudy/Sunny): ")

if temp > 10 or temp < 40:
    print("Temperature is alright!")
else:
    print("Temperature is harsh!")

if weather == "Sunny":
    print("The weather is sunny!")
else:
    print("The weather is cloudy!")