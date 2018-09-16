
from PyQt4 import QtGui, QtCore
from pyqtgraph import PlotWidget
import numpy as np
import time
import rt_function

class Interface(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(740, 480)
        self.move(300, 300)
        self.setWindowTitle('plotting')

        self.reset_button = QtGui.QPushButton('Reset', self)
        self.reset_button.resize(200, 30)
        self.reset_button.move(10, 10)
        self.reset_button.clicked.connect(self.on_reset_button_clicked)

        self.period_spin_box_label = QtGui.QLabel("Period (s)", self)
        self.period_spin_box_label.resize(90, 30)
        self.period_spin_box_label.move(10, 50)
        self.period_spin_box = QtGui.QDoubleSpinBox(self)
        self.period_spin_box.resize(70, 30)
        self.period_spin_box.move(140, 50)
        self.period_spin_box.valueChanged.connect(self.on_period_spin_box_changed)


        self.periods_to_show_spin_box_label = QtGui.QLabel("Periods to show", self)
        self.periods_to_show_spin_box_label.resize(100, 30)
        self.periods_to_show_spin_box_label.move(10, 90)
        self.periods_to_show_spin_box = QtGui.QDoubleSpinBox(self)
        self.periods_to_show_spin_box.resize(70, 30)
        self.periods_to_show_spin_box.move(140, 90)
        self.periods_to_show_spin_box.valueChanged.connect(self.on_periods_to_show_spin_box_changed)

        self.plotting_widget = PlotWidget(parent=self)
        self.plotting_widget.resize(510, 460)
        self.plotting_widget.move(220, 10)

        self.rt_function = rt_function.RTFunction('3*np.pi*np.exp(5*np.sin(2*np.pi*1*t))')
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        self.timestamps = np.array([])
        self.data = np.array([])

        self.period = 1
        self.period_spin_box.setValue(self.period)
        self.periods_to_show = 2
        self.periods_to_show_spin_box.setValue((self.periods_to_show))

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

    def on_period_spin_box_changed(self):
        """Handles the period spin box, to adjust the time of one period"""
        self.period = self.period_spin_box.value()

    def on_periods_to_show_spin_box_changed(self):
        """Handles the periods_to_show spin box, to adjust how many periods are to be shown"""
        self.periods_to_show = self.periods_to_show_spin_box.value()