"""__main__.py: Entry point to the application.
                __main__.py is exectuted when python3 dir_name gets executed"""


import interface
import sys
from PyQt4 import QtGui


app = QtGui.QApplication(sys.argv)
user_interface = interface.Interface()
sys.exit(app.exec_())