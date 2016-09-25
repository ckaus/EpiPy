# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from epipy.ui.controller.mainwindowcontroller import MainWindowController

"""EpiPy start point."""

app = QtGui.QApplication(sys.argv)
controller = MainWindowController()
controller.view.show()
sys.exit(app.exec_())
