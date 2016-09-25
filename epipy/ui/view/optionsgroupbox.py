# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, uic
from PyQt4.uic import loadUi
from epipy.ui.view import cwd


class OptionsGroupBox(QtGui.QGroupBox):
    """This class represents the options group box of the *SideBarWidget*.

    :returns: an instance of *OptionsGroupBox*
    """

    def __init__(self):
        super(OptionsGroupBox, self).__init__()
        loadUi(cwd + '/optionsgroupbox.ui', self)

        self.model_combo_box.setItemData(0,
                                         QtCore.QVariant(0),
                                         QtCore.Qt.UserRole - 1)
        self.parameters_check_box.stateChanged.connect(self.hide_show_params)
        self.advanced_dialog = None

    def add_parameter_group_box(self, parameter_group_box):
        """Adds the model parameter options.

        :param parameter_group_box: the model parameter options
        :type parameter_group_box: *QGroupBox*
        """
        if not parameter_group_box:
            return  # Do nothing
        self.remove_parameter_group_box()
        self.layout().addWidget(parameter_group_box, 3, 0, 1, 3)
        self.hide_show_params(self.parameters_check_box.isChecked())

    def clear(self):
        """Clears the *OptionsGroupBox*."""
        self.model_combo_box.setCurrentIndex(0)
        self.remove_parameter_group_box()

    def get_model_parameters(self):
        """Returns the model parameter options (label, value) based on showing
        model paramter group box on *OptionsGroupBox*.

        :returns: model parameter options
        :rtype: dict
        """
        parameters = []
        parameter_values = []
        group_box = self.layout().itemAt(3)
        if not group_box:
            return {}
        layout = group_box.widget().layout()
        for i in range(0, layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QtGui.QLabel):
                parameters.append((str(widget.text()).lower()))
            elif isinstance(widget, QtGui.QDoubleSpinBox):
                parameter_values.append(widget.value())
        return dict(zip(parameters, parameter_values))

    def hide_show_params(self, state):
        """Hides or shows the model parameter options"""
        if self.layout().itemAt(3):
            self.layout().itemAt(3).widget().setEnabled(state)

    def remove_parameter_group_box(self):
        """Removes the model parameter options"""
        if self.layout().itemAt(3):
            self.layout().itemAt(3).widget().deleteLater()

    def show_notification(self, text):
        """Shows a notification warning window *QMessageBox*.

        :param text: the showing text
        :type text: str
        """
        QtGui.QMessageBox.warning(self, 'Warning', text,
                                  QtGui.QMessageBox.Ok)
