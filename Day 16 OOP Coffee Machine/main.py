from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    coffee_kind = input(f"What would you like? ({menu.get_items()}): ").lower()
    if coffee_kind == "off":
        machine_on = False
    elif coffee_kind == "report":
        print(maker.report())
        print(money_machine.report())
    elif maker.is_resource_sufficient(menu.find_drink(coffee_kind)) and money_machine.make_payment(menu.find_drink(coffee_kind).cost):
        maker.make_coffee(menu.find_drink(coffee_kind))
