creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

for i, k in creditos.items():
    print(f'{i} tiene {k}')

total = 0
for i in creditos.values():
    total += i

print(total)