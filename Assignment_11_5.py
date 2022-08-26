# Write a python script to calculate sum of first N even natural numbers

n = int(input("Enter a natural number: "))
i = 1
s = 0
while i <= n:
    s = s + i * 2
    i += 1
print("Sum of even number is:",s)
