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
    :type controller: *SideBarViewController*

    :returns: an instance of *InputGroupBox*
    """

    def __init__(self, controller):
        InputGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.model = self.controller.get_model().get_input_model()

        self.open_file_btn.clicked.connect(self.open_file)
        self.date_cb.currentIndexChanged['QString'].connect(self.model.set_date_col_title)
        self.data_cb.currentIndexChanged['QString'].connect(self.model.set_data_col_title)
        self.population_line_edit.setValidator(QtGui.QIntValidator(self))
        self.population_line_edit.textChanged.connect(self.population_text_changed)
        self.population_slider.valueChanged[int].connect(self.population_slider_changed)

    def open_file(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self,
                                                      "Open CSV file",
                                                      filter="CSV file (*.csv);;All Files (*.*)")
        self.controller.read_file(file_name)

    def population_slider_changed(self, value):
        self.population_line_edit.setText(str(value))

    def population_text_changed(self, value):
        self.population_slider.setValue(int(value))

    def switch_availability_components(self, is_available):
        self.date_cb.setEnabled(is_available)
        self.data_cb.setEnabled(is_available)
        self.population_line_edit.setEnabled(is_available)
        self.data_range_line_edit.setEnabled(is_available)
        self.population_slider.setEnabled(is_available)
        self.data_percentage_spin_box.setEnabled(is_available)

    def update(self, event):
        """
        This function updates the view with content and change availability of
        GUI components.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.SUCCESS_READ_FILE:
            self.switch_availability_components(True)
            self.input_file_text_field.setText(self.model.file_name)
            self.date_cb.clear()
            self.date_cb.addItems(self.model.file_content.keys())
            self.data_cb.clear()
            self.data_cb.addItems(self.model.file_content.keys())
            self.data_range_line_edit.setText(self.model.data_range)
            self.population_line_edit.setText(self.model.population)
            self.data_percentage_spin_box.setValue(self.model.data_percentage)
        elif event == Event.RESET:
            self.input_file_text_field.clear()
            self.date_cb.clear()
            self.data_cb.clear()
            self.data_range_line_edit.clear()
            self.data_percentage_spin_box.setValue(100.00)
            self.switch_availability_components(False)
        elif event == Event.CANT_CONVERT_DATES:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Please make sure you have selected a 'Date' column.\n"
                                      "Dates should have the following format: YYYY-MM-DD.",
                                      QtGui.QMessageBox.Ok)

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
            self.population_text_changed('1')
        elif event == Event.INVALID_DATA_PERCENTAGE:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Invalid data percentage. Please enter a number between 1 and 100.",
                                      QtGui.QMessageBox.Ok)
        elif event == Event.INVALID_DATA:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      "Data should be numbers like 1 or 1.0.",
                                      QtGui.QMessageBox.Ok)
