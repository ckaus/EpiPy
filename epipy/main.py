# -*- coding: utf-8 -*-

import sys,os
from PyQt4 import QtCore, QtGui, uic
from epipy.ui.mainwindow import MainWindow

"""
EpiPy start point.
"""
print 'nope'
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
