import cProfile

def funcion_a_medir():
    suma = 0
    for i in range(1000):
        suma += i**2

cProfile.run('funcion_a_medir()')
