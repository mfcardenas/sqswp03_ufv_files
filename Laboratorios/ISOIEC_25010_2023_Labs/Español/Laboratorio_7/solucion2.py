def validar_input(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Debe ser número")
