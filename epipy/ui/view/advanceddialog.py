# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd
from epipylib.model import sir, sirs, seir
from epipy.ui.view.sirgroupbox import *
from epipy.ui.view.seirgroupbox import *
from epipy.ui.view.sirsgroupbox import *


class SIRAdvancedDialog(QtGui.QDialog):
    """This class represents the SIR advanced dialog.

    :returns: an instance of *SIRAdvancedDialog*
    """

    def __init__(self):
        super(SIRAdvancedDialog, self).__init__()
        loadUi(cwd + '/siradvanceddialog.ui', self)

    def get_selected_model(self):
        """Returns the correct model group box and model based
        on selection.

        :returns: the model groupbox, model module and model
        :rtype: tuple(*QGroupbox*, Module, Func)
        """
        if self.simple_radio_btn.isChecked():
            return SIRsimpleGroupBox(), sir, sir.simple
        elif self.wbad_radio_btn.isChecked():
            return SIRwbadGroupBox(), sir, sir.wbad
        elif self.vaccine_radio_btn.isChecked():
            return SIRvaccineGroupBox(), sir, sir.vaccine
        return None, None, None


class SEIRAdvancedDialog(QtGui.QDialog):
    """
    This class represents the SEIR advanced dialog.

    :returns: an instance of *SEIRAdvancedDialog*
    """

    def __init__(self):
        super(SEIRAdvancedDialog, self).__init__()
        loadUi(cwd + '/seiradvanceddialog.ui', self)

    def get_selection(self):
        """Returns the correct model group box and model based
        on selection.

        :returns: the model groupbox, model module and model
        :rtype: tuple(*QGroupbox*, Module, Func)
        """
        if self.simple_radio_btn.isChecked():
            return SEIRsimpleGroupBox(), seir, seir.simple
        return None, None, None


class SIRSAdvancedDialog(QtGui.QDialog):
    """
    This class represents the SIRS advanced dialog.

    :returns: an instance of *SIRSAdvancedDialog*
    """

    def __init__(self, controller):
        super(SIRSAdvancedDialog, self).__init__()
        loadUi(cwd + '/sirsadvanceddialog.ui', self)

    def get_selection(self):
        """Returns the correct model group box and model based
        on selection.

        :returns: the model groupbox, model module and model
        :rtype: tuple(*QGroupbox*, Module, Func)
        """
        if self.simple_radio_btn.isChecked():
            return SIRSsimpleGroupBox(), sirs, sirs.simple
        elif self.wbad_radio_btn.isChecked():
            return SIRSwbadGroupBox(), sirs, sirs.wbad
        return None, None, None
