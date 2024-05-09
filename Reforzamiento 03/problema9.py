import math
class circulo:
    radio1=4
    radio2=5
    def __init__(self,r):
        self.r = r

    def area(self):
        self.r1=float(input('Ingresa el radio del circulo: '))
        area = math.pi*pow(self.r1,2)
        return print("area del circulo:",area)

    def perimetro(self):
        perimetro = 2*self.r1*math.pi
        return print("su perimetro es:",perimetro)

circ=circulo(0)
circ.area()
circ.perimetro()
