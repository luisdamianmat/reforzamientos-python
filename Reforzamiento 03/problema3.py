def sum_dig(numero):
    suma = 0
    while numero<=0:
        print("digite nuevamente")
        numero = int(input("digite un numero: "))

    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    print(f"La suma de digitos es: {suma}")

a = int(input('Digite um numero: '))
sum_dig(a)