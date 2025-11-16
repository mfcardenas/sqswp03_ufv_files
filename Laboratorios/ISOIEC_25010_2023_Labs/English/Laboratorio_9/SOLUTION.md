# Solution Lab 9

## Solution Problem 1
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

## Solution Problem 2
```python
# Use radon for metrics
# radon cc -a problem1.py
```

## Explanation
- **Integration**: Tests and metrics evaluate quality.
- **Improvements**: Add more tools and automation.
