"""
NATO Alphabet Project

Convert words into the NATO alphabet
RYAN
ROMEO - YANKEE - ALPHA - NOVEMBER

Use list and dict comprehension
"""
import pandas

nato_alphabet = pandas.read_csv(filepath_or_buffer="./nato_alphabet/nato_alphabet.csv")

# Turn list into a dict showing letter and phrase using iterrows
# {"A":"ALpha", "B", "Bravo"}
nato_dict = {row.Letter: row.Phrase for (index, row) in nato_alphabet.iterrows()}
print(nato_dict)


# Find the letter of the word within the nato_dict
def generate_phonetic():
    try:
        word = input("Type a word \n").upper()
        results = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(results)

generate_phonetic()