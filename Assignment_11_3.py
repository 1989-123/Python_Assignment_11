# Write a python script to calculate sum of cubes of first N natural numbers

n = int(input("Enter a natural number: "))
i = 1
s = 0
while i <= n:
    s = s + i ** 3
    i += 1
print("Sum of cubes is:",s)
