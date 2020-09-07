monto = int(input('¿Cuál es el monto disponible en tu tarjeta de crédito?: '))

if monto >= 2500:
    print('Puede realizar la compra.')
    print(f'Su saldo restante es: {monto - 2500}')
elif monto <= 2500:
    print('No puede realizar la compra.')
    print(f'Le faltan: {2500 - monto}')