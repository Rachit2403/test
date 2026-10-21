#newton's sqrt
n = int(input())
def rooter(n):
    approx = 0.5*n
    better = 0.5*(approx+n/approx)
    while approx != better:
        approx = better
        better = 0.5*(approx+n/approx)
    return approx
print(rooter(n))