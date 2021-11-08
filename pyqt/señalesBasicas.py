from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(VentanaPrincipal, self).__init__(*args, **kwargs)
        # señal: la funcion connect se llamara siempre que la ventana titulo ha cambiado. el nuevo titulo se paasara
        # a la funcion
        self.windowTitleChanged.connect(self.onWindowTitleChange)
        # señal: la funcion connect se llamara siempre que la ventana titulo ha cambiado. el nuevo titulo se descarta en el lambda y e se llama a la funcion sin parametros
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        # señal:la funcion coneec se llara siempre que la ventana titulo ha cambiado.el nuevo titulo es pasado a la funcion y reemplaza el parametro por defecto
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        # señal: la funcion connect se llamara siempre que la ventana ha cambiado.el nuevo titulo es pasado a la funcion y reemplaza el parametro por defecto.se pasan datos adicionales desde dentro de lambda
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        # esto establece el titulo de la ventana que activara todas las seañles anteriores enviando el nuevo titulo a las funciones adjuntas o lambdas como el primer parametro
        self.setWindowTitle("mi increible aplicacion") #adwssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
        etiqueta = QLabel("muy interesante")
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

# slot: acepta una cadena por ejemplo el titulo dela ventana y la imprime este es el manejo de la señal que estamso
    # creando es siempre necesario agregarla asi no hagamos uso de ella
    def onWindowTitleChange(self, s):
        None
# slot: tiene parametros predeterminado y se puede llamar sin un valor

    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
app.exec_()
