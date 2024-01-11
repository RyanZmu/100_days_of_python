#  Conditionals
#  Exercise - Carnival ride height check
print("Welcome to the rollercoaster!")
height: int = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!\n")
else:
    print("Sorry, you are too short to ride :(\n")

# Exercise - Find if the number is even or odd
number: int = int(input("Enter a number\n"))

if number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")

# Nested conditionals
# Exercise - Check height and how much a ticket costs based on age
print("Welcome to the rollercoaster Pt.2!")
height: int = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!\n")
    age: int = int(input("What is your age?"))
    if age <= 12:
        print("Your ticket is $5")
    elif age <= 18:
        print("Your ticket costs $7")
    else:
        print("Your ticket costs $10")
else:
    print("Sorry, you are too short to ride :(\n")


# Exercise - BMI calculator 2.0
print("Welcome to BMI calculator 2.0")
height: float = float(input("What is your height in meters, e.g., 1.55?\n"))
weight: int = int(input("What is your weight in kg, e.g., 72?\n"))

bmi: float = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"BMI: {bmi} You are underweight!")
elif 18.5 < bmi < 25:
    print(f"BMI: {bmi} You are normal weight!")
elif 25 < bmi < 30:
    print(f"BMI: {bmi} You are slightly overweight!")
elif 30 < bmi < 35:
    print(f"BMI: {bmi} You are obese!")
else:
    print(f"BMI: {bmi} You are clinically obese!")

# Exercise - Leap year, Write a program that works out whether a given year is a leap year. Normal year has 365
# Days with an extra day in Feb.
# On every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder

# My Solution - Boolean changing constantly could be confusing
print("Check if a given year is a leap year!")
year = int(input("Enter a year and see if it is a leap year!\n"))
is_leap_year: bool = False

if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
    if year % 400 == 0:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")

# Lesson's Solution
year = int(input("What year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Ask guests for a photo in our ticket logic and add $3
print("Welcome to the rollercoaster Pt.2!")
height: int = int(input("What is your height in cm?\n"))
bill: int = 0

if height >= 120:
    print("You can ride the rollercoaster!\n")
    age: int = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 10
        print("Adult tickets are $10")

    wants_photo = input("Do you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3
        print("That will be $3")
    else:
        print("Ok we won't take your photo")

    print(f"Your total bill is {bill}")
else:
    print("Sorry, you are too short to ride :(\n")

# Exercise - Python Pizza: Find out the price of a pizza based on size and toppings
# S = 15 M = 20 L = 25 Pep on S = 2 Pep on M or L = 3 ExCheese = 1
print("Welcome to Python Pizzeria")

# Inputs
size: str = input("What size do you want? S, M or L?\n")
add_pepperoni: str = input("Do you want pepperoni? Y or N\n")
extra_cheese: str = input("Do you want extra cheese? Y or N\n")

total_price: int = 0

# Sizes
if size == "S":
    total_price += 15
elif size == "M":
    total_price += 20
elif size == "L":
    total_price += 25
else:
    print("Please enter a valid size!")

# Pepperoni
if add_pepperoni == "Y" and size == "S":
    total_price += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    total_price += 3
else:
    print("No pepperoni!")

# Cheese
if extra_cheese == "Y":
    total_price += 1
else:
    print("No extra cheese, please!")

print(f"Your total is: {total_price}")


# Logical Operators
# and or and not

# Exercise - Love Calculator: Write a program that tests compatibility between two people
print("Love calculator is calculating your score...")
name1: str = input("What is your name?\n")
name2: str = input("What is their name?\n")

# Check how many times the letters TRUE appear in the name
combined_names: str = name1 + name2
lower_names: str = combined_names.lower()

t_count: int = lower_names.count("t")
r_count: int = lower_names.count("r")
u_count: int = lower_names.count("u")
e_count: int = lower_names.count("e")

true_count: int = t_count + r_count + u_count + e_count

# Check for LOVE letters
l_count: int = lower_names.count("l")
o_count: int = lower_names.count("o")
v_count: int = lower_names.count("v")
e_count2: int = lower_names.count("e")

love_count: int = l_count + o_count + v_count + e_count2

# Add the two digits together as string and then make an int for conditionals
total_love_score_str: str = str(true_count) + str(love_count)
total_love_score: int = int(total_love_score_str)

# Conditions
if total_love_score < 10 or total_love_score > 90:
    print(f"Your Compatibility Score is: {total_love_score} You two go together like coke and mentos")
elif 40 <= total_love_score <= 50:
    print(f"Your Compatibility Score is: {total_love_score} you are alright together")
else:
    print(f"Your Compatibility Score is: {total_love_score} maybe consider not dating")

# Doing multi-line strings - literal
print('''
Hey
I
AM
Multi-lined!
''')
