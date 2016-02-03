# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.model import sir, seir, sirs
from epipy.ui.view.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.view.sirgroupbox import SIRsimpleGroupBox, SIRwbadGroupBox, SIRvaccineGroupBox
from epipy.ui.view.sirsgroupbox import SIRSsimpleGroupBox, SIRSwbadGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SIRAdvancedDialogUI, SIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "siradvanceddialog.ui"))
SIRSAdvancedDialogUI, SIRSAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "sirsadvanceddialog.ui"))
SEIRAdvancedDialogUI, SEIRAdvancedDialogBase = uic.loadUiType(os.path.join(folder_path, "seiradvanceddialog.ui"))


class SIRAdvancedDialog(SIRAdvancedDialogBase, SIRAdvancedDialogUI):
    """
    This class represents the SIR advanced dialog.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *SIRAdvancedDialog*
    """

    def __init__(self, controller):
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        """
        This function adds a selected model type, contains of view and model class,
        to the controller.
        """
        if self.simple_radio_btn.isChecked():
            self.controller.set_model_group_box(SIRsimpleGroupBox(), sir.Simple())
        elif self.wbad_radio_btn.isChecked():
            self.controller.set_model_group_box(SIRwbadGroupBox(), sir.WithBirthsAndDeaths())
        elif self.vaccine_radio_btn.isChecked():
            self.controller.set_model_group_box(SIRvaccineGroupBox(), sir.Vaccine())


class SEIRAdvancedDialog(SEIRAdvancedDialogBase, SEIRAdvancedDialogUI):
    """
    This class represents the SEIR advanced dialog.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *SEIRAdvancedDialog*
    """

    def __init__(self, controller):
        SEIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        """
        This function adds a selected model type, contains of view and model class,
        to the controller.
        """
        if self.simple_radio_btn.isChecked():
            self.controller.set_model_group_box(SEIRsimpleGroupBox(), seir.Simple())


class SIRSAdvancedDialog(SIRSAdvancedDialogBase, SIRSAdvancedDialogUI):
    """
    This class represents the SIRS advanced dialog.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *SIRSAdvancedDialog*
    """

    def __init__(self, controller):
        SIRSAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        """
        This function adds a selected model type, contains of view and model class,
        to the controller.
        """
        if self.simple_radio_btn.isChecked():
            self.controller.set_model_group_box(SIRSsimpleGroupBox(), sirs.Simple())
        elif self.wbad_radio_btn.isChecked():
            self.controller.set_model_group_box(SIRSwbadGroupBox(), sirs.WithBirthsAndDeaths())
