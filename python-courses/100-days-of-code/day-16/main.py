from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffe_maker=CoffeeMaker()
money_machine=MoneyMachine()

def safe_input(obect_type,prompt,valid_list=None):
    """This method takes input safely from the user. useful for errors"""
    while True:
        try:
            value=obect_type(input(prompt))
            if valid_list is None or value in valid_list:
                return value
            print("please give a valid name")
        except ValueError:
            print("please give a valid name")



while True:
    valid_commands = ["off", "report"]
    valid_commands.extend(menu.get_items().rstrip("/").split("/"))

    order=safe_input(str,f"What would you like? ({menu.get_items().rstrip("/")}): ", valid_commands)

    if order == "off":
        print("The machine is shutting down..")
        break
    if order =="report":
        coffe_maker.report()
    if order in valid_commands:
        if coffe_maker.is_resource_sufficient(menu.find_drink(order)):
            money_machine.make_payment(menu.find_drink(order).cost)
            coffe_maker.make_coffee(menu.find_drink(order))