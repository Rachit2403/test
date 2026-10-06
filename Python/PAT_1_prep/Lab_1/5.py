float_str = input("")
integer = int(input())
real_part, imag_part = map(float, input().split())
#mapping implements one function/action on all the elements included in it, like here it made all input values float. Also, split() splits the input at all whitespaces.
float_value = float(float_str)
print(float_value)
print(integer)
print(complex(real_part, imag_part))