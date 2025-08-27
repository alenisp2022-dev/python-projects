# Professional Python Calculator
# Author: Alen Ispiryan
# Description: Simple command-line calculator with basic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("Welcome to Professional Python Calculator!")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            x = float(input("Enter first number (or 'q' to quit): "))
        except ValueError:
            print("Goodbye!")
            break

        operation = input("Enter operation (+, -, *, /): ")

        try:
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if operation == "+":
            print(f"Result: {add(x, y)}")
        elif operation == "-":
            print(f"Result: {subtract(x, y)}")
        elif operation == "*":
            print(f"Result: {multiply(x, y)}")
        elif operation == "/":
            print(f"Result: {divide(x, y)}")
        else:
            print("Invalid operation. Try again.")
        
        print("\n----------------------\n")

if __name__ == "__main__":
    calculator()
