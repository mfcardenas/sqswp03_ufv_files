def calculator():
    print("Welcome to the Basic Calculator")
    while True:
        try:
            op = input("Operation (+, -, *, /) or 'exit': ")
            if op == 'exit':
                break
            a = float(input("First number: "))
            b = float(input("Second number: "))
            if op == '+':
                print(f"Result: {a + b}")
            elif op == '-':
                print(f"Result: {a - b}")
            elif op == '*':
                print(f"Result: {a * b}")
            elif op == '/':
                if b != 0:
                    print(f"Result: {a / b}")
                else:
                    print("Error: Division by zero")
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid input")
