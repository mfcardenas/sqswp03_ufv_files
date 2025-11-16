def validate_input(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Must be a number")
