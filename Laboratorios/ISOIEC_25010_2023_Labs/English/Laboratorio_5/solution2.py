import cProfile

def function_to_measure():
    total = 0
    for i in range(1000):
        total += i**2

cProfile.run('function_to_measure()')
