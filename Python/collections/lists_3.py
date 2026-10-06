fruits = ["apple", "banana", "orange", "coconut"]
fruits[0] = "pineapple"
fruits.append("strawberry")
fruits.remove("orange")
fruits.insert(0, "mango") #variable.insert(index, "string")
fruits.sort()
fruits.reverse() #reverses the order in list, not in reverse alphabetical order
print(fruits.index("mango"))
print(fruits.count("banana"))
print(fruits)