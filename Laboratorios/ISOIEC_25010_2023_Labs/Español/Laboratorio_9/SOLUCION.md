# Solución Laboratorio 9

## Solución Problema 1
```python
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
```

## Solución Problema 2
```python
# Usa radon para métricas
# radon cc -a problema1.py
```

## Explicación
- **Integración**: Pruebas y métricas evalúan calidad.
- Mejoras: Añade más herramientas y automatización.
