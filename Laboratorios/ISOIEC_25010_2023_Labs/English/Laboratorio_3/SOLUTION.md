# Solution Lab 3

## Solution Problem 1
```python
import re

def validate_input(input_data):
    if re.match(r"^[a-zA-Z0-9_]+$", input_data):
        return True
    return False
```

## Solution Problem 2
```python
import logging

logging.basicConfig(level=logging.ERROR)

def risky_operation():
    try:
        # Simulate operation
        raise ValueError("Simulated error")
    except ValueError as e:
        logging.error(f"Error: {e}")
        return "Handled"
```

## Explanation
- **Security**: Validations prevent attacks.
- **Reliability**: Logging and exceptions handle failures gracefully.
- **Improvements**: Add more validation and recovery patterns.
