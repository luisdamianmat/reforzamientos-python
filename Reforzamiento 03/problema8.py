class persona:

    def __init__(self,nombre,apellido,edad,lista1):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.lista1=lista1

    def nom_ape(self):
        self.lista1={}
        self.nombre1=input("Nombre de la persona: ")
        self.apellido1=input("Apellido de la persona: ")
        self.lista1["nombre"]=self.nombre1
        self.lista1["apellido"]=self.apellido1
        return self.lista1
    def edad_persona(self):
        self.edad1=input("Edad de la persona: ")
        self.lista1["edad"]=self.edad1
        return self.lista1

    def imprima(self):
        print(self.lista1)

persona1=persona("","","","")
persona1.nom_ape()
persona1.edad_persona()
persona1.imprima()

