# -*- coding: utf-8 -*-
import os
from PyQt4 import uic

path = os.path.dirname(os.path.abspath(__file__))
MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(path, 'mainwindow.ui'))

class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self, parent=None):
        MainWindowBase.__init__(self, parent)
        self.setupUi(self)