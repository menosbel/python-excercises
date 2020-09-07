clientes = {}
option = ''

while option != '6':
    if option == '1':
        ID = input('Ingresar el ID del cliente: ')
        nombre = input('Ingresar el nombre del cliente: ')
        direccion = input('Ingresar la direccion del cliente: ')
        telefono = input('Ingresar el telefono del cliente: ')
        correo = input('Ingresar el correo del cliente: ')
        preferente = input('¿Es un cliente preferente? (S/N): ').upper()
        cliente = {'nombre': nombre,
                   'direccion': direccion,
                   'telefono': telefono,
                   'correo': correo,
                   'preferente': preferente == 'S'}
        clientes[ID] = cliente
    if option == '2':
        ID_cliente = input('Ingresar el ID del cliente que desea eliminar: ')
        if ID_cliente in clientes:
            clientes.__delitem__(ID_cliente)
        else:
            print('No existe ningun cliente con el id ', id)
    if option == '3':
        ID_cliente = input('Ingresar el ID del cliente que desea visualizar: ')
        if ID_cliente in clientes:
            print(clientes.__getitem__(ID_cliente))
        else:
            print('No existe ningun cliente con el id ', id)
    if option == '4':
        print('Lista de clientes:')
        for i, k in clientes.items():
            print(i, k['nombre'])
    if option == '5':
        print('Lista de clientes preferentes:')
        for i, k in clientes.items():
            if k['preferente']:
                print(i, k['nombre'])
    option = input('Menu de opciones:\n'
                   '1 Añadir cliente\n'
                   '2 Elminar cliente\n'
                   '3 Mostrar cliente\n'
                   '4 Listar clientes\n'
                   '5 Listar clientes preferentes\n'
                   '6 Terminar programa\n'
                   'Ingrese un numero: '
                   )