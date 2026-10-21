l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search = int(input())
for i in range(len(l)):
    if (l[i] == search):
        print("Element found at position:", i+1)
        break
    else:
        print("Not at position number", i+1)