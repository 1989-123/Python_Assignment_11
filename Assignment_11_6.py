# Write a python script to calculate factorial of a given number

n = int(input("Enter a number: "))
f = 1
i = 1
while n >= i:
    f = f * n
    n -= 1
print("Factorial is:",f)
