class MenuItem:
    def __init__(self, type_of_coffee, cost, water, milk, coffee) -> None:
        self.name = type_of_coffee
        self.cost = cost
        self.ingredents = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    def __init__(self) -> None:
        self.menuItems = [
            MenuItem(type_of_coffee="cappuccino", cost=2.10, water=100, milk=50, coffee=80),
            MenuItem(type_of_coffee="latte", cost=3.50, water=80, milk=80, coffee=90),
            MenuItem(type_of_coffee="espresso", cost=4.50, water=80, milk=100, coffee=110),
        ]

    
    def getAllItems(self):
        coffees = ""
        for item in self.menuItems:
            coffees += f"{item.name} ${item.cost}/ "
        return coffees


    def orderCoffee(self, coffee_type):
        for item in self.menuItems:
            if item.name == coffee_type:
                coffeeOrdered = item
                return coffeeOrdered
        print("Sorry that is not available!")
        

# print(Menu().getAllItems())
# print(Menu().orderCoffee('latte'))