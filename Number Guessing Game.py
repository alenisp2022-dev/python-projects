# Number Guessing Game
# Author: Alen Ispiryan
# Description: User tries to guess a randomly generated number with hints and limited attempts.

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()