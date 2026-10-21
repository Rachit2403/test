#fibonacci (n)
n = int(input())
def fib(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    r = fib(a-1) + fib(a-2)
    return r
terms = [fib(i) for i in range(n)]
print(*terms)