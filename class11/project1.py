number_picked = int(input("Guess the secret number: "))
secret = 25
lives = 5

for i in range(1,lives+1):
    if number_picked != secret:
        print("Thats wrong, you have", lives-1, "left")

        
        