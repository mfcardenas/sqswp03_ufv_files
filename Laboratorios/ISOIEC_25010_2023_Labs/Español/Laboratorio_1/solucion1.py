def evaluar_funcionalidad(requisitos, implementacion):
    cumplidos = 0
    for req in requisitos:
        if req in implementacion:
            cumplidos += 1
    return (cumplidos / len(requisitos)) * 100 if requisitos else 0
