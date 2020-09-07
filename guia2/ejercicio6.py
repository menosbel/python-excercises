# opcion dos. mas optima despues de ver la solucion
operacion = int(input('''
                Seleccione la operacion que desea realizar:
                1- Suma
                2- Resta
                3- Multiplicacion
                4- Division
                5- Terminar programa
                Que desea hacer: '''))

while 1 <= operacion <= 5:
    if operacion == 5:
        print('El programa ha terminado.')
        break
    num_1 = int(input('Ingrese un numero: '))
    num_2 = int(input('Ingrese otro numero: '))
    if operacion == 1:
        print(f'Resultado: {num_1 + num_2}')
    elif operacion == 2:
        print(f'Resultado: {num_1 - num_2}')
    elif operacion == 3:
        print(f'Resultado: {num_1 * num_2}')
    elif operacion == 4:
        print(f'Resultado: {num_1 / num_2}')

    operacion = int(input('''
                Seleccione la operacion que desea realizar:
                1- Suma
                2- Resta
                3- Multiplicacion
                4- Division
                5- Terminar programa
                Que desea hacer: '''))

