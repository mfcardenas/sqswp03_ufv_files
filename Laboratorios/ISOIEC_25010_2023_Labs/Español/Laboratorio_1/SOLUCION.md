# Solución Laboratorio 1

## Solución Problema 1
```python
def evaluar_funcionalidad(requisitos, implementacion):
    cumplidos = 0
    for req in requisitos:
        if req in implementacion:
            cumplidos += 1
    return (cumplidos / len(requisitos)) * 100 if requisitos else 0
```

## Solución Problema 2
```python
def calculadora():
    print("Bienvenido a la Calculadora Básica")
    while True:
        try:
            op = input("Operación (+, -, *, /) o 'salir': ")
            if op == 'salir':
                break
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            if op == '+':
                print(f"Resultado: {a + b}")
            elif op == '-':
                print(f"Resultado: {a - b}")
            elif op == '*':
                print(f"Resultado: {a * b}")
            elif op == '/':
                if b != 0:
                    print(f"Resultado: {a / b}")
                else:
                    print("Error: División por cero")
            else:
                print("Operación no válida")
        except ValueError:
            print("Entrada no válida")
```

## Explicación
- **Funcionalidad**: La función evalúa el cumplimiento de requisitos básicos.
- **Usabilidad**: La calculadora maneja errores y proporciona feedback claro.
- Mejoras: Añade más validaciones y opciones para escalar la complejidad.
