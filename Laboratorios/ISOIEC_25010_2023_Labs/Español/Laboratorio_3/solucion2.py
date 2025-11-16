import logging

logging.basicConfig(level=logging.ERROR)

def operacion_riesgosa():
    try:
        raise ValueError("Error simulado")
    except ValueError as e:
        logging.error(f"Error: {e}")
        return "Manejado"
