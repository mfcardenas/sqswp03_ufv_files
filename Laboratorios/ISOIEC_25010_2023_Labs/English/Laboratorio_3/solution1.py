import re

def validate_input(input_data):
    if re.match(r"^[a-zA-Z0-9_]+$", input_data):
        return True
    return False
