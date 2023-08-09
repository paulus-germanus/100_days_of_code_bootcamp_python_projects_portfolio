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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0,
}


def resource_check(coffee):
    for x in resources:
        if x in MENU[coffee]["ingredients"] and resources[x] < MENU[coffee]["ingredients"][x]:
            print(f"There's not enough {x}.")
            return 0


def resource_depletion(coffee):
    for y in resources:
        if y in MENU[coffee]["ingredients"] and resources[y] > MENU[coffee]["ingredients"][y]:
            resources[y] -= MENU[coffee]["ingredients"][y]


def money_counter(q, d, n, p):
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01
    return (q * quarter) + (d * dime) + (n * nickle) + (p * penny)


machine_on = True

while machine_on:
    coffee_kind = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_kind == "off":
        machine_on = False
    elif coffee_kind == "report":
        for x in resources:
            if x == "water" or x == "milk":
                print(f"{x.capitalize()}: {resources[x]} ml")
            elif x == "coffee":
                print(f"{x.capitalize()}: {resources[x]} g")
            else:
                print(f"{x.capitalize()}: ${resources[x]}")
    elif resource_check(coffee_kind) == 0:
        machine_on = False
    elif coffee_kind == "espresso" or "latte" or "cappuccino":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        full_payment = money_counter(quarters, dimes, nickles, pennies)
        if full_payment == MENU[coffee_kind]["cost"]:
            print(f"Here is your {coffee_kind} ☕️. Enjoy!")
            resources["money"] += MENU[coffee_kind]["cost"]
            resource_depletion(coffee_kind)
        elif full_payment > MENU[coffee_kind]["cost"]:
            print(f"Here is ${round(full_payment-MENU[coffee_kind]['cost'], 2)} in change.\nHere is your {coffee_kind} ☕️. Enjoy!")
            resources["money"] += MENU[coffee_kind]["cost"]
            resource_depletion(coffee_kind)
        else:
            print(f"Sorry, that's not enough. Money refunded. Here's your ${full_payment}.")
