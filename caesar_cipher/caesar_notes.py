# Functions with inputs
import math


# Create a function called greet()
# Write three print statements and call it


def greet():
    print("Hello")
    print("Everyone")
    print("!!!")


greet()


# Give functions inputs/parameters
def greet_with_name(name):
    print(f"Hello {name}!")


greet_with_name("Ryan")


# Positional vs Keyword arguments
# More than one input
def greet_with(name, location):
    print(f"Hello {name} you are in {location}")


greet_with("Ryan", "Michigan")


# Positional arguments
# to prevent data being fed to a function out of order we can use keywords
def my_function(a, b, c):
    print(a, b, c)


# Call function with explicit keywords
my_function(a="H", c="E", b="Y!")

# Call greet_with using keyword arguments
greet_with(name="Ryan", location="Michigan")


# Paint area Calculator exercise
def paint_calc(height, width, cover):
    """ Paint Area Calculator
     You are painting a wall with these instructions:
     - 1 can of paint can 5 sq meters
     - Given a random height and width of wall, calculate how many cans of paint you need to buy
     - Height = 2, Width = 4, Coverage = 5
     - number of cans = (2 \\* 4) / 5 = 1.6
     - Round up
    """
    cans_needed: int = math.ceil((height * width) / cover)
    return print(cans_needed)


# Testing
test_h: int = int(input("Height"))
test_w: int = int(input("Width"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
