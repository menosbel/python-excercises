num_pares = []


def pares():
    for i in range(0, 101):
        if i % 2 == 0:
            num_pares.append(i)
    print(num_pares)


pares()
