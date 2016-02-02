# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
HelpWidgetUI, HelpWidgetBase = uic.loadUiType(os.path.join(folder_path, "helpwidget.ui"))


class HelpWidget(HelpWidgetBase, HelpWidgetUI):
    """
    This class represents the Help widget.

    :returns: an instance of *HelpWidget*
    """
    def __init__(self):
        HelpWidgetBase.__init__(self)
        self.setupUi(self)