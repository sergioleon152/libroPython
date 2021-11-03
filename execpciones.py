
try:
    a = 10
    a = al+10
    print("el valor de a es ", a)
except NameError:
    print("error en e el nombre de alguna variable")
except:
    print("Error generico")
else:
    print("bloque try ejecutado sin problemas por eso entramos al else")
finally:
    print("bloque finally ejecutado")
print("seguimos con el programa sin que se nos caiga")

try:
    a = 10
    a = a+10
    print("el valor de a es ", a)
except NameError:
    print("error en e el nombre de alguna variable")
except:
    print("Error generico")
else:
    print("bloque try ejecutado sin problemas por eso entramos al else")
finally:
    print("bloque finally ejecutado")
print("seguimos con el programa sin que se nos caiga ahora para atrapar un error")

try:
    a = 10
    a = al+10
# atrapando la excepcon del error para utilizarla luego
except BaseException as obj_error:
    print("error en la ejecucion del programa")
    print("motivo del error: ", obj_error)
else:
    print("bloque try ejecutado sin problemas por eso entramos al else")
finally:
    print("bloque finally ejecutado")
print("seguimos con el programa ya despues de hacer uso de la varaible dle error")
