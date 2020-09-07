number_1 = input('Ingresar un numero: ')
number_2 = input('Ingresar otro numero: ')

number_1 = int(number_1)
number_2 = int(number_2)

if number_1 < number_2:
    print(number_2 - number_1)
elif number_1 > number_2:
    print(number_1 + number_2)
elif number_1 == number_2:
    print(number_1 * number_2)

