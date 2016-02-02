# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SIRSsimpleGroupBoxUI, SIRSsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirssimplegroupbox.ui"))
SIRSwbadGroupBoxUI, SIRSwbadGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirswbadgroupbox.ui"))


class SIRSsimpleGroupBox(SIRSsimpleGroupBoxBase, SIRSsimpleGroupBoxUI):
    """
    This class represents the SIRS Simple group box.

    :returns: an instance of *SIRvaccineGroupBox*
    """

    def __init__(self):
        SIRSsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRSwbadGroupBox(SIRSwbadGroupBoxBase, SIRSwbadGroupBoxUI):
    """
    This class represents the SIRS with births and deaths group box.

    :returns: an instance of *SIRSwbadGroupBox*
    """

    def __init__(self):
        SIRSwbadGroupBoxBase.__init__(self)
        self.setupUi(self)
