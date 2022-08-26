"""
Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)
"""
x, y, i, c = 43, " ", 1, 0
while x:
    y = y + str(x % 8)
    x //= 8
    i *= 10
print("Octal is:",int(y[::-1]))
