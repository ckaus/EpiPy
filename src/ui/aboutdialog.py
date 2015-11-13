# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore

path = os.path.dirname(os.path.abspath(__file__))
AboutDialogUI, AboutDialogBase = uic.loadUiType(
    os.path.join(path, "aboutdialog.ui"))

class AboutDialog(AboutDialogBase, AboutDialogUI):
    def __init__(self, parent=None):
    	AboutDialogBase.__init__(self, parent)
    	self.setupUi(self)
    	self.okButton.clicked.connect(self.close)