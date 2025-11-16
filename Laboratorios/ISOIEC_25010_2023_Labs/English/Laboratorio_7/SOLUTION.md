# Solution Lab 7

## Solution Problem 1
```python
def menu():
    print("1. Option 1")
    print("2. Option 2")
    choice = input("Choose: ")
    if choice == '1':
        print("Executing 1")
    elif choice == '2':
        print("Executing 2")
    else:
        print("Invalid")
```

## Solution Problem 2
```python
def validate_input(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Must be a number")
```

## Explanation
- **Usability**: Clear menus and validations improve experience.
- **Improvements**: Add more interactivity and evaluations.
