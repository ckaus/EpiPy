# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class SEIRsimpleGroupBox(QtGui.QDialog):
    """This class represents the SEIR Simple group box.

    :returns: an instance of *SEIRsimpleGroupBox*
    """

    def __init__(self):
        super(SEIRSsimpleGroupBox, self).__init__()
        loadUi(cwd + '/seirssimplegroupbox.ui', self)
