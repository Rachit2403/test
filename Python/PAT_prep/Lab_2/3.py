A = int(input())
N = int(input())
binary = bin(A)[2:0]
req_binary = binary[-N:]
result = int(req_binary, 2)
print(f"Result: {result}")