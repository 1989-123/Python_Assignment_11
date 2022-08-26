# Write a python script to calculate sum of squares of first N natural numbers

n = int(input("Enter a natural number: "))
i = 1
s = 0
while i <= n:
    s = s + i ** 2
    i += 1
print("Sum of squares of first N natural number is:",s)
