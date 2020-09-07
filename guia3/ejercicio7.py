"""
Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no.
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", en caso contrario,
devolver "La palabra no es un palíndromo".
"""


def palindromo(palabra):
    if palabra == palabra[::-1]:
        print(f'{palabra} es un palindromo')
    else:
        print(f'{palabra} no es un palindromo')


palindromo('ana')