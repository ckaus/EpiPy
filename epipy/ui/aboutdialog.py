# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore

path = os.path.dirname(os.path.abspath(__file__))
AboutDialogUI, AboutDialogBase = uic.loadUiType(
    os.path.join(path, "aboutdialog.ui"))
topText = "EpyPy 1.0"
bottomText = "A Tool for fitting epidemic models.<br />Source: <a href=\"https://github.com/ckaus/EpiPy\">GitHub</a>"

class AboutDialog(AboutDialogBase, AboutDialogUI):
    def __init__(self, parent=None):
    	AboutDialogBase.__init__(self, parent)
    	self.setupUi(self)
    	self.topLabel.setText(topText);
    	self.bottomLabel.setText(bottomText);
    	self.closeButton.clicked.connect(self.close)