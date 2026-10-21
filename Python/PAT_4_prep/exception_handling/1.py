a = int(input())
def divider(x):
    try:
        res = 5/x
    except:
        res = "Whoa! Can't divide by 0, you know..."
        print(divider(a))
    finally:
        s = res
    return f"{res}"
print(divider(a))