import time

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

Money = 0
PENNY = 0.01
DIME = 0.10
NICKEL = 0.05
QUARTER = 0.25


def make_coffee():
    global Money
    global resources
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "espresso" and (
            resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >=
            MENU["espresso"]["ingredients"]["coffee"]):
        penny = int(input("How much penny? "))
        dime = int(input("How much dime? "))
        nickel = int(input("How much dime? "))
        quarter = int(input("How much quarter? "))
        user_coins_sum = (penny * PENNY) + (dime * DIME) + (nickel * NICKEL) + (quarter * QUARTER)
        if user_coins_sum < MENU["espresso"]["cost"]:
            print("Money Refunded sorry the coins are enough")
            make_coffee()
        elif user_coins_sum == MENU["espresso"]["cost"]:
            Money += user_coins_sum
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso enjoy your day")
            make_coffee()
        elif user_coins_sum > MENU["espresso"]["cost"]:
            Money += user_coins_sum
            user_change = user_coins_sum - MENU["espresso"]["cost"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is your coffee and the change {user_change} enjoy your coffee")
            make_coffee()

    elif user_choice == "espresso" and (
            resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] <
            MENU["espresso"]["ingredients"]["coffee"]):
        print("sorry the resources are not enough")
        make_coffee()

    elif user_choice == "latte" and (
            resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=
            MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]):
        penny = int(input("How much penny? "))
        dime = int(input("How much dime? "))
        nickel = int(input("How much dime? "))
        quarter = int(input("How much quarter? "))
        user_coins_sum = (penny * PENNY) + (dime * DIME) + (nickel * NICKEL) + (quarter * QUARTER)
        if user_coins_sum < MENU["latte"]["cost"]:
            print("Money Refunded sorry the coins are enough")
            make_coffee()
        elif user_coins_sum == MENU["latte"]["cost"]:
            Money += user_coins_sum
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print("Here is your espresso enjoy your day")
            make_coffee()
        elif user_coins_sum > MENU["latte"]["cost"]:
            Money += user_coins_sum
            user_change = user_coins_sum - MENU["latte"]["cost"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print(f"Here is your coffee and the change {user_change} enjoy your coffee")
            make_coffee()

    elif user_choice == "latte" and (resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] <
                                     MENU["latte"]["ingredients"]["coffee"] or resources["milk"] <
                                     MENU["latte"]["ingredients"]["milk"]):
        print("sorry the resources are not enough")
        make_coffee()

    elif user_choice == "cappuccino" and (
            resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >=
            MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= MENU["cappuccino"]["ingredients"][
                "milk"]):
        penny = int(input("How much penny? "))
        dime = int(input("How much dime? "))
        nickel = int(input("How much dime? "))
        quarter = int(input("How much quarter? "))
        user_coins_sum = (penny * PENNY) + (dime * DIME) + (nickel * NICKEL) + (quarter * QUARTER)
        if user_coins_sum < MENU["cappuccino"]["cost"]:
            print("Money Refunded sorry the coins are enough")
            make_coffee()
        elif user_coins_sum == MENU["cappuccino"]["cost"]:
            Money += user_coins_sum
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print("Here is your espresso enjoy your day")
            make_coffee()
        elif user_coins_sum > MENU["cappuccino"]["cost"]:
            Money += user_coins_sum
            user_change = user_coins_sum - MENU["cappuccino"]["cost"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print(f"Here is your coffee and the change {user_change} enjoy your coffee")
            make_coffee()

    elif user_choice == "cappuccino" and (
            resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] <
            MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < MENU["cappuccino"]["ingredients"][
                "milk"]):
        print("sorry the resources are not enough.")
        make_coffee()

    elif user_choice == "report":
        print("Generating report......")
        time.sleep(3)
        print(resources)
        make_coffee()

    elif user_choice == "off":
        print("Machine is turning off...")
        time.sleep(4)
        print("Machine can now be maintained")

    elif user_choice == "money":
        print(Money)
        make_coffee()


make_coffee()
