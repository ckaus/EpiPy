# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRAdvancedDialogUI, SIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "siradvanceddialog.ui"))


class SIRAdvancedDialog(SIRAdvancedDialogBase, SIRAdvancedDialogUI):
    def __init__(self, option_group_box):
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.option_group_box = option_group_box
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.option_group_box.add_model_param_gb(QtCore.QString('SIR'))
        elif self.wbad_radio_btn.isChecked():
            self.option_group_box.add_model_param_gb(QtCore.QString('SIRwbad'))
        elif self.vaccine_radio_btn.isChecked():
            self.option_group_box.add_model_param_gb(QtCore.QString('SIRvaccine'))
