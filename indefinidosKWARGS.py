# *args es para pasarle a una funcion endeterminados valores QUE LOS TOMARA COMO UNA TUPLA y **kwargs es pasarle a una funcion indeterminados valores DEFINIDOS  QUE LOS TOMARA  COMO UN DICCIONARIO

def argumentos_como_tuplas(a, b, *argumentos):
    print(a, b)
    print(
        f"en esta variable fue que metimos los argumentos indefinidos y esto se mostrara como una tupla:  {argumentos} ")


def kwargs_como_diccionarios(a, b, **kwargsdicionarios):
    print(a, b)
    print("tenemos que pasarle a los kwargs la variable completa con su valor para que nos pueda mostrar el siguiente diccionario", kwargsdicionarios)


argumentos_como_tuplas(1, 2, 2.22, "yamid", "sergio")
kwargs_como_diccionarios(1, 4, variable1=2.33, varaible2=3, variable3="sergio")
