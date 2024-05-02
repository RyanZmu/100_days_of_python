"""
CSV weather data exercise
"""
# with open(file="csv_map_usa_game/weather_data.csv",mode="r") as weather_data:
#     data = weather_data.readlines()

# # Format weather data
# formatted_data = []
# for item in data:
#     new_data =

# print(data)

# Instead of above, use csv module
# import csv

# # Alot of work - use Pandas next
# with open(file="csv_map_usa_game/weather_data.csv",mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(data)
# print(temperatures)

import pandas

# Read csv in one line
data = pandas.read_csv(filepath_or_buffer="./csv_map_usa_game/weather/data/weather_data.csv")

print(data)
print(data["temp"])

# Print the panda dataframe
# The sheet = dataframe
print(type(data))

# Print a panda series
# Equivlant to a row,list
print(type(data["temp"]))

# Turn the csv file into a Dict - :O
dict_data = data.to_dict()
print(dict_data)

# Turn rows (Series) into a list
temp_list = data["temp"].to_list()
print(temp_list)

# Get average temp
num_of_temps = len(temp_list)
total = sum(temp_list)
average_temp = total / num_of_temps

# Avoid the work above by just using the Series.mean() method
print(data["temp"].mean())

print(average_temp)

# Get max value of temps using Series method
max_temp = data["temp"].max()
print(max_temp)

# Can use dot accessor for column keys - case sensitive
print(data.temp)

# Get Data in rows - access data and then data.day
# Entire row of data
print(data[data.day == "Monday"])


# FInd What day has the max temp
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)

# Get monday's temp converted to Celsius - [0] to drop the 0 from output
monday_temp = data[data.day == "Monday"].temp[0]

# Convert
to_celsius = (monday_temp - 32) / 1.8
print({"celsius":to_celsius})


# Create a dataframe from scratch
data_dict = {
    "students": ["fred", "jim", "jill"],
    "scores": [45, 23, 70]
}

student_data = pandas.DataFrame(data_dict)
print(student_data)

# Create a CSV with the data above
student_data.to_csv("./csv_map_usa_game/weather/data/new_csv.csv")

