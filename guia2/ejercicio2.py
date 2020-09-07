numbers = [1, 234, 54, 34, 967, 456, 38, 88, 109, 3]
numbers.sort()


print(f'El numero mayor es: {numbers[-1]}')
print(f'El numero menor es: {numbers[0]}')

numbers_big = []
for i in numbers:
    if i > 100:
        numbers_big.append(i)

numbers_small = []
for i in numbers:
    if i < 50:
        numbers_small.append(i)

if len(numbers_big) >= 3:
    print(f'Numeros mayores a 100: {numbers_big}')
else:
    print(f'Numeros menores a 50: {numbers_small}')