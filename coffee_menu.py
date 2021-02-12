class MenuItem:
    """ Models each Menu Item.  The Menu class makes a menu list using this.
        I added 'code' so user can simply enter 1st letter of the menu item.
        Definitely a pain testing the code when you have to type cappuccino
        over and over again. """
    def __init__(self, code, name, water, milk, coffee, cost):
        self.code = code
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """ Models the Menu with drinks. Added code."""
    def __init__(self):
        self.menu = [
            MenuItem(code='l', name="Latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(code='e', name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(code='c', name="Cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """ Returns all the names and prices of the available menu items."""
        options = ""
        for item in self.menu:
            options += f"{item.name} ${item.cost:.2f} | "
        return options

    def find_drink(self, order_name):
        """ Searches the menu for a particular drink by code. Returns that item
            if it exists, otherwise returns None. """
        for item in self.menu:
            if item.code == order_name:
                return item
        print("Sorry that item is not available.")
        return False
