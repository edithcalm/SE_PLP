num1 = float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
            result = num1 + num2
            print("{num1} + {num2} = {result}")
elif operator == "-":
        result = num1 -num2
        print("{num1} - {num2} = {reult}")
elif operator == "*":
        result = num1 * num2 
        print("{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
           print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")  
else:
  print("Invalid operator. Please enter +, -, *, or /.")
