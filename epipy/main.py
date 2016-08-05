# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from epipy.ui.controller.mainwindowcontroller import MainWindowController
from epipy.ui.view.mainwindow import MainWindow

"""
EpiPy start point.
"""

app = QtGui.QApplication(sys.argv)

main_window_controller = MainWindowController()
main_view = MainWindow(main_window_controller)
main_view.show()

sys.exit(app.exec_())
