"""
numeros = [1, 5, 6, 7, 19, 922, 34]
numeros.sort()
print(f'Lista ordenada: {numeros}')
print(f'Numero menor: {numeros[0]}')
print(f'Numero mayor: {numeros[-1]}')
"""

lista_numeros = []
rta = 1

while rta == 1:
    numero = int(input('Ingrese un numero: '))
    lista_numeros.append(numero)
    preg = input('Presione s para seguir o n para parar: ').lower()
    if preg == 's':
        rta = 1
    elif preg == 'n':
        rta = 0

print(lista_numeros)