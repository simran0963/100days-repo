f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
#Already used functions with outputs.
formatted_name = f_name + l_name
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
	"""Take the first and last name and format it to return the title case version of the name."""
	if f_name == "" or l_name == "" :
		return "You didn't provide valid inputs." 
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"Result: {formatted_f_name} {formatted_l_name}"

format_name()