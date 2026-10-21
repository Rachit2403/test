divisorcount = []
def countDivisors(n):
    for m in range(1, n):
        res = n / m
        if res%1 == 0:
            divisorCount.append(m)
        else:
            continue
divisorCount = len(divisorcount)
n = int(input())

divisorCount = countDivisors(n, n)

print("Count of divisors:", divisorCount)

if divisorCount % 2 == 0:
    print("Even")
else:
    print("Odd")