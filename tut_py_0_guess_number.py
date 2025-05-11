import random

secret_number = random.randint(1, 10)

print("Guess the number between 1 and 10!")

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try guessing higher.")
    else:
        print("Too high! Try guessing lower.")
