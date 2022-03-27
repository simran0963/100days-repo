import random
import os

def clear():
	os.system('cls')

clear()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '+', '#', '$', '%', '(', ')', '*', '&']
print("Welcome to PyPassword generator!")

letter = int(input("How many letters do you want in your password? "))

number = int(input("How many numbers do you want in your password? "))

symbol = int(input("How many symbols do you want in your password? "))




password_list = []
for char in range(1, letter + 1):
	password_list.append(random.choice(alphabets))
for num in range(1, number + 1):
	password_list += random.choice(numbers)
for sym in range(1, symbol + 1) :
	password_list += random.choice(symbols)
	 
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list :
	password += char
print(f"Your password is:", {password})