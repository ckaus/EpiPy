# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from epipy.ui.controller.controllerservice import ControllerService
from epipy.ui.controller.mainwindowcontroller import MainWindowController
from epipy.ui.view.mainwindow import MainWindow

"""
EpiPy start point.
"""
app = QtGui.QApplication(sys.argv)
controller_service = ControllerService()
main_view_controller = MainWindowController(controller_service)
main_view = MainWindow(main_view_controller)
main_view.show()
sys.exit(app.exec_())
