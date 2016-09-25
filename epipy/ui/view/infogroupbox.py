# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class InfoGroupBox(QtGui.QGroupBox):
    """This class represents the info group box of *MainWindow*.

    :returns: an instance of *InfoGroupBox*
    """

    def __init__(self):
        super(InfoGroupBox, self).__init__()
        loadUi(cwd + '/infogroupbox.ui', self)

    def set_info(self, text):
        """Output given text on the *InfoGroupBox*.

        :param text: the output text
        :type text: str
        """
        self.info_plain_text_edit.appendPlainText(text)
        self.info_plain_text_edit.appendPlainText('\n')
