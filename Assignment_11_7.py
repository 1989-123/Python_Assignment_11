# Write a python script to count digits in a given number

x = 1238732
c, i = 0, 1
while x:
    y = x %10
    x //= 10
    c += 1
print("Digit in given number is:",c)
