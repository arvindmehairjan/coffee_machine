from data import MENU, resources

# Money
money = 0.00

# Types of amount money
quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

def calculate_amount():
    print("Please insert coins.")
    amount_quarters = int(input("How many quarters? ")) * quarter
    amount_dimes = int(input("How many dimes? ")) * dime
    amount_nickles = int(input("How many nickles? ")) * nickle
    amount_pennies = int(input("How many pennies? ")) * penny
    return amount_quarters + amount_dimes + amount_nickles + amount_pennies

def calculate_remaining_ingredients(type_coffee, ingredient):
    if type_coffee == "espresso" and ingredient == "water":
        return resources['water'] - MENU[type_coffee]['ingredients']['water']
    elif type_coffee == "espresso" and ingredient == "coffee":
        return resources['coffee'] - MENU[type_coffee]['ingredients']['coffee']
    elif type_coffee == "cappuccino" and ingredient == "water":
        return resources['water'] - MENU[type_coffee]['ingredients']['water']
    elif type_coffee == "cappuccino" and ingredient == "coffee":
        return resources['coffee'] - MENU[type_coffee]['ingredients']['coffee']
    elif type_coffee == "cappuccino" and ingredient == "milk":
        return resources['milk'] - MENU[type_coffee]['ingredients']['milk']
    elif type_coffee == "latte" and ingredient == "water":
        return resources['water'] - MENU[type_coffee]['ingredients']['water']
    elif type_coffee == "latte" and ingredient == "coffee":
        return resources['coffee'] - MENU[type_coffee]['ingredients']['coffee']
    elif type_coffee == "latte" and ingredient == "milk":
        return resources['milk'] - MENU[type_coffee]['ingredients']['milk']

should_continue = True
while should_continue:

    # Prompt user to ask what type of coffee he/she would like
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    list_ingredients = ['water', 'coffee', 'milk']

    # Print current status of coffee machine
    if choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(money, 2)}")
    # Choice espresso
    elif choice == 'espresso':
        total_amount = calculate_amount()
        if total_amount < MENU[choice]['cost']:
            print("Sorry, not enough money.")
        else:
            if resources['water'] > MENU[choice]['ingredients']['water'] and \
                    resources['coffee'] > MENU[choice]['ingredients']['coffee']:
                resources['water'] = calculate_remaining_ingredients(choice, list_ingredients[0])
                resources['coffee'] = calculate_remaining_ingredients(choice, list_ingredients[1])
                total_change = total_amount - MENU[choice]['cost']
                money += MENU[choice]['cost']
                print(f"Here is ${round(total_change, 2)} in change")
                print(f"Here is your {choice}. Enjoy!")
            elif resources['water'] < MENU[choice]['ingredients']['water']:
                print(f"Sorry, we do not have water . Here is your money back.")
            elif resources['coffee'] < MENU[choice]['ingredients']['coffee']:
                print(f"Sorry, we do not have coffee . Here is your money back.")
    # Choice latte or cappuccino
    elif choice == 'latte' or choice == "cappuccino":
        total_amount = calculate_amount()
        if total_amount < MENU[choice]['cost']:
            print("Sorry, not enough money.")
        else:
            if resources['water'] > MENU[choice]['ingredients']['water'] and \
                    resources['coffee'] > MENU[choice]['ingredients']['coffee'] and \
                    resources['milk'] > MENU[choice]['ingredients']['milk']:
                resources['water'] = calculate_remaining_ingredients(choice, list_ingredients[0])
                resources['coffee'] = calculate_remaining_ingredients(choice, list_ingredients[1])
                resources['milk'] = calculate_remaining_ingredients(choice, list_ingredients[2])
                total_change = total_amount - MENU[choice]['cost']
                money += MENU[choice]['cost']
                print(f"Here is ${round(total_change, 2)} in change")
                print(f"Here is your {choice}. Enjoy!")
            elif resources['water'] < MENU[choice]['ingredients']['water']:
                print(f"Sorry, we do not have water . Here is your money back.")
            elif resources['milk'] < MENU[choice]['ingredients']['milk']:
                print(f"Sorry, we do not have milk . Here is your money back.")
            elif resources['coffee'] < MENU[choice]['ingredients']['coffee']:
                print(f"Sorry, we do not have coffee . Here is your money back.")
    elif choice == 'off':
        break
