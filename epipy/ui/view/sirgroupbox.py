# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class SIRsimpleGroupBox(QtGui.QGroupBox):
    """This class represents the SIR Simple group box.

    :returns: an instance of *SIRsimpleGroupBox*
    """

    def __init__(self):
        super(SIRsimpleGroupBox, self).__init__()
        loadUi(cwd + '/sirsimplegroupbox.ui', self)


class SIRwbadGroupBox(QtGui.QGroupBox):
    """This class represents the SIR with deaths and births group box.

    :returns: an instance of *SIRwbadGroupBox*
    """

    def __init__(self):
        super(SIRwbadGroupBox, self).__init__()
        loadUi(cwd + '/sirwbadgroupbox.ui', self)


class SIRvaccineGroupBox(QtGui.QGroupBox):
    """This class represents the SIR Vaccine group box.

    :returns: an instance of *SIRvaccineGroupBox*
    """

    def __init__(self):
        super(SIRvaccineGroupBox, self).__init__()
        loadUi(cwd + '/sirvaccinegroupbox.ui', self)
