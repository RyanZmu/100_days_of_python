# Loops
# For Loop
fruits: list = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")

# Exercise: Find average height - Write a program that calculates the average student height from a List of heights
print("Finding the average height!")

student_heights: list = input("Enter three heights!").split()

# Turns each number str into an int
# Use range so n = 0 and so forth, otherwise n will equal 123 on first iteration; n = first array value with range
student_height_total: int = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    student_height_total += student_heights[n]

# Calculate and display average
student_height_average: int = int(student_height_total / len(student_heights))
print(f"The average height for the class is {student_height_average}")

# Exercise: Find the High Score - Calculate the highest score from a List of scores. No max or min functions allowed
print("Find the high score!")
score_list: list = input("Enter Scores").split()

highest_score: int = 0
# Unlike in JS where n would be the index value, in py it is the actual value of score_list[i] each iteration unless
# using range
for n in range(0, len(score_list)):
    score_list[n] = int(score_list[n])
    if score_list[n] > highest_score:
        highest_score = score_list[n]

print(f"The highest score is: {highest_score}!")

# Range
# one through 10
# third parameter can say what to step by (by 2, by 3, etc)
for number in range(1, 11, 3):
    print(number)

# Adding sum from 1 to 100
total: int = 0
for number in range(1, 101):
    total += number
print(total)

# Exercise: Add the sum of all even numbers from 1 to X based on user input. If x = 100, 2 would be first even number
target_number: int = int(input("Enter a number to get the sum of all even numbers starting at 1\n"))

sum_of_numbers: int = 0
for number in range(1, target_number + 1):
    if number % 2 == 0:
        sum_of_numbers += number

print(sum_of_numbers)
