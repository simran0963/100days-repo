print("Welcome to the tip calculator.")
bill = input("What was the total bill?\nRs")
bill = float(bill)
tip = input(f"What percentage tip would you like to give?, 10, 12 , or 15? ")
tip = int(tip)
people = input("How many people to split the bill? ")
people = int(people)


final_value = float(bill + bill * (tip/100))
final_value /= people
print(f"Each person should pay: Rs", final_value)