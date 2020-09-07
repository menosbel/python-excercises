decimal = 0
for i in range(3):
    binario = input("Ingrese un número binario: ")
    for bit in binario:
        decimal += decimal + int(bit)
    print(decimal + 1)
    decimal = 0


