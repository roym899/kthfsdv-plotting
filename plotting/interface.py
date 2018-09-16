
from PyQt4 import QtGui, QtCore
from pyqtgraph import PlotWidget
import numpy as np
import time
import rt_function

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

        self.rt_function = rt_function.RTFunction('3*np.pi*np.exp(5*np.sin(2*np.pi*1*t))')
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(20)

        self.timestamps = np.array([])
        self.data = np.array([])

        self.periods_to_show = 2
        self.period = 1

    def update(self):
        """Callback for updating for sampling the function and updating the plotting widget"""
        self.plotting_widget.clear()


        t, data = self.rt_function.sample()
        current_time = time.time()
        self.timestamps = np.append(self.timestamps, t)
        self.data = np.append(self.data, data)
        self.plotting_widget.plot(self.timestamps-current_time, self.data)
        rm_idx = np.where(current_time - self.timestamps >= self.period*self.periods_to_show)[0]
        self.timestamps = np.delete(self.timestamps, rm_idx)
        self.data = np.delete(self.data, rm_idx)

    def on_reset_button_clicked(self):
        """Handles the reset button, clears the datapoints"""
        self.timestamps = np.array([])
        self.data = np.array([])
