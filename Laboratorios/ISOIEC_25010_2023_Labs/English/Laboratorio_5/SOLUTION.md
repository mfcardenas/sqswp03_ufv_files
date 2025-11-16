# Solution Lab 5

## Solution Problem 1
```python
# Optimized
def sum_of_squares(n):
    return sum(i**2 for i in range(n+1))
```

## Solution Problem 2
```python
import cProfile

def function_to_measure():
    # Code to profile
    pass

cProfile.run('function_to_measure()')
```

## Explanation
- **Efficiency**: Comprehensions reduce complexity.
- **Measurement**: cProfile identifies hotspots.
- **Improvements**: Add more metrics and optimizations.
