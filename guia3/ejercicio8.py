"""
Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
Luego crear una función que, a partir de esos datos, devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
"""


def consumo_auto(mardel):
    litros = (mardel * 2 / 100) * 2
    return litros


litros = consumo_auto(400)


def costo(precio):
    costo_nafta = litros * precio
    return costo_nafta


costo_viaje = costo(60)


print(f'El auto que va y vuelve de Mardel gasta {litros} litros de nafta.\n{litros} litros cuestan {costo_viaje}')
