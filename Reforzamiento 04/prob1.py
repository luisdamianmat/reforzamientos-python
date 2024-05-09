"""Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""

# Completa el ejercicio aquí
def error():

    try:
        suma = 80 + "Hola Pythonista"
    except TypeError:
        print("Error: La suma de un int con una cadena no es posible, vuelva a intentarlo")
    else:
        print("Operacion correcta")

error()




