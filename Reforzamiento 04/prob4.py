"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)"""

def division():

    try:
        string = "Hello Pythonista"
        print(string / 0)
    except TypeError:
        print("Error: La division de una cadena con 0 no es posible, vuelva a intentarlo")
    else:
        print("operacion correcta")

division()