"""
Create a coffee machine using OOP

Make each into modules, bring all modules into this page and make a coffee_maker object

1. Print report (receipt)
2. Check resources
3. Process coins
4. Check transaction success
5. Make Coffee

"""
from modules.menu import Menu
from modules.coffee_machine import CoffeeMachine
from modules.money_machine import MoneyMachine

# Create classes
menu = Menu()
coffee = CoffeeMachine()
payment_processing = MoneyMachine()

# Track so if False, will stop prompting user
machine_on: bool = True


def machine_prompts():
    global machine_on

    print("Welcome to the coffee machine! Make your Selection below!")
    print(f"Here is our menu! \n {menu.getAllItems()}")

    coffee_desired: str = input("Which coffee would you like?").lower()

    if coffee_desired == 'off':
        machine_on = False
        machine_off()
    elif coffee_desired == 'report':
        getReport()
    else:
        orderCoffee(coffee_ordered=coffee_desired)
    return


def orderCoffee(coffee_ordered):
    # Find coffee user requested
    coffee_order = menu.orderCoffee(coffee_ordered)

    # Work out asking for payment
    if coffee_order != None:
        payment = input(f'Payment owed ${coffee_order.cost} \n Please enter coin amounts in following order with commas [Q,D,N] \n')

        # Process transaction via Money Machine module - this assumes user followed q,d,n format correctly
        coffee_transaction = payment_processing.transaction(coffee_bought=coffee_order,payment=payment)

        # Confirm transaction success and resouces are available, brew coffee.
        if coffee_transaction and coffee.makeCoffee(coffee_order):
            print(f"Pouring your {coffee_order.name} coffee!")
    return


def getReport():
    #  get a report of machine resources
    resources_report = coffee.reportResources()
    print(resources_report)
    return


# For vending machine maintainance!
def machine_off():
    coffee.machine_shutdown()
    return


# initial prompt
while machine_on:
    machine_prompts()
