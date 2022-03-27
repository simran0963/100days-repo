import os

def clear():
	os.system('cls')

clear()

print("Leap year finder.")
year = input("Enter the year you want to check: ")
year =int(year)


if year % 4 == 0 :
	if year % 100 == 0 :
		if year % 400 == 0 :
			print("Year entered is a leap year.")

		else :
			print("Year entered is not a leap year.")

	else :
		print("Year entered is a leap year.")

else :
	print("Year entered is not a leap year.")