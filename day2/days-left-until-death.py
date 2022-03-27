#take the age as input
age = input("What is your current age?\n")
age = int(age)

#Taking 90 as the average age calculate the number of days, weeks and minths left
days = (365 * 90) - (365 * age)
weeks = (52 * 90) - (52 * age)
months = (12 * 90) - (12 * age)
result = f"You have {days} days, {weeks} weeks, and {months} months left."
print(result)

# TO calculate exact weeks try the code below.

# age = int(input("Enter your age here: "))
# years = 90 - age
# days = years * 365
# weeks = int(days / 7)
# months = years * 12
# print(f"You have {days} days, {weeks} weeks and {months} months left.")