class operacion:
    def __init__(self,numero):
        self.numero=numero

    def cubo(self):
        self.numero=int(input("digite un numero: "))
        self.cubito=self.numero**3
        return self.cubito

    def cuadrado(self):
        self.cuadrado=self.cubito**(2)
        return self.cuadrado

num=operacion(0)
print("el numero digita al cubo es: ",num.cubo())
print("del resultado del cubo elevado al cuadro es:",num.cuadrado())