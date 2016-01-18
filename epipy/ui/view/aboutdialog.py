# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(dir_name(__file__))), 'resources/ui')
AboutDialogUI, AboutDialogBase = uic.loadUiType(os.path.join(folder_path, "aboutdialog.ui"))


class AboutDialog(AboutDialogBase, AboutDialogUI):
    def __init__(self):
        AboutDialogBase.__init__(self)
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)
