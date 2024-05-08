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

word = input("Type a word \n").upper()

# Find the letter of the word within the nato_dict
results = [nato_dict[letter] for letter in word]
print(results)
