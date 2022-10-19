MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coins = [["quarters", 0.25], ["dimes", 0.10],
         ["nickles", 0.05], ["pennies", 0.01]]
machine_money = 0


def check_resources(drink):
    for ingredient in MENU[drink]['ingredients']:
        for resource in resources:
            if resources[resource] < MENU[drink]['ingredients'][ingredient]\
                    and resource == ingredient:
                print(f"Sorry, there is not enough {resource}")
                return False
    return True


def insert_money(cost):
    total = 0
    # ask the user to insert each of the coins
    for coin in coins:
        choice = int(input(f"How many {coin[0]}?"))
        total += choice * float(coin[1])
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(total - cost, 2)
    print(f"Here is ${change} in change")
    return True


def generate_report(machine_money):
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(machine_money)


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        exit()

    elif choice == "report":
        generate_report(machine_money)

    elif check_resources(choice):
        print("Insert coins.")
        if insert_money(float(MENU[choice]["cost"])):
            # if enough money is inserted, add to the machine money,
            # subtract the ingredients from the resources and serve the drink
            machine_money += MENU[choice]["cost"]
            for ingredient in MENU[choice]['ingredients']:
                resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
            print(f"Enjoy your {choice} ☕")
