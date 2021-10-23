numero = 1
contador = 0
suma = 0
while numero != 0:
    numero = int(eval(input("ingresa un numero entero ")))
    contador += 1
    print(f"el numero {contador} : {numero}")

    suma = suma+numero
print(f"la suma es {suma}")
