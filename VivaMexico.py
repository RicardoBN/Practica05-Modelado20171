from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from datetime import datetime, date, time, timedelta
import calendar
import sys


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("¡Viva México!")
        self.setWindowIcon(QIcon("bandera.png")) 
        self.resize(100, 100)
        self.button = QtGui.QPushButton("Aprietame", self)
        self.heroes = QtGui.QLabel(self)
        layout = QtGui.QVBoxLayout(self)        
        layout.addWidget(self.heroes)
        layout.addStretch()
        layout.addWidget(self.button)
        layout.addStretch()
        self._text = "Gracias a nuestros héroes Migel Hidalgo, José María y Morelos y El pipila Somos libres!!"
        self._index = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(200)
        self.button.pressed.connect(self.on_press)
        self.button.released.connect(self.on_release)           
    
    @pyqtSlot()
    def on_press(self):
        texto = tiempoFaltante()         
        self.button.setText(texto)
        
   
    @pyqtSlot()
    def on_release(self):
    
        self.button.setText("Aprietame")
        
  
    

    
    def handleTimer(self):
        self._index += 1
        self.heroes.setText(self._text[:self._index])
        if self._index > len(self._text):
            self.timer.stop()

def tiempoFaltante():
        hoy = datetime.now()   # Asigna datetime de la fecha actual
        hoyT = datetime(hoy.year, 9, 16, 0, 0, 0)
        dif = hoyT - hoy
        days, hours, minutes = dif.days, dif.seconds // 3600, dif.seconds // 60 % 60
        if(dif.days < 365 and dif.days >= 0):
            x = "Faltan: "+str(dif.days)+" dias, "+str(hours)+" horas y "+str(minutes)+" minutos para el siguiente grito!!"
            return x
        else:      
            anioSig = datetime(hoy.year+1, 9, 16, 0, 0, 0)  # Asigna datetime específica
            dif= anioSig - hoy    
            months, hours, minutes = dif.days/30, dif.seconds // 3600, dif.seconds // 60 % 60  
            x = "Faltan: "+str(dif.days)+" dias, "+str(hours)+" horas y "+str(minutes)+" minutos para el siguiente grito!!"
            return x

    

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())