
import random
secret_number = random.randint(1, 50)
attempts = 5

while attempts > 0:

    guess = int(input("\nEnter your guess: "))
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        break

    else:
        print("Wrong guess! Try again.")

        difference = abs(secret_number - guess)

        if difference <= 2:
            print("Hot!")
        elif difference <= 5:
            print("Warm!")
        elif difference <= 10:
            print("Cold!")
        else:
            print("Ice cold!")

    attempts = attempts - 1

    print("Lives left: ", end="")

    for i in range(attempts):
        print("heart", end=" ")

    print()
if guess != secret_number:
    print("\nno hearts left GAME OVER!")
    print("The secret number was:", secret_number)

