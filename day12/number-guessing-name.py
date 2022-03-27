from random import randint
from art import logo
import os

def clear():
	os.system('cls')

clear()
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
	if answer > guess:
		print("Too Low.")
		return turns - 1
	elif answer < guess:
		print("Too High.")
		return turns - 1
	else:
		print(f"You got it! The answer was {answer}.")

def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	elif level == "hard":
		return HARD_LEVEL_TURNS

def game():
	print(logo)
	print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
	answer = randint(1, 100)
	print(f"Pssst, your answer is {answer}")

	turns = set_difficulty()
	guess = 0
	while guess != answer:
		print(f"You have {turns} attempts left to guess the answer.")
		guess = int(input("Enter the number: "))
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print("You have run out of guesses. You lose.")
			return
		elif guess != answer:
			print("Guess again.")

game()