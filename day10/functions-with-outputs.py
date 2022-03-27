import os
def clear():
	os.system('cls')

clear()

#Functions with Outputs
formatted_f_name = str(input("enter your first name: ")).title()
formatted_l_name = str(input("enter your last name: ")).title()
	
def format_name(f_name, l_name):
	print(f"Your name is " + f_name + " " + l_name)
  
format_name(f_name=formatted_f_name, l_name=formatted_l_name)
#NOTE that a different kind of approach is used for the same code as above in the docstrings.py file