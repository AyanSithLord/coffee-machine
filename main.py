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
resources["cost"] = 0
is_on = True
while is_on == True:
    order = input("Hello What Coffee Would you like (espresso, latte, cappuccino)?: ").lower()
    if order == "espresso":
        print("please insert coins")
        coins = {"quarter": 0.25,
                 "nickel": 0.05,
                 "dime": 0.10,
                 "penny": 0.01, }
        Number_of_quarters = int(input("Whats the Number of quarters: "))
        Number_of_dimes = int(input("Whats the Number of Dimes: "))
        Number_of_nickels = int(input("Whats the number of Nickels: "))
        Number_of_pennies = int(input("Whats The Number of Pennies: "))
        total_quarters = coins["quarter"] * Number_of_quarters
        total_dimes = coins["dime"] * Number_of_dimes
        total_nickels = coins["nickel"] * Number_of_nickels
        total_pennies = coins["penny"] * Number_of_pennies

        Money_paid = total_nickels + total_pennies + total_dimes + total_quarters
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        Espresso_Change = Money_paid - 1.5
        if Money_paid < 1.5:
            print("Sorry You dont have enough money to buy this")
        elif Money_paid > 1.5:
            print(f"Here is your Change: ${Espresso_Change}")
            resources["cost"] += 1.5
        if resources["water"] >= 50 and resources["coffee"] >= 18 and Money_paid >= 1.5:
            print("Here is your espresso. Enjoy! ☕")
    elif order == "report":
        print(resources)
    elif order == "cappuccino":
        print("please insert coins")
        coins = {"quarter": 0.25,
                 "nickel": 0.05,
                 "dime": 0.10,
                 "penny": 0.01, }
        Number_of_quarters = int(input("Whats the Number of quarters: "))
        Number_of_dimes = int(input("Whats the Number of Dimes: "))
        Number_of_nickels = int(input("Whats the number of Nickels: "))
        Number_of_pennies = int(input("Whats The Number of Pennies: "))
        total_quarters = coins["quarter"] * Number_of_quarters
        total_dimes = coins["dime"] * Number_of_dimes
        total_nickels = coins["nickel"] * Number_of_nickels
        total_pennies = coins["penny"] * Number_of_pennies

        Money_paid = total_nickels + total_pennies + total_dimes + total_quarters

        Cappuccino_Change = Money_paid - 3.0
        if Money_paid < 3.0:
            print("Sorry You dont have enough money to buy this")
        elif Money_paid > 3.0:
            print(f"Here is your Change: ${Cappuccino_Change}")
            resources["cost"] += 3.0
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100 and Money_paid >= 3.0:
            print("Here is your cappuccino. Enjoy! ☕")
        if resources["water"] < 200:
            print("Sorry We dont have enough water")
        elif resources["coffee"] < 24:
            print("Sorry we dont have enough coffee")
        elif resources["milk"] < 100:
            print("Sorry we dont have enough milk")
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100
    elif order == "latte":
        print("please insert coins")
        coins = {"quarter": 0.25,
                 "nickel": 0.05,
                 "dime": 0.10,
                 "penny": 0.01, }
        Number_of_quarters = int(input("Whats the Number of quarters: "))
        Number_of_dimes = int(input("Whats the Number of Dimes: "))
        Number_of_nickels = int(input("Whats the number of Nickels: "))
        Number_of_pennies = int(input("Whats The Number of Pennies: "))
        total_quarters = coins["quarter"] * Number_of_quarters
        total_dimes = coins["dime"] * Number_of_dimes
        total_nickels = coins["nickel"] * Number_of_nickels
        total_pennies = coins["penny"] * Number_of_pennies

        Money_paid = total_nickels + total_pennies + total_dimes + total_quarters

        latte_change = Money_paid - 2.5
        if Money_paid < 2.5:
            print("Sorry You dont have enough money to buy this")
        elif Money_paid > 2.5:
            print(f"Here is your Change: ${latte_change}")
            resources["cost"] += 2.5
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 150 and Money_paid >= 2.5:
            print("Here is your latte. Enjoy! ☕")
        if resources["water"] < 250:
            print("Sorry We dont have enough water")
        elif resources["coffee"] < 24:
            print("Sorry we dont have enough coffee")
        elif resources["milk"] < 150:
            print("Sorry we dont have enough milk")
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150

    elif order == "off":
        is_on = False
    else:
        print("invalid input try again. Maybe you spelt something wrong")