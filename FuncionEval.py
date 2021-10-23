# la funcion eval lee lo que esta en un string y lo combierte en un tipo de dato que le parezca mas conveniente

# en este momento  ya lo reconocio como un int si metemos entero o float si metemos decimal
# asi ingrese un float con ecval no me tirara error y lo transformara a entero
numero = int(eval(input("ingresa un numero")))

print(numero*2)
a, b, c = eval(input("introduce valores a,byc: "))
