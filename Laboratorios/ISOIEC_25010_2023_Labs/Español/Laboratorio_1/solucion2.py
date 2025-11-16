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
