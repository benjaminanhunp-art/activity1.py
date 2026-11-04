number = int(input("Enter your number: "))

result = "Yes its prime"

for i in range(2,number):
    if number % i == 0:
        result = "It isnt a prime"
        break

print(result)