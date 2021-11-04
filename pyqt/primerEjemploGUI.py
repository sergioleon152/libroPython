from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# solo se necesita para acceder a la linea de comandos
import sys
# solo necesitaremos una (y solo una ) instancia de QApplication por aplicacion
# Pasamos sys.argv para permiter argumentos de linea de conados para la aplicacion
# si sabe que no utilizata argumentos de linea de comandos QApplication([]) tambien funciona
aplicacion = QApplication(sys.argv)
# de esta manera creamos la ventana pero para verla debemos indicarlo
ventana = QMainWindow()
ventana.show()  # las ventanas siempre estan de forma oculta de forma predeterminada


# iniciando el ciclo de eventos esta instruccion siempre va de ultimas
aplicacion.exec_()

# la aplicacio no llegara aqui hasta que termine  y tamibien el  evento
# el bucle se para
