"""
Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.
"""


def decorator_function(original_function):
    def funcion_interna(*args):
        print('La siguiente es una función matemática: ')
        print(original_function(*args))

    return funcion_interna


@decorator_function
def suma(a, b):
    return f'Esto es una suma y el resultado es: {a + b}'


print(suma(45, 25))

# Cuando la ejecuto funciona OK, pero me tira un "None" al final de la ejecucion no entiendo por que
