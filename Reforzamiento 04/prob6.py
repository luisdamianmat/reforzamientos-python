"""Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo"""

def pedir_entero():
    entero1=int(input("digite un numero entero: "))
    entero2=int(input("digite un numero entero: "))
    return entero1,entero2
def sumar():
    return print("La suma es: ",sum(pedir_entero()))



