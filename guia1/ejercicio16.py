datos = {}
respuesta = 'S'

while respuesta == 'S':
    key = input('Que dato desea introducir?')
    value = input(f'{key}: ')
    datos[key] = value
    print(datos)
    respuesta = input('Desea seguir introduciendo datos? Ingrese S por si o N por no: ').upper()


