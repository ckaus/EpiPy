# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
SIRSsimpleGroupBoxUI, SIRSsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirssimplegroupbox.ui"))
SIRSwbadGroupBoxUI, SIRSwbadGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "sirswbadgroupbox.ui"))


class SIRSsimpleGroupBox(SIRSsimpleGroupBoxBase, SIRSsimpleGroupBoxUI):
    def __init__(self):
        SIRSsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)


class SIRSwbadGroupBox(SIRSwbadGroupBoxBase, SIRSwbadGroupBoxUI):
    def __init__(self):
        SIRSwbadGroupBoxBase.__init__(self)
        self.setupUi(self)
