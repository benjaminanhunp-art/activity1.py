base = int(input("Enter the base number: "))
n = int(input("Enter the power: "))

result = 1

for i in range(n):
    result = result * base

print("Answer =", result)