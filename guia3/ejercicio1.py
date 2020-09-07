def transformador():
    horas = int(input('Ingrese una cantidad de horas: '))
    minutos = horas * 60
    segundos = horas * 3600
    print(f'{horas} hora/s: {minutos} minutos, {segundos} segundos')


transformador()