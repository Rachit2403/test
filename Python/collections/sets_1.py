fruits = {"apple", "banana", "orange", "coconut"}
print(len(fruits))
print("pineapple" in fruits)
# As sets are unordered, indexing is meaningless, hence provides errors when used on sets
fruits.add("pineapple")
fruits.remove("coconut")
fruits.pop()
print(fruits)