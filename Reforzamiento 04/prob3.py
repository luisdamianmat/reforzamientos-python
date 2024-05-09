"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""

def nom_usuario():
    try:
        persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
        persona['profesion']
    except KeyError:
        print("ERROR: acceso a key incorrecto en diccionario")
    else:
        print("Buen manejo de diccionario")

nom_usuario()
