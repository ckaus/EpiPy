# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

#from epipy.ui.mainwindow import MainWindow
from epipy.ui.epipy_gui import MainWindow

"""
EpiPy start point.
"""

app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())


