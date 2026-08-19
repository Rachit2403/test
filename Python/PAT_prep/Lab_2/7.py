n = int(input())
binary = bin(n)[2:]
req_binary = binary[-4:].zfill(4)
print(req_binary)