import data




def take_order():
    """This function takes the order from the user and returns it."""

    while True:
        order = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
        if order in ["espresso", "latte", "cappuccino", "report", "off"]:
            return order
        else:
            print("Invalid input. Please try again.")


def report():
    """This function prints the current resources of the coffee machine."""
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: ${data.resources['money']}")


def check_resources(order):
    """This function checks if there are enough resources to make the order."""
    for ingredient in data.MENU[order]["ingredients"]:
        if data.MENU[order]["ingredients"][ingredient]>data.resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_coins(order):
    print(f"please insert ${data.MENU[order]["cost"]} for your {order}")

    total_money=0

    while True:
        try:
            quarters=float(input("please insert quarters: "))
            total_money+=quarters*0.25
            print(f"${total_money:.2f}")
            break
        except ValueError:
            print("invalid coin, insert again.") 
    while True:       
        try:
            dimes=float(input("please insert dimes: "))
            total_money+=dimes*0.10
            print(f"${total_money:.2f}")
            break
        except ValueError:
            print("invalid coin, insert again.")
    while True:
        try:
            nickles=float(input("please insert nickles: ")) 
            total_money+=nickles*0.05
            print(f"${total_money:.2f}")
            break
        except ValueError:
            print("invalid coin, insert again.")
    while True:
        try:
            pennies=float(input("please insert pennies: "))
            total_money+=pennies*0.01
            print(f"${total_money:.2f}")
            break
        except ValueError:
            print("invalid coin, insert again.")

    total_money=round(total_money,2)

    cost=data.MENU[order]["cost"]

    if cost > total_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_money>cost:
        print(f"“Here is ${round(total_money-cost,1)} dollars in change.")
    return True


def deduct_resources(order):
    for ingredient in data.MENU[order]["ingredients"]:
        data.resources[ingredient]-= data.MENU[order]["ingredients"][ingredient]
    data.resources["money"]+=data.MENU[order]["cost"]
    
def machine():
    """This function runs the coffee machine."""
    stop=False
    while not stop:
        order=take_order()

        if order == "report":
            report()
        elif order == "off":
            stop=True
        else:
            if check_resources(order):
                if calculate_coins(order):
                    deduct_resources(order)
                    print( f"Here is your {order}. Enjoy!")




machine()


# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5

#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
