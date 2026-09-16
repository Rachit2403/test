capitals = {"USA": "WASHINGTON DC", 
            "INDIA": "NEW DELHI", 
            "CHINA": "BEIJING",
            "RUSSIA": "MOSCOW"}
askey = input("Which country's capital do you want to know? (q to quit): ").upper()
while askey != "Q":

    if capitals.get(askey):
        print(f"The capital of {askey} is {capitals.get(askey)}")
        askey = input("Which country's capital do you want to know? (q to quit): ").upper()
        
    else:
        print(f"We do not have {askey} in out database.")
        askey = input("Which country's capital do you want to know? (q to quit): ").upper()
else:
    print("Thank you!")