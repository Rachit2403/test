#sum of n terms
n = int(input())
l = list(map(int, input().split()))
def adder(a):
    total = 0
    for i in l:
        total += i
    return total
print(adder(l))