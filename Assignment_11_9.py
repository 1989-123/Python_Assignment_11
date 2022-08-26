"""
Write a python script to print binary equivalent of a
given decimal number. (do not use bin() method) 
"""

x, y, i, c = 84, " ", 1, 0
while x:
    y = y + str(x % 2)
    x //= 2
    i *= 10
print("Binary is:",int(y[::-1]))
