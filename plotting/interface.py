
from PyQt4 import QtGui
from pyqtgraph import PlotWidget
import numpy as np

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

        self.plotting_widget = PlotWidget(parent=self)
        self.plotting_widget.resize(510, 460)
        self.plotting_widget.move(120, 10)

        data = np.array([1,2,3,4])
        self.plotting_widget.plot(data)

        self.show()


    def on_reset_button_clicked(self):
        print("reset")