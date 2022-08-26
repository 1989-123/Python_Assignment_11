# Write a python script to calculate sum of first N odd natural numbers

n = int(input("Enter a natural number: "))
i = 1
s = 0
while i <= n:
    s = s + i * 2 - 1
    i += 1
print("Sum of odd number is:",s)
