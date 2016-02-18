# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore, QtWebKit

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(dir_name(__file__))), '')


class HelpWidget(QtGui.QWidget):
    """
    This class represents the Help widget.

    :returns: an instance of *HelpWidget*
    """

    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        menu_cb = QtGui.QComboBox()
        menu_cb.addItem(QtCore.QString('GUI Components'))
        menu_cb.addItem(QtCore.QString('Example: Fit Data'))
        menu_cb.currentIndexChanged['int'].connect(self.change_manual_page)
        layout.addWidget(menu_cb)
        self.web_view = QtWebKit.QWebView()
        self.change_manual_page(0)
        layout.addWidget(self.web_view)
        self.setLayout(layout)

    def change_manual_page(self, value):
        if value == 0:
            self.web_view.load(QtCore.QUrl(os.path.join(folder_path + 'resources/manual', "manual.htm")))
        elif value == 1:
            self.web_view.load(QtCore.QUrl(os.path.join(folder_path + 'resources/manual', "example.htm")))
