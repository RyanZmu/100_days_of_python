import random
# Password Generator!
# Create a Password Generator that creates a password based on the users desired amount of letters, symbols and numbers
# Constants
NUM_LIST: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LETTER_LIST: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS_LIST: list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# Inputs
user_letters: int = int(input("How many letters should your password have?"))
user_numbers: int = int(input("How many numbers should your password have?"))
user_symbols: int = int(input("How many symbols should your password have?"))

# Create a list of possible chars to be used in final password
char_pool: list = []

# These loops would work best as a function, however follow the lesson and just user loops for now
# Find x amount of random numbers - range = number of times to repeat
for number in range(0, user_numbers):
    char_pool += random.choice(NUM_LIST)

# Find x amount of random letters
for letter in range(0, user_letters):
    char_pool += random.choice(LETTER_LIST)

# Find x amount of random symbols
for symbol in range(0, user_symbols):
    char_pool += random.choice(SYMBOLS_LIST)

# Reorder the char_pool to make a random password
random.shuffle(char_pool)
final_password: str = "".join(char_pool)

print(f'Your password is {final_password}')
