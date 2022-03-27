import os

def clear():
	os.system('cls')

clear()

print("Welcome to Python Pizza deliveries!")

print("Small Pizza: Rs 100")
print("Medium pizza: Rs 180")
print("Large Pizza: Rs 250")
size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese? ")
if size == "S" :
	bill = 100
	if add_pepperoni == "Y" :
	  bill += 25
	if extra_cheese == "Y" :
	  bill += 15
	  print(bill)
	else :
	  print(bill)
	  
if size == "M" :
	bill = 180
	if add_pepperoni == "Y" :
	  bill += 40
	if extra_cheese == "Y" :
	  bill += 15
	  print(bill)
	else :
	  print(bill)

if size == "L" :
	bill = 250
	if add_pepperoni == "Y" :
	  bill += 40
	if extra_cheese == "Y" :
	  bill += 15
	  print(bill)
	else :
	  print(bill)