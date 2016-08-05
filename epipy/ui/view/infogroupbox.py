# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.ui.controller.event import Event
from epipy.ui.model.infomodel import InfoModel

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
icon_path = os.path.join(dir_name(dir_name(dir_name(__file__))), 'resources/pictures/')
InfoGroupBoxUI, InfoGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "infogroupbox.ui"))


class InfoGroupBox(InfoGroupBoxBase, InfoGroupBoxUI):
    """
    This class represents the information group box for printing information.

    :param controller: the used controller
    :type controller: *MainWindowController*

    :returns: an instance of *InfoGroupBox*
    """

    def __init__(self, controller):
        InfoGroupBoxBase.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.controller.attach(self)
        self.model = self.controller.get_model().get_info_model()

    def update(self, event):
        """
        This function updates the view with content.

        :param event: an occurred event
        :type event: an *Event*
        """

        if event == Event.PRINT_INFORMATION:
            self.info_plain_text_edit.appendPlainText(str(self.model))
            self.info_plain_text_edit.appendPlainText('\n')
        elif event == Event.CLEAR_INFORMATION:
            self.info_plain_text_edit.clear()
