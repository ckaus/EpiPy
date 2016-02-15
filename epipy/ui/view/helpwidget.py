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
        web_view = QtWebKit.QWebView()
        web_view.load(QtCore.QUrl(os.path.join(folder_path + 'resources', "manual.htm")))
        layout.addWidget(web_view)
        self.setLayout(layout)
