nombre = input('Escriba su nombre: ')
edad = input('Escriba su edad: ')
direccion = input('Escriba su direccion: ')
telefono = input('Escriba su telefono: ')

diccionario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

print(f"Tu nombre es {diccionario['nombre']}")
print(f"Tu edad es {diccionario['edad']}")
print(f"Tu direccion es {diccionario['direccion']}")
print(f"Tu telefono es {diccionario['telefono']}")