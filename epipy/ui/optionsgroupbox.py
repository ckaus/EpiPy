# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui
from epipy.ui.sirgroupbox import SIRGroupBox
from epipy.ui.advanceddialog import SIRAdvancedDialog

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    def __init__(self):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.current_group_box = None
        self.current_advanced_dialog = None
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.advanced_btn.setEnabled(False)
        # disable first item of model box in option groupbox
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.add_model_param_gb)

    def add_model_param_gb(self, model_name):
        if self.current_group_box:
            self.current_group_box.hide()
        if model_name == QtCore.QString('SIR'):
            # self.current_model_group_box = SIRGroupBox()
            self.current_group_box = SIRGroupBox()
            self.layout().addRow(self.current_group_box)
            self.advanced_btn.setEnabled(True)

    def show_advanced_dialog(self):
        self.current_advanced_dialog = SIRAdvancedDialog()
        self.current_advanced_dialog.show()
        print "Show advanced dialog"

