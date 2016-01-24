# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtGui
from epipy.ui.controller.event import Event

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
InputGroupBoxUI, InputGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "inputgroupbox.ui"))


class InputGroupBox(InputGroupBoxBase, InputGroupBoxUI):
    def __init__(self, controller):
        InputGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)

        self.open_file_btn.clicked.connect(self.open_file)

    def open_file(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open CSV file", filter="CSV file (*.csv);;All Files (*.*)")
        if file_name:
            self.controller.set_input_file(file_name)

    def update(self, event):
        if event == Event.READ_FILE:
            pass
            # self.input_file_text_field.setText(self.controller.get_input_file())
