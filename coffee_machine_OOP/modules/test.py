students = [
    {"name": "Frank",
     "major": "Science",
     "gpa": 4.0},

    {"name": "Jill",
     "major": "Medical",
     "gpa": 3.0},

    {"name": "Jim",
     "major": "Business",
     "gpa": 2.5},
]

# Find Frank GPA
majors = []
for student in students:
    majors.append(student["major"])

print(majors)
