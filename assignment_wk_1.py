
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the mathematical operation (+, -, *, /): ")

# Perform the mathematical operation based on the user's input
if operation == "+":
    result = (num1 + num2)
elif operation == "-":
    result = (num1 - num2)
elif operation == "*":
    result = (num1 * num2)
elif operation == "/":
    result = (num1 / num2)
else:
    result = "Error: Invalid mathematical operation"

# Print the result
print("Result:", result)