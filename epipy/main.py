# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from epipy.ui.controller.mainviewcontroller import MainViewController
from epipy.ui.model.mainmodel import MainModel
from epipy.ui.view.mainwindow import MainWindow

"""
EpiPy start point.
"""
app = QtGui.QApplication(sys.argv)
main_model = MainModel()
main_controller = MainViewController()
main_view = MainWindow(main_controller)
main_view.show()
sys.exit(app.exec_())
