l = float(input())
t = float(input())
h = float(input())
vol_brick = 0.2 * 0.1 * 0.05
vol_wall = l*t*h
num_bricks = round(vol_wall / vol_brick)
print(f"Number of bricks needed: {num_bricks: ,}")
