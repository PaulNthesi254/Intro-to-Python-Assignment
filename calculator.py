# prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# prompt the  user to enter the second number
num2 = float(input("Enter the second number: "))

# prompt the user to enter the operation of choice
operation = input("Enter operation (+, -, *, /): ")

# Arithmetic operations
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")

