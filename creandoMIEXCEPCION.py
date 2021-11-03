class exceso_peso(RuntimeError):
    def __init__(self, suma):
        super().__init__()
        self.cantidad = suma


try:
    num1 = eval((input("introduzca el peso del objeto 1:")))

    num2 = eval((input("introduzca el peso del objeto 2:")))
    total = num1+num2
    if total > 100:
        raise exceso_peso(total)
except exceso_peso as obj_error:
    print("no se han guardado los datos")
    print("Motivo el peso total excede el valor maximo(100kg) en: ",
          obj_error.cantidad-100, "KG")
except:
    print("los datos no se han introducido correctamente y no se han guardado")
else:
    print("los datos han sido correctamente guardados")

print("seguimos con el programa")
