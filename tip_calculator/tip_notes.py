# Data types
# String
print("Hello"[4])

# Integer
print(324 + 5)
# Way to write integers with , formatting
print(123_456_789)

# Float
print(3.14)

# Booleans
True
False

# type conversion (casting) and type check
print(type("String"))
print(type(123))

# Int to str
converted_int = str(10)
print(converted_int)

a = str(123)
print(type(a))

# Prints 70100
print(str(70) + str(100))

# Exercise - Write a program that adds the digits in a 2-digit number. Ex: 35 --> 3 + 5 = 8

# First solution
two_digit_number: str = input("Type a two digit number\n")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Making it more readable, try to do less on one line moving forward
two_digit_number: str = input("Type a two digit number\n")

first_digit: int = int(two_digit_number[0])
second_digit: int = int(two_digit_number[1])

print(first_digit + second_digit)

# Math Operators
print(3 - 5)  # Subtraction
print(3 + 5)  # Addition
print(3 * 2)  # Multiplication
print(6 / 3)  # Division, note that division is always a float - use Floor Division // for whole number
print(4 ** 2)  # Exponents

# PEMDAS
# Remember M and D are same level of priority same with A and S
# Evaluates the first one to the left like below, 3*3 and then 3/3
print(3 * 3 + 3 / 3 - 3)  # Comes out to 7.0 (float due to division)

# Challenge - Make the above equation output 3 instead of 7
print(3 * (3 + 3) / 3 - 3)  # Use () to increase priority of 3 + 3

# Exercise - BMI Calculator, Write a program that calculates the BMI from a user's height and weight
height: float = float(input("What is your height in feet? ie: 5.6 for 5'6\"\n"))
weight: int = int(input("What is your weight in lbs? ie: 125\n"))

bmi_value: int = int(weight / height ** 2)

print(bmi_value)

# Rounding to second decimal place
print(round(8 / 3, 2))

# Floor division - drops decimal places
print(8 // 3)

# Increments and Decrements based on previous values
result = 4 / 2
result /= 2
print(result)  # Would equal 1 because result /= 2 is like saying result/2 -> 2/2 = 1

score = 0
# User scores go up by 1
score += 1
print(score)

# F strings - template literals basically
print(f"your score is {score}")
