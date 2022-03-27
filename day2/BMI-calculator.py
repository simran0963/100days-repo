print("BMI Calculator")
weight = input("enter your weight in kg ")
weight = float(weight)

height = input("enter your height in m ")
height = float(height)

bmi = weight/(height ** 2)

# print("Your BMI is " + str(result))
# print(bmi_as_int)
print(int(round(bmi)))