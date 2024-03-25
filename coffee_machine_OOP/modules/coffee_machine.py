import sys


class CoffeeMachine:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 500,
        }

        self.canMakeCoffee = True


    def makeCoffee(self, coffee_type):
        if coffee_type.ingredents['water'] > self.resources['water']:
            self.canMakeCoffee = False
            print('Not enough water!')
            print(f"Sorry we are all out of {coffee_type.name}!")
            self.refill()

        elif coffee_type.ingredents['milk'] > self.resources['milk']:
            self.canMakeCoffee = False
            print('Not enough milk!')
            print(f"Sorry we are all out of {coffee_type.name}!")
            self.refill()

        elif coffee_type.ingredents['coffee'] > self.resources['coffee']:
            self.canMakeCoffee = False
            print('Not enough coffee!')
            print(f"Sorry we are all out of {coffee_type.name}!")
            self.refill()

        else:
            self.resources['water'] -= coffee_type.ingredents['water']
            self.resources['milk'] -= coffee_type.ingredents['milk']
            self.resources['coffee'] -= coffee_type.ingredents['coffee']

            print(f"Pouring your {coffee_type.name} coffee!")
        return self.canMakeCoffee


    def reportResources(self):
        report = self.resources
        return report


    def refill(self):
        refill_prompt = input("Refill? Y/N")

        if refill_prompt.lower() == 'y':
            self.resources = {
                "water": 300,
                "milk": 200,
                "coffee": 500,
            }
            print("Machine has been refilled! Proceed with the coffee!")
        else:
            sys.exit()