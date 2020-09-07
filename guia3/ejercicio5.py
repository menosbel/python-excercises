# Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números,
# False si hay al menos uno de los parámetros ingresados que no es un número, y
# None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.


def mi_funcion(*args):
    argumentos = []
    for i in args:
        if type(i) == int or type(i) == float:
            argumentos.append(i)
    if len(argumentos) == len(args):
        return True
    elif len(argumentos) != 0:
        return False
    else:
        return None


print(mi_funcion('pepe', 'hola'))
print(mi_funcion('pepe', 'hola', 2.5, 4))
print(mi_funcion(2.5, 4))
