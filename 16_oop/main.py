from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        exit()
    if choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            print("Insert coins.")
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
