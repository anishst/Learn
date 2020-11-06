import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Anish PyQT app")
        label = QLabel("This is aweseome\nNew Line")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def onWindowTitleChange(self,s):
        print(s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

        