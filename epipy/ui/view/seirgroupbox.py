# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class SEIRsimpleGroupBox(QtGui.QGroupBox):
    """This class represents the SEIR Simple group box.

    :returns: an instance of *SEIRsimpleGroupBox*
    """

    def __init__(self):
        super(SEIRsimpleGroupBox, self).__init__()
        loadUi(cwd + '/seirsimplegroupbox.ui', self)
