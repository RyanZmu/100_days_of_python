"""
Calculator App:
Ask user for a number
Ask for an Operator
 - Output a list of valid operators
Ask for a second number
Calculate
Ask user if they wish to continue
    - Do you want to calculate starting from the last total
    - Or do you want a new calculation?
"""

operators: list = ["+", "-", "*", "/", "%", "**"]
user_continue: bool = False
result: int = 0


def calculation(first_int, second_int, operator):
    global result, user_continue
    match operator:
        case "+":
            result = first_int + second_int
        case "-":
            result = first_int - second_int
        case "*":
            result = first_int * second_int
        case "/":
            result = first_int / second_int
        case "%":
            result = first_int % second_int
        case "**":
            result = first_int ** second_int

    answer_str: str = f"{first_int} {operator} {second_int} = {result}"

    print(answer_str)
    continue_input: str = input(f"Type 'y' to continue calculating with {result}, "
                                f"or type 'n' to start a new calculation\n")

    if continue_input.lower() == "y":
        user_continue = True
        user_inputs()
    else:
        user_continue = False
        user_inputs()


def user_inputs():
    global result
    if not user_continue:
        first_number: float = float(input("What is the first number?\n"))
        print(operators)
        operator_requested: str = input("Pick an operation\n")
        second_number: float = float(input("What is the second number?\n"))

        calculation(first_int=first_number, second_int=second_number, operator=operator_requested)
    else:
        operator_requested: str = input("Pick an operation\n")
        second_number: float = float(input("What is the second number?\n"))

        calculation(first_int=result, second_int=second_number, operator=operator_requested)


# Start program
user_inputs()
