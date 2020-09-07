import string

abecedario = list(string.ascii_lowercase)
abecedario_copia = abecedario.copy()

for i in abecedario_copia:
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        if i == vocal:
            abecedario_copia.remove(i)

print(abecedario)
print(abecedario_copia)