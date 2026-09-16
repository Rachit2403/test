capitals = {"USA": "Washington DC", 
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"}
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Washington D.C."})
capitals.pop("China")
capitals.popitem() #removes the last entry
print(capitals)
for key in capitals.keys():
    print(key)
for val in capitals.values():
    print(val)
for key, val in capitals.items():
    print(f"{key} : {val}")