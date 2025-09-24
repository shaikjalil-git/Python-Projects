#expresso $1.50 = 50ml water, 18g Coffee
#Latte $4.50 = 200ml Water, 24g Coffee, 150ml Milk 
#Cappuccino $3.00 = 250ml Water, 24g COffee, 100ml Milk

MENU = {
    "expresso": {
        "ingredients": {
            "water" : 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost" : 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}
profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def is_resources_sufficient(order_ingredients):
    """----------------Returns True when order can be made, False if ingredients are insufficient-------------------"""
    
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():   
    """-------------------Returns the total calculated money from inserted coins----------------------"""
    print("insert the coins")
    total = int(input("How many Quaters?")) * 0.25
    total += int(input("How many Dimes?")) * 0.1  
    total += int(input("How many Pennies?")) * 0.01
    total += int(input("How many Nickles?")) * 0.05
    return total 

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(order_ingredients):
    """Deduct the required ingredients from the resourrces"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice}☕. Enjoy!")




is_on = True

# CODE STARTS HERE 😐😐😐

while is_on:   
    choice = input("What would you like? (Expresso/Latte/Cappuccino):").lower()
    if choice == "Exit":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])
            