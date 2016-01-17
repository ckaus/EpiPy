# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRGroupBoxUI, SIRGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirsimplegroupbox.ui"))
SIRwbadGroupBoxUI, SIRwbadGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirwbadgroupbox.ui"))
SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI = uic.loadUiType(os.path.join(folder_path, "sirvaccinegroupbox.ui"))


class SIRGroupBox(SIRGroupBoxBase, SIRGroupBoxUI):
    def __init__(self):
        SIRGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRwbadGroupBox(SIRwbadGroupBoxBase, SIRwbadGroupBoxUI):
    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRvaccineGroupBox(SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI):
    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)
