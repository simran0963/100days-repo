import os

def clear():
	os.system('cls')

clear()

print("Welcome to Love Calculator")
name1 = str(input("What is your name? ")).lower()
name2 = str(input("What is their name? ")).lower()

combined_string = name1 + name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

# t = combined_string.count("t")
# r = combined_string.count("r")
# u = combined_string.count("u")
# e = combined_string.count("e")
# l = combined_string.count("l")
# o = combined_string.count("o")
# v = combined_string.count("v")
# e = combined_string.count("e")

# T = combined_string.count("t")
# R = combined_string.count("r")
# U = combined_string.count("u")
# E = combined_string.count("e")
# L = combined_string.count("l")
# O = combined_string.count("o")
# V = combined_string.count("v")
# E = combined_string.count("e")

# true = int((t+T) + (R+r) + (u+U) + (e+E))
# love = int((l+L) + (o+O) + (v+V) + (e+E))
# love_score = str(true) + str(love)

if love_score > "90" or love_score < "10" :
	print(f"Your score is,", love_score, "you go together like coke and mentos")

elif love_score > "40" and love_score < "50" :
	print(f"Your score is,", love_score, "you are alright together.")

else :
	print(love_score)
