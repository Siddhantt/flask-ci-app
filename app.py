def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    operation = input("Enter operation: ").strip().lower()
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = calculate(a, b, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
