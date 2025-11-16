# Solución Laboratorio 5

## Solución Problema 1
```python
# Optimizado
def suma_cuadrados(n):
    return sum(i**2 for i in range(n+1))
```

## Solución Problema 2
```python
import cProfile

def funcion_a_medir():
    # Código a perfilar
    pass

cProfile.run('funcion_a_medir()')
```

## Explicación
- **Eficiencia**: Comprehensions reducen complejidad.
- **Medición**: cProfile identifica hotspots.
- Mejoras: Añade más métricas y optimizaciones.
