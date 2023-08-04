import random

print("Welcome to the Number Guessing Game!/nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(number_of_attempts):
    number = random.randint(1, 100)
    attempts = number_of_attempts
    game_on = True
    while game_on:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Congratulations! You guessed the number! :)")
            game_on = False
        elif guess < number:
            print("Too low.")
            attempts -= 1
            if attempts == 0:
                print("Sorry, your outta attempts, you've lost...")
                game_on = False
        elif guess > number:
            print("Too high.")
            attempts -= 1
            if attempts == 0:
                print("Sorry, your outta attempts, you've lost...")
                game_on = False

if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)