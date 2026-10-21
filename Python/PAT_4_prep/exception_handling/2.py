try:
    x = int(input())
    def divider(a):
        try:
            num = int(a)
            res = 10/num
        except(ZeroDivisionError):
            res = "Oi, you dum-dum?"
        finally:
            t = f"Result: {res}"
        print(t)
    divider(x)
except(ValueError):
    print("Oi, you dum-dum?")