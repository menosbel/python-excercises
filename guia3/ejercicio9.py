"""
Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas.
Luego crear una función que nos informe los estudiantes aprobados (nota >= 7),
los estudiantes desaprobados (4 <= nota < 7)
y los estudiantes aplazados (0 <= nota < 4).
"""

estudiantes_notas = {}

for i in range(10):
    alumno = input('Nombre del alumno: ')
    nota = int(input('Nota: '))
    estudiantes_notas[alumno] = nota

print(f'Los estudiantes y sus notas son: {estudiantes_notas}')


def estudiantes_estado():
    aprobados = {}
    desaprobados = {}
    aplazados = {}
    for clave, valor in estudiantes_notas.items():
        if valor >= 7:
            aprobados[clave] = valor
        elif 4 <= valor <= 7:
            desaprobados[clave] = valor
        elif 0 <= valor < 4:
            aplazados[clave] = valor
    print(f'Los estudiantes aprobados son: {aprobados}')
    print(f'Los estudiantes desaprobados son: {desaprobados}')
    print(f'Los estudiantes aplazados son: {aplazados}')


estudiantes_estado()

