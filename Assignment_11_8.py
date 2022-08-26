# Write a python script to calculate sum of digits of a given number

x = 123652
s = 0
while x:
    s = s + x % 10
    x //= 10
print("Sum of digit is:",s)
