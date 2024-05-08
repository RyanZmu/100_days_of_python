"""
*args *kwargs playground

Default and keywords
**kw and **args lets you have default arguments for functions that dont need specifying every function call

When you see a argument that looks like this: arg=... it means there is a default value for that argument
Can set what arguments are required and what ones are optional and are defaulted

This will allow you to set default arguments and require arguments with each function
"""
# Make function to add any amount of numbers
# **args puts the arguments into a tuple - can access by index
# Also known as unlimited positional arguments
def add(*args):
    # Print an arg - second arg
    print(args[1])

    total = 0
    for n in args:
        total += n
    return total

print(add(1,10,2))

# **kwargs - double **
# kwargs makes a dict
def calculate(n, **kwargs):
    print(kwargs)

    # Print a kwarg
    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)

#  Can use kwargs["name_of_argument"] to create optional args for the class
class Car:
    def __init__(self, owner, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.owner = owner

# Note there are only **kwargs when hovering over the var
# Will fail if a kwarg is missing
# Using .get above will avoid this fail and just return None
# This allows us to make optional keyword arguments
my_car = Car(make="Nissan", owner="Ryan", model="GT-R")
print(my_car.owner)
print(my_car.make)
print(my_car.model)
