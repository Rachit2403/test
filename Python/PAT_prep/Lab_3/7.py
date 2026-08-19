N = int(input())
s = int(input())
S = s / 8
t = N / S
sec = int(t % 60)
min = int(t // 60)
hour = int(t // 3600)
print(f"Downloaad time: {hour} hours, {min} minutes, and {sec} seconds")