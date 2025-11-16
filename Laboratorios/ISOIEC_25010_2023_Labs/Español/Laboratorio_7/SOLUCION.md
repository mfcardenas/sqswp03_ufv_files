# Solución Laboratorio 7

## Solución Problema 1
```python
def menu():
    print("1. Opción 1")
    print("2. Opción 2")
    choice = input("Elige: ")
    if choice == '1':
        print("Ejecutando 1")
    elif choice == '2':
        print("Ejecutando 2")
    else:
        print("Inválido")
```

## Solución Problema 2
```python
def validar_input(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Debe ser número")
```

## Explicación
- **Usabilidad**: Menús claros y validaciones mejoran experiencia.
- Mejoras: Añade más interactividad y evaluaciones.
