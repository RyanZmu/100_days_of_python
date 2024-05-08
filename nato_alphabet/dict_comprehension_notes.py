"""
Dict Comprehension - a way of creating a dict using shorten syntax
Syntax

list to dict
new_dict = {new_key:new_value for item in list}

dict to new_dict with conditional
new_dict = {new_key:new_value for (key,value) in dict.items() if condition}
"""
names = ["Barry", "Ryan", "Jerry"]

"""
Make a dict placing scores next to each name 1-100
"""
from random import randint
student_scores = {name:randint(1,100) for name in names}
print(student_scores)

"""
Make a new dict from student_scores and call it passed_scores, all students score > 60 have passed
Remeber .items() to get all items in the dict
"""
passed_scores = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_scores)

"""
Using Dict Comprehension, create a dict called result that takes each word in the sentence and calculates number of letters
NO LOOPS

Do not change the sentence var directly
"""
# sentence = input("Type a sentence")

# # Get a dict of word:letter_counts from list
# results = {word:len(word) for word in sentence.split()}
# print(results)

"""
Use Dict Comprehension to create a dict called degrees Fahrenheit
to convert temp_c into temp_f use
(temp_c + 9/5)) + 32 = temp_f

input a dict with day:temp
"""
weather_c = {"Monday":12, "Tuesday":23, "Wednesday": 20, "Thursday": 30, "Friday":8}
print(weather_c)

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)


"""
Iterating over Panda DataFrames
"""
import pandas

student_dict = {
    "student": ["Barry", 'Ryan', "Jerry"],
    "score": [32, 89, 94]
}

# Normal for loop to loop over a dict
for (key, value) in student_dict.items():
    print(key, value)

# Create dataframe
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through data frame - this is not useful really
for (key, value) in student_data_frame.items():
    print(value)

# Panda has it's own builtin loop called iterrows
# Loops through each row instead of columns like above
for (index, row) in student_data_frame.iterrows():
    print(index, row)
    print(row.student)
    if row.student == "Ryan":
        print(row.student)
