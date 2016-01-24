# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtGui, QtCore
from epipy.ui.controller.event import Event

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
icon_path = os.path.join(dir_name(dir_name(dir_name(__file__))), 'resources/pictures/')
InfoGroupBoxUI, InfoGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "infogroupbox.ui"))


class InfoGroupBox(InfoGroupBoxBase, InfoGroupBoxUI):
    def __init__(self, controller):
        InfoGroupBoxBase.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.controller.attach(self)

        self.spacer = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding)
        self.top_layout.addItem(self.spacer)

        self.clear_btn = QtGui.QPushButton()
        self.clear_icon = QtGui.QIcon(icon_path + 'clear.png')
        self.clear_btn.clicked.connect(self.info_plain_text_edit.clear)
        self.clear_btn.setIcon(self.clear_icon)
        self.top_layout.addWidget(self.clear_btn)

    def update(self, event):
        if event == Event.LOG:
            model = self.controller.get_model()
            self.info_plain_text_edit.appendPlainText(str(model))
