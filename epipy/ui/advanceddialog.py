# -*- coding: utf-8 -*-

import os
from PyQt4 import uic
from epipy.ui.sirgroupbox import SIRsimpleGroupBox, SIRwbadGroupBox, SIRvaccineGroupBox
from epipy.ui.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.sirsgroupbox import SIRSsimpleGroupBox, SIRSwbadGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRAdvancedDialogUI, SIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "siradvanceddialog.ui"))
SIRSAdvancedDialogUI, SIRSAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "sirsadvanceddialog.ui"))
SEIRAdvancedDialogUI, SEIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "seiradvanceddialog.ui"))


class SIRAdvancedDialog(SIRAdvancedDialogBase, SIRAdvancedDialogUI):
    def __init__(self, option_group_box):
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.option_group_box = option_group_box
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SIRsimpleGroupBox())
        elif self.wbad_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SIRwbadGroupBox())
        elif self.vaccine_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SIRvaccineGroupBox())


class SEIRAdvancedDialog(SEIRAdvancedDialogBase, SEIRAdvancedDialogUI):
    def __init__(self, option_group_box):
        SEIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.option_group_box = option_group_box
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SEIRsimpleGroupBox())


class SIRSAdvancedDialog(SIRSAdvancedDialogBase, SIRSAdvancedDialogUI):
    def __init__(self, option_group_box):
        SIRSAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.option_group_box = option_group_box
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SIRSsimpleGroupBox())
        elif self.wbad_radio_btn.isChecked():
            self.option_group_box.add_model_parameter_group_box(SIRSwbadGroupBox())
