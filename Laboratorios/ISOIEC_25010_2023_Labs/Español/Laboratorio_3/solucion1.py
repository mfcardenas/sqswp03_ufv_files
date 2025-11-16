import re

def validar_entrada(entrada):
    if re.match(r"^[a-zA-Z0-9_]+$", entrada):
        return True
    return False
