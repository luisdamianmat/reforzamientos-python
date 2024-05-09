"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""
"""se esta tomando la palabra 'entre' como que considera a ambos numeros de los extremos"""
lista=[]
def cuadrado(x,y):
    if x>y:
        while y<=x:
            cua=pow(y,2)
            lista.append(cua)
            y=y+1
        print(lista)
    elif x<y:
        while x<=y:
            cua=pow(x,2)
            lista.append(cua)
            x=x+1
        print(lista)
    else:
        print("los cuadrados comprendidos entre los numeros digitados es: {}".format(pow(x,2)))

a=int(input("digite un numero: "))
b=int(input("digite otro numero: "))
cuadrado(a,b)

