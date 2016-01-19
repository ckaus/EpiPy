# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtGui

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
InfoGroupBoxUI, InfoGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "infogroupbox.ui"))


class InfoGroupBox(InfoGroupBoxBase, InfoGroupBoxUI):
    def __init__(self):
        InfoGroupBoxBase.__init__(self)
        self.setupUi(self)

        self.clear_btn.clicked.connect(self.clear_fitting_info)

    def clear_fitting_info(self):
        if self.info_plain_text_edit.toPlainText():
            reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to clear the fitting information?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.info_plain_text_edit.clear()
