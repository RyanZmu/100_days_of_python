# Dictionaries

programming_dict: dict = {
    "Bug": "Error that prevents a program from running correctly",
    "Function": "Code we can easily call over and over again",
}
print(programming_dict["Bug"])

# Add new items to dict
programming_dict["Loop"] = "The action of doing something over and over again"
print(programming_dict)

# Empty dict
empty_dict: dict = {}

# Wipe an existing dict
# programming_dict = {}
# print(programming_dict)

# Edit existing items in a dict
programming_dict["Bug"] = "A moth in your computer"
print(programming_dict)

# Loop through a dict
for key in programming_dict:
    print(key)
    print(programming_dict[key])

# Grading program
# Take in a list of students and values, loop through and interpret each score
# Make a new dict called student_grades
# 91-100 = "Outstanding", 81-90 = "Exceeds Expectations", 71-80 "Acceptable", 70 or lower = "Fail"
student_scores: dict = {
    "Harry": 100,
    "Jill": 87,
    "Hank": 54,
    "Frank": 67,
    "Bill": 71,
}


def scores_to_grades(scores):
    student_grades: dict = {}

    for key in scores:
        if scores[key] >= 91:
            student_grades[key] = "Outstanding"
        elif 81 <= scores[key] <= 90:
            student_grades[key] = "Exceeds Expectations"
        elif 71 <= scores[key] <= 80:
            student_grades[key] = "Acceptable"
        elif scores[key] <= 70:
            student_grades[key] = "Fail"

    return student_grades


print(scores_to_grades(scores = student_scores))

# Nesting Dicts
travel_log: list = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Dijon"],
     "total_visits": 12
     },
    {
     "country": "Germany",
     "cities_visited": ["Berlin"],
     "total_visits": 2
     },
]

# Loop and display each city visited
for index in range(0, len(travel_log)):
    print(travel_log[index]["cities_visited"])


# Exercise: Add a new country object to the travel_log list with a function
def add_to_travel(country, cities_visited, total_visits):
    travel_log.append(
     {
        "country": country,
        "cities_visited": cities_visited,
        "total_visits": total_visits
     }
    )


add_to_travel(country="Spain", cities_visited=["Barcelona", "City"], total_visits=31)
print(travel_log)
