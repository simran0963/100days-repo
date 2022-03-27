import random
# Create a words list, a list of words
words_list = ['serendipity', 'petrichor', 'supine', 'solitude', 'aurora']
#Randomly choose a word from the words list 
choosen_word = random.choice(words_list)
#Ask the user to take a guess
guess = input("Enter your choice: ").lower()
#check if  the choosen word and your guess match
for letter in choosen_word:
	if letter == guess:
		print("Right")

	else :
		print("Wrong")