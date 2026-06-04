#:.(num)f = round off to 'num' digits
#:(num) = allocate 'num' spaces
#:0(num) = allocate 'num' spaces and provide 0 padding for the remaining spaces
#:< = left alignment
#:> = right alignment
#:^ = center alignment
#:+ = provide '+' sign before positive numbers and leave negative ones as is
#:= = place sign to leftmost place
#: = leave space for positive and put '-' for negative
#:, = spaces between digits in large numbers
price1 = 24659826.91626812
price2 = -7892681.7892
price3 = 76257.7706827
print(f"Price 1 is {price1:>,.2f}!")
print(f"Price 2 is {price2:>,.2f}!")
print(f"Price 3 is {price3:>,.2f}!")
