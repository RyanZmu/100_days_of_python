import random
import my_module

# Random module
# Random number between 1 and 10
random_int: int = random.randint(1, 10)
print(random_int)

# Split code into modules when things get complex
# Using custom module
print(my_module.greeting)

# Random floats number between 0 and 1 by default (never 1)
random_float: float = random.random()

# Multiply by a number to make a range 0 - 5
random_float_five: float = random.random() * 5
print(random_float)

# Exercise: Heads or Tails coin flip
print("Heads or Tails?")
coin_heads: str = "Heads"
coin_tails: str = "Tails"

coin_flip: int = random.randint(0, 1)

if coin_flip == 0:
    print(coin_tails)
else:
    print(coin_heads)

# Lists
fruits: list = ["apples", "grapes"]
print(fruits)

states_of_america = ["Michigan", "New York", "Maine"]
print(states_of_america)

# Changing data in a list
states_of_america[-1] = "Florida"
print(states_of_america)

# Adding to a list
states_of_america.append("California")
print(states_of_america)

# Add a list of items to another list
states_of_america.extend(["Idaho", "Delaware"])
print(states_of_america)

# Exercise: Select a random name from a list of names and this person pays the bill
# choice() is not allowed
print("Banker Roulette, Who will pay?")

names_string: str = input("Enter names - separated by a space\n")
names = names_string.split()
names_length = len(names)

# -1 to avoid an out of range array index
random_int: int = random.randint(0, names_length - 1)

# Picks name based on random index number
person_who_pays: str = names[random_int]

# print({"names": names}, {"names_length": names_length}, {"random_int": random_int})
print(f"{person_who_pays} has to pay the bill! Sorry {person_who_pays}!")

# Nested lists
fruits: list = ["Apples", "Grapes"]
veggies: list = ["Potatoes", "Spinach"]

# Combine two lists into one list
dirty_dozen: list = [fruits, veggies]
print(dirty_dozen)

# Exercise: Treasure Map - Write a program that marks an X on a map based on user input
# Update nested list with an X
print("Treasure Map")
line_x_axis: list = ["A", "B", "C"]
line1: list = [" ", " ", " "]
line2: list = [" ", " ", " "]
line3: list = [" ", " ", " "]

map_lists: list = [line1, line2, line3]
position: str = input("Where do you want to hide the treasure? x-axis: A,B,C and y-axis: 1,2,3\n")
print("Hiding your treasure!")

letter: str = position[0].lower()
abc: list = ["a", "b", "c"]
letter_index: int = abc.index(letter)  # 0 return
number_index: int = int(position[1]) - 1  # 2 return
map_lists[number_index][letter_index] = "X"  # [2][0]

print(f"{line1}\n{line2}\n{line3}")
