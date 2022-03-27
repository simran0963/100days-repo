import os

def clear():
	os.system('cls')

clear()
#An improved version of the BMI calculator
 
weight = input("enter your weight in kg ")
weight = int(weight)
height = input("enter your height in m ")
height = float(height)

bmi = round(weight / (height ** 2), 2)
print(bmi)
if bmi < 18.5 :
	print("You are underweight.")

elif 18.5 < bmi < 25 :
	print("You are normal weight.")

elif 25 < bmi < 30 :
	print("You are overweight")

elif 30 < bmi < 35 :
	print("You are obese.")

else :
	print("You are clinically obese.")