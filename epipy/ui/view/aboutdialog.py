# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd
from epipy import __version__, __description__, __author__


class AboutDialog(QtGui.QDialog):
    """This class represents the about dialog.

    :returns: an instance of *AboutDialog*
    """

    def __init__(self):
        super(AboutDialog, self).__init__()
        loadUi(cwd + '/aboutdialog.ui', self)

        text = 'EpiPy - ' + __version__ + '\n' + \
               'Description: ' + __description__ + '\n' + \
               'Authors: ' + __author__
        self.text_label.setText(text)
        self.close_btn.clicked.connect(self.close)
