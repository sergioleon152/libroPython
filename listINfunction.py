def elevar_2(numeber: int, lista: list):  # al poner el tipo de dato podemos omiter esto apra pasar la lista osea cualquier tipo de tato puede pasarse sim tener que poner el tipo de dato si no que lo hacemos para que la funcion sepa que tene que esperar
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    numeber **= 2


def main():
    numero = 10
    lista = [1, 2, 3, 4, 5]
    print(f"lista original{lista},lnumero original {numero}")
    elevar_2(numero, lista)
    print(
        f"numero despues del llamado de la funcion{numero},lista despies del llamdo de la funcion {lista}")


main()
