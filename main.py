from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

coffee_machine_on = True
while coffee_machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        coffee_machine_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        choosen_item = menu.find_drink(choice)
        if choosen_item:
            if coffee_maker.is_resource_sufficient(choosen_item) and money_machine.make_payment(choosen_item.cost):
                coffee_maker.make_coffee(choosen_item)