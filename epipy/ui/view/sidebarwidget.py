# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd, Notification
from epipy.ui.view.inputgroupbox import InputGroupBox
from epipy.ui.view.optionsgroupbox import OptionsGroupBox


class SideBarWidget(QtGui.QWidget):
    def __init__(self):
        super(SideBarWidget, self).__init__()
        loadUi(cwd + '/sidebarwidget.ui', self)

        # Top
        self.input_group_box = InputGroupBox()
        self.layout().addWidget(self.input_group_box)
        # Center
        self.options_group_box = OptionsGroupBox()
        self.layout().addWidget(self.options_group_box)
        self.spacer = QtGui.QSpacerItem(0, 0, 0, QtGui.QSizePolicy.Expanding)
        self.layout().addItem(self.spacer)
        # Bottom
        self.bottom_widget = QtGui.QWidget(self)
        self.bottom_layout = QtGui.QHBoxLayout(self.bottom_widget)
        self.fit_btn = QtGui.QPushButton('Fit')
        self.bottom_layout.addWidget(self.fit_btn)
        self.reset_btn = QtGui.QPushButton('Reset')
        self.bottom_layout.addWidget(self.reset_btn)
        self.layout().addWidget(self.bottom_widget)

    def clear(self):
        """Clears widgets on *SideBarWidget*."""
        reply = QtGui.QMessageBox.question(self,
                                           'Message',
                                           Notification.RESET_DATA,
                                           QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.input_group_box.clear()
            self.options_group_box.clear()
