# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class SIRSsimpleGroupBox(QtGui.QGroupBox):
    """This class represents the SIRS Simple group box.

    :returns: an instance of *SIRSsimpleGroupBox*
    """

    def __init__(self):
        super(SIRSsimpleGroupBox, self).__init__()
        loadUi(cwd + '/sirssimplegroupbox.ui', self)


class SIRSwbadGroupBox(QtGui.QGroupBox):
    """This class represents the SIRS with births and deaths group box.

    :returns: an instance of *SIRSwbadGroupBox*
    """

    def __init__(self):
        super(SIRSwbadGroupBox, self).__init__()
        loadUi(cwd + '/sirswbadgroupbox.ui', self)
