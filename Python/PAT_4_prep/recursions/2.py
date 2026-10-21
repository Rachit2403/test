#fibonacci
n = int(input())
def fibonacci(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    r = fibonacci(a-1) + fibonacci(a-2)
    return r
r = fibonacci(n)
print(r)