divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

usuario = input('Escriba una divisa: ')

for i,k in divisas.items():
    if i == usuario:
        print(k)
        break
    else:
        print('Esa divisa no esta en el diccionario')
        break
