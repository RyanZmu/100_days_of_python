"""
Hangman Game!
"""
import random

word_list: list = ["balloon", "skyscraper", "bunk", "ice cream"]
hangman_chars: list = ["O", "|", "\\", "/", "/", "\\"]

# Pick a word randomly and check user input against the word
word_chosen: str = random.choice(word_list)

#  Create blank spaces for each letter
word_as_blanks: list = []

for letter in range(0, len(word_chosen)):
    if word_chosen[letter] != " ":
        word_as_blanks += word_chosen[letter].replace(word_chosen[letter], "_")
    else:
        word_as_blanks += word_chosen[letter].replace(word_chosen[letter], " ")

# User score tracking
guesses_left: int = 6


# Functions
def user_score():
    global guesses_left
    if guesses_left > 0:
        guesses_left -= 1
    return guesses_left


# If player guess is correct, enter that letter in the correct space. Find the index where the letter is.
def add_letter_to_blank(user_guess):
    global word_chosen, word_as_blanks
    for index in range(0, len(word_chosen)):
        if word_chosen[index] == user_guess:
            word_as_blanks[index] = user_guess


def check_player_win():
    global word_as_blanks, guesses_left
    player_win_check: bool = False
    player_lose_check: bool = False
    word_blank_str: str = "".join(word_as_blanks)

    # Check if no blank spaces remain
    if word_blank_str.find("_") == -1 and guesses_left > 0:
        player_win_check = True
    elif guesses_left <= 0:
        player_lose_check = True
    return player_win_check, player_lose_check


hangman_index: int = -1
build_hangman: str = ""


def is_user_correct(user_guess):
    global hangman_index, build_hangman

    if word_chosen.count(user_guess) != 0:
        print(f"Correct! {user_guess} is in the word!")
        add_letter_to_blank(user_guess)
    else:
        print(f"Sorry! {user_guess} is not in the word!")
        user_score()

        hangman_index += 1

        if hangman_index <= len(hangman_chars) - 1:
            build_hangman += hangman_chars[hangman_index]

            print(build_hangman)


# User input for guessing
def prompt_user():
    global guesses_left

    # Print the board initially
    print("".join(word_as_blanks))

    while guesses_left >= 0:
        user_guess = input("What letter do you guess?")
        is_user_correct(user_guess)

        # Update the board
        print("".join(word_as_blanks))

        player_win = check_player_win()[0]
        player_lose = check_player_win()[1]

        # Check for win/lose before giving next prompt
        if player_win:
            print("You Win!")
            return
        elif player_lose:
            print("You Lose")
            return


# Start the game
prompt_user()
