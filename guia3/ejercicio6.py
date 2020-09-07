"""
Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
"""


def modo_Title(mensaje):
    if mensaje.istitle():
        print(f'El mensaje ya está en modo title: {mensaje}')
    else:
        print(mensaje.title())


modo_Title('buenos dias')




