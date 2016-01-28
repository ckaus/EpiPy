# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, uic

from epipy.ui.controller.event import Event
from epipy.ui.view.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    def __init__(self, controller):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.advanced_dialog = None
        self.advanced_btn.setEnabled(False)
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.controller.set_model)
        self.setEnabled(False)

    def show_advanced_dialog(self):
        model = self.controller.get_epidemic_model()
        if model == 'SIR':
            self.advanced_dialog = SIRAdvancedDialog(self.controller)
        elif model == 'SEIR':
            self.advanced_dialog = SEIRAdvancedDialog(self.controller)
        elif model == 'SIRS':
            self.advanced_dialog = SIRSAdvancedDialog(self.controller)
        self.advanced_dialog.show()

    def update(self, event):
        if event == Event.ENABLE_OPTIONS:
            self.setEnabled(True)
        elif event == Event.DISABLE_OPTIONS:
            self.setEnabled(False)
        if event == Event.ENABLE_ADVANCED_BUTTON:
            if not self.advanced_btn.isEnabled():
                self.advanced_btn.setEnabled(True)
        elif event == Event.SHOW_MODEL_PARAMETER_GROUP_BOX:
            if self.layout().itemAt(2):
                self.layout().itemAt(2).widget().setParent(None)
            self.layout().addWidget(self.controller.get_current_model_parameter_group_box(), 3, 0, 3, 3)
        elif event == Event.DISABLE_PARAMETERS:
            self.controller.get_current_model_parameter_group_box().setEnabled(False)
        elif event == Event.ENABLE_PARAMETERS:
            self.controller.get_current_model_parameter_group_box().setEnabled(True)
