
from PyQt4 import QtGui

class Interface(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.move(300, 300)
        self.setWindowTitle('plotting')


        self.reset_button = QtGui.QPushButton('Reset', self)
        self.reset_button.resize(100, 30)
        self.reset_button.move(10, 10)
        self.reset_button.clicked.connect(self.on_reset_button_clicked)

        self.show()


    def on_reset_button_clicked(self):
        print("reset")