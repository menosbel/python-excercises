lista1 = [1, 2, 3]
lista2 = [-1, 0, 2]

producto = 0
for i in range(len(lista1)):
    resultado = lista1[i] * lista2[i]
    producto += resultado

print(producto)