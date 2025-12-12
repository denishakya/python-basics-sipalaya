# Project 2: built simple calculator

def simple_calculator():
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("Select operation: +, -, *, /, //, %, **")
    op = input("Enter operation: ")

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "//":
        result = x // y
    elif op == "%":
        result = x % y
    elif op == "**":
        result = x ** y
    else:
        result = "Invalid operation"

    print("Result:", result)
