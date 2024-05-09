class revertir:
    def __init__(self,oracion):
        self.oracion=oracion

    def imprimir(self):
        #letra=input("Ingresa la oracion: ")
        resultado=' '.join(reversed(self.oracion.split()))
        #cambiar por letra si se quiere imprimir por usuario
        print(resultado)



frase='Hola pythonistas seguimos adelante'
print("Hola pythonistas seguimos adelante")
oracion1=revertir(frase)
oracion1.imprimir()