# Solution Lab 1

## Solution Problem 1
```python
def evaluate_functionality(requirements, implementation):
    fulfilled = 0
    for req in requirements:
        if req in implementation:
            fulfilled += 1
    return (fulfilled / len(requirements)) * 100 if requirements else 0
```

## Solution Problem 2
```python
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
```

## Explanation
- **Functionality**: The function evaluates compliance with basic requirements.
- **Usability**: The calculator handles errors and provides clear feedback.
- **Improvements**: Add more validations and options to scale complexity.
