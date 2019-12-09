from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5.QtWidgets import *
from ip import *

class Menu:

    def __init__(self):

        #self.datos = datos
        self.window = QMainWindow()
        self.window.setWindowTitle("CrackMan-IpCalculator")
        self.window.setStyleSheet("background:url(fondo.jpg)")
        self.window.setFixedSize(720,580)
        self.colocarBotones()
        self.ipe =""

    def colocarBotones(self):

        self.linea = QLineEdit(self.window)
        self.linea.setGeometry(20,22,100,30)
        self.linea.setStyleSheet("background:#ECF0F1")

        self.prefijo = QLabel(self.window)
        self.prefijo.setGeometry(130,22,50,30)
        self.prefijo.setStyleSheet("background:#ECF0F1")

        self.clase = QLabel(self.window)
        self.clase.setGeometry(190,22,50,30)
        self.clase.setStyleSheet("background:#ECF0F1")

        self.mask = QLabel(self.window)
        self.mask.setGeometry(250,22,100,30)
        self.mask.setStyleSheet("background:#ECF0F1")

        self.tipe = QLabel(self.window)
        self.tipe.setGeometry(370,22,80,30)
        self.tipe.setStyleSheet("background:#ECF0F1")

        self.info = QPushButton(self.window)
        self.info.setText("Información")
        self.info.setStyleSheet("background:#FEFB63")
        self.info.setGeometry(20,60,100,30)
        self.info.clicked.connect(self.informacion)

        self.opcion = QComboBox(self.window)
        self.opcion.addItems(["host","subredes"])
        self.opcion.setStyleSheet("background:#FEFB63")
        self.opcion.setGeometry(20,115,120,30)
        #self.opcion.clicked.connect(self.informacion)

        self.numSub = QLineEdit(self.window)
        self.numSub.setGeometry(150,115,100,30)
        self.numSub.setStyleSheet("background:#ECF0F1")

        self.calcular = QPushButton(self.window)
        self.calcular.setText("Calcular")
        self.calcular.setGeometry(255,115,100,30)
        self.calcular.setStyleSheet("background:#FEFB63")
        self.calcular.clicked.connect(self.DatosCalculo)

        self.respuestas = QListWidget(self.window)
        self.respuestas.setStyleSheet("background:#ECF0F1")
        self.respuestas.setGeometry(20,220,300,300)

        self.respuestas2 = QListWidget(self.window)
        self.respuestas2.setStyleSheet("background:#ECF0F1")
        self.respuestas2.setGeometry(350,220,300,300)

        self.datoSubredes = QLabel(self.window)
        self.datoSubredes.setGeometry(480,115,100,30)
        self.datoSubredes.setStyleSheet("background:#ECF0F1")

        self.datoHost = QLabel(self.window)
        self.datoHost.setGeometry(370,115,90,30)
        self.datoHost.setStyleSheet("background:#ECF0F1")

        self.maskSubred = QLabel(self.window)
        self.maskSubred.setGeometry(605,115,110,30)
        self.maskSubred.setStyleSheet("background:#ECF0F1")

        self.subred = QPushButton(self.window)
        self.subred.setText("Listar subRedes")
        self.subred.setStyleSheet("background:#FEFB63")
        self.subred.setGeometry(110,180,100,30)
        self.subred.clicked.connect(self.listarSubredes)

        self.host = QPushButton(self.window)
        self.host.setText("Listar Host")
        self.host.setStyleSheet("background:#FEFB63")
        self.host.setGeometry(380,180,100,30)
        self.host.clicked.connect(self.listarHost)

        self.refrescaH = QPushButton(self.window)
        self.refrescaH.setText("Refrescar Host!")
        self.refrescaH.setStyleSheet("background:#FEFB63")
        self.refrescaH.setGeometry(550,180,100,30)
        self.refrescaH.clicked.connect(self.refrescarHost)

        self.refresca = QPushButton(self.window)
        self.refresca.setText("Refrescar!")
        self.refresca.setStyleSheet("background:#FEFB63")
        self.refresca.setGeometry(500,530,100,30)
        self.refresca.clicked.connect(self.refrescar)

      
    def informacion(self):

        self.entrada = self.linea.text()

        if(self.entrada == ''):
            self.error = QMessageBox.about(self.window,"Error","Duermete otro rato we")
            self.error.show()
        else:
            self.ipe = ip(self.entrada)
            self.ipe.tipo()
            self.prefijo.setStyleSheet("background:#76D7C4")
            self.prefijo.setText(self.ipe.prefijo)
            self.tipe.setStyleSheet("background:#76D7C4")
            self.tipe.setText(self.ipe.typo)
            self.clase.setStyleSheet("background:#76D7C4")
            self.clase.setText(self.ipe.clase)
            self.mask.setStyleSheet("background:#76D7C4")
            self.mask.setText(self.ipe.mask)
    
    def DatosCalculo(self):
        op = self.opcion.currentText()
        num_sub = int(self.numSub.text())

        if(op == "subredes"):

            self.ipe.SubNetC(num_sub)

            if(self.ipe.clase is 'C'):
                self.datoHost.setText(str(self.ipe.numHost()))
                self.datoSubredes.setText(str(num_sub))
                self.maskSubred.setText(self.ipe.mascaraSubred())
            
            elif(self.ipe.clase is 'B'):
                self.datoHost.setText(str(self.ipe.numHost()))
                self.datoSubredes.setText(str(num_sub))
                self.maskSubred.setText(self.ipe.mascaraSubred())
            
            else:
                self.datoHost.setText(str(self.ipe.numHost()))
                self.datoSubredes.setText(str(num_sub))
                self.maskSubred.setText(self.ipe.mascaraSubred())


           
        elif(op == "host"):
            self.ipe.subRedesHost(num_sub)

            if(self.ipe.clase is 'B'):
                self.datoHost.setText(str(num_sub))
                self.datoSubredes.setText(str(self.ipe.numSub))
                self.maskSubred.setText(self.ipe.mascaraSubred())
            
            elif(self.ipe.clase is 'C'):
                self.datoHost.setText(str(num_sub))
                self.datoSubredes.setText(str(self.ipe.numSub))
                self.maskSubred.setText(self.ipe.mascaraSubred())
            else:
                self.datoHost.setText(str(num_sub))
                self.datoSubredes.setText(str(self.ipe.numSub))
                self.maskSubred.setText(self.ipe.mascaraSubred())

    

    def listarSubredes(self):
        self.respuestas.addItems(self.ipe.subRedes)
    

    def listarHost(self):

        if(self.ipe.clase == 'C'):
        
            self.ipe.calcularHostC(self.respuestas.currentItem().text())
            self.respuestas2.addItems(self.ipe.host)
        
        elif(self.ipe.clase == 'B'):
            self.ipe.calcularHostB(self.respuestas.currentItem().text())
            self.respuestas2.addItems(self.ipe.host)
  
   
        
    
    def refrescar(self):
        self.linea.setText(" ")
        self.prefijo.setText(" ")
        self.clase.setText(" ")
        self.mask.setText(" ")
        self.tipe.setText(" ")
        self.numSub.setText(" ")
        self.datoSubredes.setText(" ")
        self.datoHost.setText(" ")
        self.maskSubred.setText(" ")
        self.respuestas.clear()
        self.respuestas2.clear()
    
    def refrescarHost(self):
        self.ipe.host = [ ]
        self.respuestas2.clear()
 
      
    def Mostrar(self):
        self.window.show()
      

app = QApplication(sys.argv)

m = Menu()
m.Mostrar()

app.exec_()

