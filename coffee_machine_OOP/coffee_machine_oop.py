"""
Create a coffee machine using OOP

Make each into modules, bring all modules into this page and make a coffee_maker object

1. Print report (receipt)
2. Check resources
3. Process coins
4. Check transaction success
5. Make Coffee

"""
import sys
from modules.menu import Menu, MenuItem
from modules.coffee_machine import CoffeeMachine

# Create classes
menu = Menu()
coffee = CoffeeMachine()

machine_on: bool = True


def machine_prompts():
    global machine_on

    print("Welcome to the coffee machine! Make your Selection below!")
    print(f"Here is our menu! \n {menu.getAllItems()}")

    coffee_desired: str = input("Which coffee would you like?").lower()

    if coffee_desired == 'off':
        machine_on = False
        machine_off()

    orderCoffee(coffee_ordered=coffee_desired)


def orderCoffee(coffee_ordered):
    global menu, coffee

    # Find coffee user requested
    coffee_order= menu.orderCoffee(coffee_ordered)

    # Make coffee
    if coffee_order:
        coffee.makeCoffee(coffee_order)
        

# For vending machine workers!
def machine_off():
    print("Shut off override activated! Powering down...")
    sys.exit()


# initial prompt
while machine_on:
    machine_prompts()
