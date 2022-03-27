#TODO: 1. Print the report of all coffee machine resources.
#TODO: 2. Check that the resources are sufficient to make the drink order.
#TODO: 3. Process coins.
#TODO: 4. Check if the transaction was successful.
#TODO: 5. Make coffee.

from CoffeeMachine import MENU, resources
import os

def clear():
  os.system('cls')

clear()


profit = 0


def is_resource_sufficient(order_ingredients):
	"""Returns True if order is made and False when ingredients are insufficient."""
	for item in order_ingredients:
		if order_ingredients[item] >= resources[item]:
			print(f"Sorry there is not enough {item}.")
			return False
	return True


def process_coins():
	"""Returns the total calculated from coins inserted"""
	print("Please insert coins.")
	total = int(input("How many quarters?: ")) * 0.25
	total += int(input("How many dimes?: ")) * 0.1
	total += int(input("How many nickels?: ")) * 0.05
	total += int(input("How many pennies?: ")) * 0.01
	return total

def is_transasction_successful(money_recieved, drink_cost):
	if money_recieved >= drink_cost:
		change = round(money_recieved - drink_cost, 2)
		print(f"Here is ${change} in change.")
		global profit
		profit += drink_cost
		return True
	else:
		print("Sorry that's not enough money. Money refunded.")
		return False


def make_coffee(drink_name, order_ingredients):
	"""Deduct the required ingredients from the resources."""
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	print(f"Here is your {drink_name} ☕")


is_on = True
while is_on :
  choice = input("What would you like? (espresso/Latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  else:
	  drink = MENU[choice]
	  if is_resource_sufficient(drink["ingredients"]):
		  payment = process_coins()
		  if is_transasction_successful(payment, drink["cost"]):
			  make_coffee(choice, drink["ingredients"])