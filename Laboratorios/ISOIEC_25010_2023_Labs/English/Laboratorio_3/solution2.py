import logging

logging.basicConfig(level=logging.ERROR)

def risky_operation():
    try:
        raise ValueError("Simulated error")
    except ValueError as e:
        logging.error(f"Error: {e}")
        return "Handled"
