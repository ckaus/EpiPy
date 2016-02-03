# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SEIRsimpleGroupBoxUI, SEIRsimpleGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "seirsimplegroupbox.ui"))


class SEIRsimpleGroupBox(SEIRsimpleGroupBoxBase, SEIRsimpleGroupBoxUI):
    """
    This class represents the SEIR Simple group box.

    :returns: an instance of *SEIRsimpleGroupBox*
    """

    def __init__(self):
        SEIRsimpleGroupBoxBase.__init__(self)
        self.setupUi(self)
