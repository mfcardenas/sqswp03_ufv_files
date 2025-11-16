def evaluate_functionality(requirements, implementation):
    fulfilled = 0
    for req in requirements:
        if req in implementation:
            fulfilled += 1
    return (fulfilled / len(requirements)) * 100 if requirements else 0
