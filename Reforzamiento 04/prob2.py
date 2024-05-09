"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""
def indice_lista():
    try:
        lista = [2, 6, 10, 4, 5, 23, 1]
        lista[10]
    except IndexError:
        print("ERROR: índice incorrecto en lista, no existe.")
    else:
        print("Buen manejo de lista")

indice_lista()