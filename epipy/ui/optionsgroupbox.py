# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore, QtGui

from epipy.model import sir, seir, sirs
from epipy.ui.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog
from epipy.ui.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.sirgroupbox import SIRsimpleGroupBox
from epipy.ui.sirsgroupbox import SIRSsimpleGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    def __init__(self, main_window):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.current_group_box = None
        self.current_advanced_dialog = SIRAdvancedDialog(self)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.init_model_param_group_box)
        self.main_window = main_window
        self.available_spin_boxes = []
        self.available_parameters = []
        self.model = None

    def init_model_param_group_box(self, selected_item):
        if selected_item == QtCore.QString('SIR'):
            self.current_advanced_dialog = SIRAdvancedDialog(self)
            self.add_model_parameter_group_box(SIRsimpleGroupBox())
            self.model = sir.Simple()
        elif selected_item == QtCore.QString('SEIR'):
            self.current_advanced_dialog = SEIRAdvancedDialog(self)
            self.add_model_parameter_group_box(SEIRsimpleGroupBox())
            self.model = seir.Simple()
        elif selected_item == QtCore.QString('SIRS'):
            self.current_advanced_dialog = SIRSAdvancedDialog(self)
            self.add_model_parameter_group_box(SIRSsimpleGroupBox())
            self.model = sirs.Simple()

    def add_model_parameter_group_box(self, model_parameter_group_box):
        # reset - function is called if a new options group box is added
        self.available_spin_boxes = []
        self.available_parameters = []

        if self.current_group_box is not None:  # is called only at the beginning
            self.current_group_box.deleteLater()
        self.layout().addRow(model_parameter_group_box)
        self.current_group_box = model_parameter_group_box
        layout = self.current_group_box.layout()
        # add handler to spin boxes and imagine available labels
        for i in range(0, layout.count()):
            widget = layout.itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                self.available_parameters.append(widget.text())
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                self.available_spin_boxes.append(widget)
                widget.valueChanged.connect(self.inform_main_window)

    def inform_main_window(self):
        # prepare parameters based on labels and spin boxes
        values = []
        for spin_box in self.available_spin_boxes:
            values.append(spin_box.value())
        available_parameters = self.available_parameters
        available_parameters = [str(item).lower() for item in available_parameters]
        param = dict(zip(available_parameters, values))
        self.main_window.update_parameters(param)

    def show_advanced_dialog(self):
        self.current_advanced_dialog.show()
