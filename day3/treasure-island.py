import os

def clear():
	os.system('cls')

clear()

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where would you like to go? "left" or "right"?').lower()



if choice1 == "left" :
	choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. type "swim" to swim across.').lower()


	if  choice2 == "wait" :
		choice3 = input("You arrived at the island unharmed. There is a house with 3 doors.One is red, one is yellow and one blue.Which colour do you choose? ").lower()
		if choice3 == "red" :
			print("It's a Room full of fire. Game Over.")
		elif choice3 == "yellow" :
			print("You found the treasure. You win!")
		elif choice3 == "blue" :
			print("You entered the room of beasts. Game Over.")
	
	else :	
		print("You got attacked by an angry trout. Game Over.")

else :
	print("You fell into the hole. Game Over.")	