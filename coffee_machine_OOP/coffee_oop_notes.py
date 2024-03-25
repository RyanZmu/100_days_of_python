from turtle import Turtle, Screen
from prettytable import PrettyTable

# Object class names are in PascalCase
# car = carBlueprint()

# Create a turtle named Timmy using classes
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('red', 'green')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.title("Messing with OOP!")
my_screen.exitonclick()

# Create a table object and try it out
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

print(table)
