# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRAdvancedDialogUI, SIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "siradvanceddialog.ui"))


class SIRAdvancedDialog(SIRAdvancedDialogBase, SIRAdvancedDialogUI):
    def __init__(self):
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)

