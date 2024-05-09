
def pedir_palabra():
    nombre = input("Escriba una palabra: ")

    while len(nombre) < 3:
        nombre = input("Escriba una palabra de mas de 3 letras: ")

    print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

pedir_palabra()
