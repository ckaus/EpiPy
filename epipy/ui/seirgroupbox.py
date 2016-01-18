# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SEIRsimpleGroupBoxUI, SEIRsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "seirsimplegroupbox.ui"))


class SEIRsimpleGroupBox(SEIRsimpleGroupBoxBase, SEIRsimpleGroupBoxUI):
    def __init__(self):
        SEIRsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)

