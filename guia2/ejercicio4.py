numbers = []

for i in range(6):
    num = int(input('Ingrese un numero: '))
    numbers.append(num)
numbers.sort()

for i in numbers:
    print(i)
