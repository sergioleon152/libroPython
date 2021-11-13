from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(VentanaPrincipal, self).__init__(*args,**kwargs)
        self.setWindowTitle("mi primera ventana")
        etiqueta=QLabel("super app")
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        herramientas=QToolBar("Barra Herramientas")
        #antes de agregar la barra de herramientas a la ventana le diremos de cuanto sera el tamaño de los iconos o si no los mostrara horrible , los iconos son los uqe le pasaremos a los QAction como primer argumento
        herramientas.setIconSize(QSize(12,12))


        self.addToolBar(herramientas)
        #usando señales esto lo sabemos cada vez que hago uso de la funcion connect
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.setWindowTitle("buena crack")
        #ahora vamos a crear un QAction qeu es como un boton que sirve para tener tanto comandos en la barra de herramientas como el menu ejemplo la opcion de cortar cuando damos cont+x o cuando le damos en el menu seria toda una misma gracias a este objeto para darle un icono se le pasa como primer argumento
        botonAccion=QAction(QIcon(r"iconos/fugue-icons-3.5.6/icons-shadowless/edit.png"),"edit",self)
        botonAccion.setStatusTip("este es el boton de editar")
        botonAccion.triggered.connect(self.onMyToolBarButtonClick)
        botonAccion.setCheckable(True)
       

        herramientas.addAction(botonAccion)
        

        #ahora crearems un statusbar #esto nos muestra el texto que pongamos con el setStatusTip
        self.setStatusBar(QStatusBar(self))
        #-------------------------------------------------------
        #ahora agregaremos un apr mas de botones y cosas locas osea widgets para y un separador
        herramientas.addSeparator()
        botonAccion2=QAction(QIcon(r"iconos/fugue-icons-3.5.6/icons-shadowless/color.png"),"file",self)
        botonAccion2.setStatusTip("boron de archivo")
        botonAccion2.triggered.connect(self.onMyToolBarButtonClick)
        botonAccion2.setCheckable(True)
        herramientas.addAction(botonAccion2)
        #---------------------------------
        #agregando algunos widgts a la barra de herramientas
        herramientas.addSeparator()
        herramientas.addWidget(QLineEdit())
        herramientas.addSeparator()
        herramientas.addWidget(QDateEdit())
        #-------------------------------------------
        #aca le estamos diciendo que aparezca el texto del boton al lado del icono que colocamos pero si queremos podemos omitir esto y solo aparecera el icono o podemos seleccionar otras opciones
        herramientas.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.addToolBar(herramientas)


    #y aca estamos usando el slot por defecto del click ara nuestro QACTIONBUTTON
    def onMyToolBarButtonClick(self,s):
        print("click ",s)


    #este sera el slot de la señal de cuando cambia el titulo de la ventana
    def my_custom_fn(self):
        print("cambio el titulo de la funcion")


app=QApplication(sys.argv)
ven = VentanaPrincipal()
ven.show()
app.exec_()
