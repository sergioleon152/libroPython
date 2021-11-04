from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# nuestra clase heredara de QMainWIndow para volverla lo que llaman subclase de QMainWIndow y asi poder editar mejor mi aplicacion


class VentanaPrincipal(QMainWindow):
    # PODEMOS PASARLE CUANTOS ARGUMENTOS QUERAMOS O DEJARLO VACIO TAMBIEN FUNCIONARA
    # def __init__(self):
    #super(VentanaPrincipal, self).__init__()
    def __init__(self, *args, **kwargs):
        super(VentanaPrincipal, self).__init__(*args, **kwargs)
        self.setWindowTitle("mi increible app")
        label = QLabel("esto es increible")

        # el espacio de nombre Qt tiene muchos atributos para personalizar
        # WIDGETS. SEE : http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)
        # ahora estableceremos que siempre la etiqueta este en elcentro asi se expanda la ventana
        self.setCentralWidget(label)


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
app.exec_()
