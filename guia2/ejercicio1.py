message = input('Ingrese un mensaje: ')

if len(message) >= 100:
    print(message)
elif 50 <= len(message) < 100:
    print(message[::-1])
else:
    print('Su mensaje es demasiado corto.')

