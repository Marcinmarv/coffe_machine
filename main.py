from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_machine =CoffeeMaker()
report = money_machine.report()
print(report)
is_on = True
while is_on:
    chosen = input(f"What do you want to {menu.get_items()} ")
    if chosen == "off":
        is_on = False
    elif chosen == "report":
        money_machine.report()
        coffee_machine.report()
    else:
        drink = menu.find_drink(chosen)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

