# Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números,
# si los hay, que aparecen en dicho mensaje.

numeros = []


def numbers():
    mensaje = input('Ingrese un mensaje: ')
    for i in mensaje.split():
        if i.isdigit():
            numeros.append(i)
    print(f'Los numeros dentro del mensaje son: {numeros}')


numbers()