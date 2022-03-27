from art import logo

print(logo)

#Calculator

# def Calculation(n1, operation, n2):
#   if operation == "+":
#Add
def add(n1, n2):
    return n1 + n2

  # elif operation == "-":
#Subtract
def subtract(n1, n2):
    return n1 - n2

  # elif  operation == "*":
#Multiply
def multiply(n1, n2):
    return n1 * n2

  # elif operation == "/":
#Divide
def divide(n1, n2):
    return n1 / n2

  # else:
  #   print("Invalid operation")

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

num1 = int(input("Enter the first number: "))
result = "n1" "operation" "n2"
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Enter the second number: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")