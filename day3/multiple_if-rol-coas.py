import os

def clear():
	os.system('cls')

clear()

print("Welcome to the roller coaster")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
	print("You can ride the roller coaster!")
	your_age = input("enter your age ")
	your_age = int(your_age)

	if your_age < 12 :
		print("You need to pay Rs 50.")
		bill = 50
	elif 12 <= your_age < 18 :
		print("you need to pay Rs 100")
		bill = 100
	else :
		print("You need to pay Rs 150.")
		bill = 150

	photo_ticket = input("do you want a photo taken? Y or N? ")
	

	if photo_ticket == "Y" :
		bill += 25
		print(bill)
else :
	print("Sorry, you've to grow taller before you can ride.")
