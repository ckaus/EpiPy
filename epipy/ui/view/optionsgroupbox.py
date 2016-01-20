# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, uic, QtGui

from epipy.ui.model.mainmodel import Event
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
        self.setEnabled(False)
        self.advanced_dialog = None
        self.advanced_btn.setEnabled(False)
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.controller.set_model)

    def show_advanced_dialog(self):
        model = self.controller.get_model()
        if model == 'SIR':
            self.advanced_dialog = SIRAdvancedDialog(self.controller)
        elif model == 'SEIR':
            self.advanced_dialog = SEIRAdvancedDialog(self.controller)
        elif model == 'SIRS':
            self.advanced_dialog = SIRSAdvancedDialog(self.controller)
        self.advanced_dialog.show()

    def get_model_parameters(self):
        parameters = []
        parameter_values = []
        group_box = self.controller.get_model_parameter_group_box()
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                parameters.append((str(widget.text()).lower()))
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                parameter_values.append(widget.value())
        return dict(zip(parameters, parameter_values))

    def update(self, event):
        if event == Event.ENABLE_ADVANCED_BUTTON:
            self.advanced_btn.setEnabled(True)
        elif event == Event.ENABLE_MODEL_PARAMETER_GROUP_BOX:
            self.setEnabled(True)
            if self.controller.get_model():  # one model was choosing before
                self.controller.notify(Event.ENABLE_FIT_BUTTON)
        elif event == Event.DISABLE_MODEL_PARAMETER_GROUP_BOX:
            self.setEnabled(False)
            self.controller.notify(Event.DISABLE_FIT_BUTTON)
        elif event == Event.SHOW_MODEL_PARAMETER_GROUP_BOX:
            if self.layout().itemAt(2):
                self.layout().itemAt(2).widget().setParent(None)
            self.layout().addRow(self.controller.get_model_parameter_group_box())
            self.controller.notify(Event.ENABLE_FIT_BUTTON)
        elif event == Event.FIT_DATA:
            params = self.get_model_parameters()
            self.controller.set_model_parameters(params)
