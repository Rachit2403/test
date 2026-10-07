s = {1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 3, 3, 2, 7, 8, 10, 9}
#add: adds one element specified in the ()
#update: add a collection of elements specified in the ()
#discard: removes the element specified in the () [doesn't give error if it does not work]
#remove: removes the element specified in the ()
print(s)
s.add(11)
print(s)
s.update([13, 14])
print(s)
s.discard(25)
print(s)
s.remove(11, 13)
print(s)