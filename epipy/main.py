# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from epipy.ui.controller.mainviewcontroller import MainViewController

from epipy.ui.view.mainwindow import MainWindow

"""
EpiPy start point.
"""
app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window_controller = MainViewController(main_window)
main_window_controller.run()
sys.exit(app.exec_())
