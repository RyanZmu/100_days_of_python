"""
Great Squirrel Census of 2018!

- Create a CSV called squirrel_count
- Pull out Fur colors
 - How many grey squirrels, cinnamon and black squirrels
- Build a new data frame for these counts (Fur Color, Count)
"""
import pandas

# Get the all of the data
squirrel_data = pandas.read_csv(filepath_or_buffer="./csv_map_usa_game/great_squirrel_census/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240502.csv")

# Get fur colors
squirrel_fur_data = squirrel_data["Primary Fur Color"]

black_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
gray_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

# Make a dict of colors and turn into a csv
squirrel_colors = {
    "Furs": ["Black", "Gray", "Cinnamon"],
    "Counts": [black_fur, gray_fur, cinnamon_fur]
}

squirrel_fur = pandas.DataFrame(squirrel_colors)
print(squirrel_fur)

squirrel_fur.to_csv("./csv_map_usa_game/great_squirrel_census/data/squirrel_fur.csv")


