#exponents (n^m)
n = int(input())
m = int(input())
def power(n, m):
    if m == 1:
        return n
    if m == 0:
        return 1
    else:
        res = n*power(n, m-1)
        return res
print(power(n, m))