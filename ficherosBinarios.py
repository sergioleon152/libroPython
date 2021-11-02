f = open(r"clientes.txt", "wb+")
f.write(b"Sergio Andres Leon Arango")
f.write(b"yamid julian leon arango")
f.write(b"adriana maria arango mira")
suma = 0
col = eval(input("introduce el numero de la columna a extraer 1-3"))
while 1 > col > 3:
    col = eval(input("numero equivocado intorduce de nuevo el numero de columna"))
num = eval(input("introduce el numero de registros a extrear"))
for i in range(num):
    if i == 0:

        f.seek((col-1)*10, 0)
    else:
        f.seek(((col-1)*10 + 50*1), 0)
    dato = f.read(10)
    if dato != b'':
        print(dato)
        if col == 3:
            suma += float(dato)
    else:
        print("hemos llegado al final del fichero")
        break
if col == 3:
    print("la suma en todos los registros indicados es ", suma)
f.seek(1, 0)
print("el con tenido de todo el fichero en forma de lista es ", list(f))
f.close()
