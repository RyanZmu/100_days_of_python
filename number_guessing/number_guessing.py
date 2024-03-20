import random

'''
Number Guessing Game!

Think of a number 1-100
Choose Difficulty Easy or Hard
Show number of guessing attempts left out of 5

Make a guess:
    Tell user if number is too high or too low
Make a guess - 1 attempt
    If less than 0 attempts left and wrong, end game
If correct, output user wins

Easy = 10 attempts
Hard = 5 attempts

'''

RANDOM_NUMBER: int = random.randint(1, 100)
end_game = False

print(RANDOM_NUMBER)

print(f"WELCOME To The Number Guessing Game!\n"\
      f"I'm thinking of a number between 1 and 100!\n"\
     )


def number_guessing_game():

    game_difficulty: str = input("Choose a difficulty: Easy (10 attempts) or Hard (5 attempts)\n")
    user_guess: int = int(input("Make a guess!:\n"))

    if game_difficulty.lower() == "easy":
        attempts_left = 10
    elif game_difficulty.lower() == "hard":
        attempts_left = 5
    else:
        "Error! Invalid difficulty!"

    if attempts_left >= 0:
        if user_guess > RANDOM_NUMBER:
            attempts_left - 1
            print(f"Too high! You have {attempts_left} attempts left!")
        elif user_guess < RANDOM_NUMBER and attempts_left:
            attempts_left - 1
            print(f"Too Low! You have {attempts_left} attempts left!")
        elif user_guess == RANDOM_NUMBER:
            print(f"CORRECT THE NUMBER IS {RANDOM_NUMBER} YOU WIN!!!")
    elif attempts_left < 0:
        end_game = True
        print(f"No Attempts Left! You Lose! The Number was {RANDOM_NUMBER}")


while not end_game:
    number_guessing_game()
