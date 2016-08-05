# -*- coding: utf-8 -*-

import os
from PyQt4 import uic
from epipylib.model import sir, sirs, seir

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
    """

    def __init__(self, controller):
        """
        :param controller: the used controller
        :type controller: *SideBarController*
        :returns: an instance of *SIRAdvancedDialog*
        """
        SIRAdvancedDialogBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.button_box.accepted.connect(self.set_selected_radio_btn)

    def set_selected_radio_btn(self):
        if self.simple_radio_btn.isChecked():
            self.controller.set_options_model(SIRsimpleGroupBox(), sir, sir.simple)
        elif self.wbad_radio_btn.isChecked():
            self.controller.set_options_model(SIRwbadGroupBox(), sir, sir.wbad)
        elif self.vaccine_radio_btn.isChecked():
            self.controller.set_options_model(SIRvaccineGroupBox(), sir, sir.vaccine)


class SEIRAdvancedDialog(SEIRAdvancedDialogBase, SEIRAdvancedDialogUI):
    """
    This class represents the SEIR advanced dialog.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *SEIRAdvancedDialog*
    """

    def __init__(self, controller):
        """

        :param controller:
        """
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
            self.controller.set_options_model(SEIRsimpleGroupBox(), seir, seir.simple)


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
            self.controller.set_options_model(SIRSsimpleGroupBox(), sirs, sirs.simple)
        elif self.wbad_radio_btn.isChecked():
            self.controller.set_options_model(SIRSwbadGroupBox(), sirs, sirs.wbad)
