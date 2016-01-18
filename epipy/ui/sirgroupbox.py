# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRsimpleGroupBoxUI, SIRsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirsimplegroupbox.ui"))
SIRwbadGroupBoxUI, SIRwbadGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirwbadgroupbox.ui"))
SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI = uic.loadUiType(os.path.join(folder_path, "sirvaccinegroupbox.ui"))


class SIRsimpleGroupBox(SIRsimpleGroupBoxBase, SIRsimpleGroupBoxUI):
    def __init__(self):
        SIRsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRwbadGroupBox(SIRwbadGroupBoxBase, SIRwbadGroupBoxUI):
    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRvaccineGroupBox(SIRvaccineGroupBoxBase, SIRvaccineGroupBoxUI):
    def __init__(self):
        SIRwbadGroupBoxBase.__init__(self)
        self.setupUi(self)
