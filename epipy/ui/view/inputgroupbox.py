# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtGui

from epipy.ui.controller.event import Event

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
InputGroupBoxUI, InputGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "inputgroupbox.ui"))


class InputGroupBox(InputGroupBoxBase, InputGroupBoxUI):
    """
    This class represents the input group box for files.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *InputGroupBox*
    """

    def __init__(self, controller):
        InputGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.open_file_btn.clicked.connect(self.open_file)
        self.date_cb.currentIndexChanged['QString'].connect(self.controller.set_date_col)
        self.data_cb.currentIndexChanged['QString'].connect(self.controller.set_data_col)
        self.data_range_line_edit.textChanged.connect(self.controller.set_data_range)
        self.population_line_edit.setValidator(QtGui.QIntValidator(self))
        self.population_line_edit.textChanged.connect(self.controller.set_population)

    def open_file(self):
        """
        This functions reads a local CSV file.
        """
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open CSV file", filter="CSV file (*.csv);;All Files (*.*)")
        if file_name:
            # clear input boxes just in case something was configure before
            if self.input_file_text_field.text():
                self.controller.clear_input()

            self.input_file_text_field.clear()
            self.input_file_text_field.setText(file_name)
            self.controller.set_input_file(file_name)

    def update(self, event):
        """
        This function updates the view with content and change availability of
        GUI components.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.SET_FILE_CONTENT:
            self.date_cb.addItems(self.controller.get_file_header())
            self.data_cb.addItems(self.controller.get_file_header())
            self.data_range_line_edit.setText(self.controller.get_data_range())
        elif event == Event.ENABLE_COL_DATE_FORMAT:
            self.date_cb.setEnabled(True)
            self.data_cb.setEnabled(True)
            self.population_line_edit.setEnabled(True)
            self.data_range_line_edit.setEnabled(True)

        elif event == Event.SHOW_CANT_CONVERT_DATES:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Please make sure you have selected a 'Date' column.\n"
                                      "Dates should have the following format: YYYY-MM-DD\n",
                                      QtGui.QMessageBox.Ok)
        elif event == Event.CLEAR_INPUT:
            self.input_file_text_field.clear()
            self.date_cb.clear()
            self.data_cb.clear()
            self.data_range_line_edit.clear()
            self.population_line_edit.clear()
        elif event == Event.NO_POPULATION:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Please define a population.",
                                      QtGui.QMessageBox.Ok)
        elif event == Event.INVALID_DATA_RANGE:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Invalid data range and/or data range has not format: from:to",
                                      QtGui.QMessageBox.Ok)
        elif event == Event.INVALID_POPULATION:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Invalid population. Value must be greater than 0.",
                                      QtGui.QMessageBox.Ok)
