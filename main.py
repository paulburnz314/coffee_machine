from coffee_menu import Menu
from coffee_maker import CoffeeMaker
from money_tracker import MoneyTracker

if __name__ == "__main__":
    running = True
    coffee_bot = CoffeeMaker()
    coffee_bot_menu = Menu()
    money_bank = MoneyTracker()

    while running:
        """ get_items will return drink names and prices """
        print("\nWelcome to coffee-bot ☕")
        print(f"I serve the following hot drinks: {coffee_bot_menu.get_items()}")
        order_code = input("Enter the first letter of the menu item to make an order: ").lower()

        if order_code == 'off':
            running = False
        elif order_code == 'report':
            coffee_bot.report()
            money_bank.report()
        else:
            if not coffee_bot_menu.find_drink(order_code):
                print("Enter an item from the menu.")
            else:
                drink_choice = coffee_bot_menu.find_drink(order_code)
                if coffee_bot.is_resource_sufficient(drink_choice):
                    if money_bank.make_payment(drink_choice.cost):
                        coffee_bot.make_coffee(drink_choice)
                else:
                    print("Try ordering something else.")