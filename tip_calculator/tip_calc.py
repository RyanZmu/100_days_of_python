# Get total from user
total_bill: float = float(input("What is the total bill?\n $"))
total_people: int = int(input("How many people are splitting the bill?\n"))
tip_percentage: int = int(input("How much do you want to tip?\n"))

# Get tip owed by each person
tip: float = (total_bill / total_people) * (tip_percentage / 100)

# Find total each should pay when tip is added
total_for_each: float = round((total_bill / total_people), 2) + tip

# Format solution for getting only the 2nd decimal place in a float - study this format method
formatted_total = "{:.2f}".format(total_for_each)

print(f"Each person should pay ${formatted_total}")
