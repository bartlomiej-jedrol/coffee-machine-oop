from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, coffee=18, milk=0, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
coffee_maker_001 = CoffeeMaker()
money_machine_001 = MoneyMachine()


is_on = True
while is_on:
    choice = input(f" What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_001.report()
        money_machine_001.report()
    elif choice in menu.get_items().split(sep="/"):
        product = menu.find_drink(choice)
        if coffee_maker_001.is_resource_sufficient(
            drink=product
        ) and money_machine_001.make_payment(cost=product.cost):
            coffee_maker_001.make_coffee(order=product)
    else:
        is_on = False
