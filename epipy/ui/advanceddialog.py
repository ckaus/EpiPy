# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.model import sir, seir, sirs
from epipy.ui.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.sirgroupbox import SIRsimpleGroupBox, SIRwbadGroupBox, SIRvaccineGroupBox
from epipy.ui.sirsgroupbox import SIRSsimpleGroupBox, SIRSwbadGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRAdvancedDialogUI, SIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "siradvanceddialog.ui"))
SIRSAdvancedDialogUI, SIRSAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "sirsadvanceddialog.ui"))
SEIRAdvancedDialogUI, SEIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "seiradvanceddialog.ui"))


class SIRAdvancedDialog(SIRAdvancedDialogBase, SIRAdvancedDialogUI):
    def __init__(self, options_controller):
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.options_controller = options_controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.options_controller.update(self, SIRsimpleGroupBox(), sir.Simple())
        elif self.wbad_radio_btn.isChecked():
            self.options_controller.update(self, SIRwbadGroupBox(), sir.WithBirthsAndDeaths())
        elif self.vaccine_radio_btn.isChecked():
            self.options_controller.update(self, SIRvaccineGroupBox(), sir.Vaccine())


class SEIRAdvancedDialog(SEIRAdvancedDialogBase, SEIRAdvancedDialogUI):
    def __init__(self, options_controller):
        SEIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.options_controller = options_controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.options_controller.update(self, SIERsimpleGroupBox(), seir.Simple())


class SIRSAdvancedDialog(SIRSAdvancedDialogBase, SIRSAdvancedDialogUI):
    def __init__(self, options_controller):
        SIRSAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.options_controller = options_controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.options_controller.update(self, SIRSsimpleGroupBox(), sirs.Simple())
        elif self.wbad_radio_btn.isChecked():
            self.options_controller.update(self, SIRSwbadGroupBox(), sirs.WithBirthsAndDeaths())
