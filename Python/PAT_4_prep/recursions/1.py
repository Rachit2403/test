#factorials
n = int(input())
def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)
res = factorial(n)
print(res)