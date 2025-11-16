# Solución Laboratorio 3

## Solución Problema 1
```python
import re

def validar_entrada(entrada):
    if re.match(r"^[a-zA-Z0-9_]+$", entrada):
        return True
    return False
```

## Solución Problema 2
```python
import logging

logging.basicConfig(level=logging.ERROR)

def operacion_riesgosa():
    try:
        # Simula operación
        raise ValueError("Error simulado")
    except ValueError as e:
        logging.error(f"Error: {e}")
        return "Manejado"
```

## Explicación
- **Seguridad**: Validaciones previenen ataques.
- **Fiabilidad**: Logging y excepciones manejan fallos gracefully.
- Mejoras: Añade más patrones de validación y recuperación.
