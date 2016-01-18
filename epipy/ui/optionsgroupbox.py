# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui
from epipy.ui.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog
from epipy.ui.sirgroupbox import SIRsimpleGroupBox
from epipy.ui.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.sirsgroupbox import SIRSsimpleGroupBox


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    def __init__(self):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.current_group_box = None
        self.current_advanced_dialog = SIRAdvancedDialog(self)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.init_model_param_group_box)

    def init_model_param_group_box(self, selected_item):
        if selected_item == QtCore.QString('SIR'):
            self.current_advanced_dialog = SIRAdvancedDialog(self)
            self.add_model_parameter_group_box(SIRsimpleGroupBox())
        elif selected_item == QtCore.QString('SEIR'):
            self.current_advanced_dialog = SEIRAdvancedDialog(self)
            self.add_model_parameter_group_box(SEIRsimpleGroupBox())
        elif selected_item == QtCore.QString('SIRS'):
            self.current_advanced_dialog = SIRSAdvancedDialog(self)
            self.add_model_parameter_group_box(SIRSsimpleGroupBox())

    def add_model_parameter_group_box(self, model_parameter_group_box):
        if self.current_group_box is not None:  # is called only at the beginning
            self.current_group_box.deleteLater()
        self.layout().addRow(model_parameter_group_box)
        self.current_group_box = model_parameter_group_box

    def show_advanced_dialog(self):
        self.current_advanced_dialog.show()
