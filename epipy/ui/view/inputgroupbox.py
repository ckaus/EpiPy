# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class InputGroupBox(QtGui.QGroupBox):
    """This class represents the input group box of *SideBarWidget*.

    :returns: an instance of *InputGroupBox*
    """

    def __init__(self):
        super(InputGroupBox, self).__init__()
        loadUi(cwd + '/inputgroupbox.ui', self)

        self.population_line_edit.setValidator(QtGui.QDoubleValidator(self))
        self.population_line_edit.setMaxLength(10)  # 10 Billion - 1
        regex_validator = QtGui.QRegExpValidator(self)
        regex_validator.setRegExp(QtCore.QRegExp('[0-9]{1,4}:[0-9]{1,4}'))
        self.data_range_line_edit.setValidator(regex_validator)
        self.data_percentage_spin_box.clear()

    def clear(self):
        """Clears the *InputGroupBox*."""
        self.input_file_text_field.clear()
        self.date_cb.clear()
        self.data_cb.clear()
        self.population_line_edit.clear()
        self.data_range_line_edit.clear()
        self.data_percentage_spin_box.clear()

    def get_data_percentage(self):
        """Returns the percentage of data range.

        :returns: the percentage of data range
        :rtype: float
        """
        return self.data_percentage_spin_box.value()

    def get_data_range(self):
        """Returns the data range of selected CSV file.
        Data range has the format from:to.

        :returns: data range of selected CSV file
        :rtype: str
        """
        return str(self.data_range_line_edit.text())

    def get_population(self):
        """Returns the population.

        :returns: the population of input data
        :rtype: int
        """
        return int(self.population_line_edit.text())

    def get_selected_data_cb_text(self):
        """Returns the selected data column

        :returns: selected data column
        :rtype: str
        """
        return str(self.data_cb.currentText())

    def get_selected_date_cb_text(self):
        """Returns selected date column

        :returns: selected date column
        :rtype: str
        """
        return str(self.date_cb.currentText())

    def open_file(self):
        """Shows an open file dialog.

        :returns: the file name of the selected CSV file.
        :rtype: str
        """
        filter = 'CSV file (*.csv);;All Files (*.*)'
        return str(QtGui.QFileDialog.getOpenFileName(self, 'Open CSV file',
                                                     filter=filter))

    def show_notification(self, text):
        """Shows a notification warning window *QMessageBox*.

        :param text: the showing text
        :type text: str
        """
        QtGui.QMessageBox.warning(self, 'Warning', text,
                                  QtGui.QMessageBox.Ok)

    def update(self, file_name, date_cb_title, data_cb_title, data_range,
               data_percentage, population):
        """Updates the *InputGroupBox* view.

        :param file_name: the file name
        :type file_name: str
        :param date_cb_title: the CSV file header
        :type date_cb_title: list
        :param data_cb_title: the CSV file header
        :type data_cb_title: list
        :param data_range: the file data range
        :type data_range: str
        :param data_percentage: the file data range percentage
        :type data_percentage: float
        :param population: the population
        :type population: int
        """
        self.input_file_text_field.setText(file_name)
        self.date_cb.clear()
        self.date_cb.addItems(date_cb_title)
        self.data_cb.clear()
        self.data_cb.addItems(data_cb_title)
        self.data_range_line_edit.setText(data_range)
        self.data_percentage_spin_box.setValue(data_percentage)
        self.population_line_edit.setText(str(population))
