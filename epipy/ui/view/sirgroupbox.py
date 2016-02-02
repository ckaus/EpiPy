# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SIRsimpleGroupBoxUI, SIRsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirsimplegroupbox.ui"))
SIRwbadGroupBoxUI, SIRwbadGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirwbadgroupbox.ui"))
SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI = uic.loadUiType(os.path.join(folder_path, "sirvaccinegroupbox.ui"))


class SIRsimpleGroupBox(SIRsimpleGroupBoxBase, SIRsimpleGroupBoxUI):
    """
    This class represents the SIR Simple group box.

    :returns: an instance of *SIRsimpleGroupBox
    """

    def __init__(self):
        SIRsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRwbadGroupBox(SIRwbadGroupBoxBase, SIRwbadGroupBoxUI):
    """
    This class represents the SIR with deaths and births group box.

    :returns: an instance of *SIRwbadGroupBox*
    """

    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRvaccineGroupBox(SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI):
    """
    This class represents the SIR Vaccine group box.

    :returns: an instance of *SIRvaccineGroupBox*
    """

    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)
