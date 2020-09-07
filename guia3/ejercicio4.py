# Ejercicio 4: Crear una función que, a partir de 4 números, devuelva el mayor producto de dos de ellos.
# Imprimir resultado por pantalla.


def producto():
    numeros = []
    for i in range(4):
        num = input('Ingrese un numero: ')
        numeros.append(num)
    numeros.sort()
    num_1 = int(numeros[-1])
    num_2 = int(numeros[-2])
    print(num_1 * num_2)


producto()
