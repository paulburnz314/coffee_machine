class CoffeeMaker:
    def __init__(self):
        """ Attributes of the machine that makes the coffee, stored resources """
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """ Method to print a report of resource levels. """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """ Method returns True when order can be made, False if ingredients are insufficient.
            Must pass to it the drink type. """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """ Method deducts the required ingredients from the resources.
            Then 'makes' the coffee recipe. """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
