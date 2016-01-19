# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtGui

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
icon_path = os.path.join(dir_name(dir_name(dir_name(__file__))), 'resources/pictures/')
InfoGroupBoxUI, InfoGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "infogroupbox.ui"))


class InfoGroupBox(InfoGroupBoxBase, InfoGroupBoxUI):
    def __init__(self):
        InfoGroupBoxBase.__init__(self)
        self.setupUi(self)
        save_btn = QtGui.QPushButton(self)
        save_icon = QtGui.QIcon(icon_path + 'save.png')
        save_btn.setIcon(save_icon)
        self.clear_btn = QtGui.QPushButton(self)
        clear_icon = QtGui.QIcon(icon_path + 'clear.png')
        self.clear_btn.setIcon(clear_icon)
        spacer = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding)
        self.top_layout.addWidget(save_btn)
        self.top_layout.addItem(spacer)
        self.file_name = QtGui.QLabel('No File Name')
        self.top_layout.addWidget(self.file_name)
        self.top_layout.addItem(spacer)
        self.top_layout.addWidget(self.clear_btn)
