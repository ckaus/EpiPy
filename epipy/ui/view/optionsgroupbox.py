# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    def __init__(self):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
