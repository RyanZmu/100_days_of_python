# Print function
print("Hello World!")

# nested string
print("print('what to print')")

# Multi line string with newline char
print("Hello World\nHow are you?")

# Spaced string
print("Hello" + " Ryan!")
print("Hello" + " " + "Ryan!")

############################

# Input function
input("What is your name?")

# Nest input inside of print - returns Hello Name!
print("Hello " + input("What is your name?") + "!")

# Exercise: Output number of characters in a name
# Course Solution
print(len(input("What is your name?")))

# My solution
name: str = input("What is your name?")
print(len(name))

# Sync variable assignment order
name = "Ryan"
print(name)

name = "Jack"
print(name)


# Exercise: Write a program that switches the values store in the variables a and b
# Example input: 10 23 output: 23 10
a: str = input()
b: str = input()

# Use a third variable to store original value of a
c: str = b

b = a
a = c

print("a: " + a)
print("b: " + b)