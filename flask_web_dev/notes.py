# # Decorators
# # As a function that will give additional functiionality to a function
#
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# # Functions are First class objects; can be passed as arguments like do_something(add(1,2,))
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# # pass in a function for calc_function
# results = calculate(add, 1, 2)
# print(results)

# Nested Functions

# def outer_function():
#     print("outer")
#
#     # Scope means nested is only accessible inside this function
#     def nested_function():
#         print("nested")
#
#     nested_function()
#
# outer_function()

# Functions can be returned from other functions
# def outer_function():
#     print("outer")
#
#     # Scope means nested is only accessible inside this function
#     def nested_function():
#         print("nested")
#
#     return nested_function
#
#
# inner_function = outer_function()  # Returns the nested function
# inner_function()  # Runs the inner function

# Decorators - A function that wraps another function
# import time
#
# # Instead of needing to play time.sleep(2) in each function, just calling the decorator and function will handle it
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("bye")
#
# # No delay so triggered right away
# def say_greeting():
#     print("How are you?")


# Decorators can grab another function and gibes it some more functionality - like above with adding a delay
# Non-Syntactic Sugar version of a decorator - using @ is easier to read at a glance and is preferred
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

# Advanced Decorators
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = True
#
# # Make a decoration function to check that the user_is_logged_in == True before every function runs
# # Pass in arguments to decorators
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:  # Use args[] to grab first positional argument
#             function(args[0])  # If logged in, run the function for the user
#         else:
#             print("User not logged in")
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"this is {user.name}'s new blog post")
#
#
# new_user = User(name="Ryan")
# create_blog_post(new_user)

# Exercise - Create a decorator that returns the function name of arguments given
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
