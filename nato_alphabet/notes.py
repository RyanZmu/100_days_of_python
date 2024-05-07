# # List Comprehension

# numbers = [1,2,3]
# new_list = []

# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# # Instead write it as to add 1 to each number
# new_list = [n + 1 for n in numbers]

# # Get each letter
# name = "Ryan"
# new_name = [letter for letter in name]
# print(new_name)


# # Double the value of the range
# new_range = [n * 2 for n in range(1,5)]
# print(new_range)

# # Conditional List Comprehension
# names = ["Barry", "Ryan", "Jerry"]
# new_names = [n for n in names if n is not "Barry" and len(n) == 4]
# print(new_names)


# # Exercise: Write a list comprehension to create a new list called squared_numbers.
# # Square all numbers in a list
# numbers_to_square = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [number * number for number in numbers_to_square]
# print(squared_numbers)


# # Exercise: Filtering Odd Numbers
# list_of_strings = input().split(",")
# odd_numbers = [int(number) for number in list_of_strings if int(number) % 2 != 0]

# print(odd_numbers)


# Exervise: Data Overlap
# Read the contents of both file1 and file2, create a list of common numbers
with open(file="./nato_alphabet/files/file1.txt") as list_1:
    list_1_results = [int(item.replace("\n","")) for item in list_1]
    print(list_1_results)

with open(file="./nato_alphabet/files/file2.txt") as list_2:
    list_2_results = [int(item.replace("\n","")) for item in list_2]
    print(list_2_results)

common_numbers_my_solution = [number for number in list_1_results if list_2_results.count(number) >= 1]
print(common_numbers_my_solution)

common_numbers_course_solution = [number for number in list_1_results if number in list_2_results]
print(common_numbers_course_solution)


