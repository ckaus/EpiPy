# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from epipylib.core.fit import fit

import numpy as np

from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.utils import csvmanager, dateconverter


class SideBarController(BaseController):
    """
    This class represents a controller for notify views which are added
    to *SideBarWidget*. The controller include the logic of attached views.

    :returns: an instance of *SideBarController*
    """

    def __init__(self, parent):
        BaseController.__init__(self, parent, SideBarModel())

        self.current_parameter_group_box = None
        self.select_file = False
        self.select_options = False

    def read_file(self, file_name):
        """
        This functions reads a local CSV file.
        """
        if file_name:
            self.model.input_model.file_name = file_name
            self.model.input_model.file_content = csvmanager.read(file_name)
            self.model.input_model.data_input_length = len(self.model.input_model.file_content.values()[0])
            self.model.input_model.data_range = '0:%s' % self.model.input_model.data_input_length
            self.model.input_model.population = '1'
            self.model.input_model.data_percentage = 100.00
            self.select_file = True
            self.ready_for_fit()
            self.notify(Event.SUCCESS_READ_FILE)

    def get_model(self):
        return self.model

    def set_options_model(self, parameter_group_box, epidemic_model_class, epidemic_model):
        self.model.options_model.epidemic_model = epidemic_model
        self.model.options_model.epidemic_model_class = epidemic_model_class
        self.current_parameter_group_box = parameter_group_box
        self.select_options = True
        self.ready_for_fit()
        self.notify(Event.SUCCESS_SELECT_OPTIONS)

    def set_with_parameters(self, value):
        self.model.options_model.with_parameters = value

    def set_epidemic_model_class(self, epidemic_model_class):
        self.model.options_model.epidemic_model_class = epidemic_model_class

    def get_current_parameter_group_box(self):
        return self.current_parameter_group_box

    def ready_for_fit(self):
        if self.select_file and self.select_options:
            self.notify(Event.ENABLE_FIT_BUTTON)

    def reset_data(self):
        self.model = SideBarModel()
        self.select_file = False
        self.select_options = False
        self.notify(Event.RESET)

    def get_model_parameters(self):
        """
        This function collects data from epidemic model parameter group box.

        :returns: dict of epidemic model parameters
        """
        parameters = []
        parameter_values = []
        group_box = self.current_parameter_group_box
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                parameters.append((str(widget.text()).lower()))
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                parameter_values.append(widget.value())
        return dict(zip(parameters, parameter_values))

    def fit_data(self):

        if not self.is_input_data_valid():
            return

        data_range = self.model.input_model.data_range.split(":")
        from_value = int(data_range[0])
        to_value = int(data_range[1])

        file_content = self.model.input_model.file_content
        population = int(self.model.input_model.population)
        #
        # x- and y-axis
        x_data = np.array(file_content[str(self.model.input_model.date_col_title)], dtype=float)
        y_data = np.array(file_content[str(self.model.input_model.data_col_title)], dtype=float)

        # fitted model range
        x_data_fit = x_data[from_value:to_value]
        y_data_fit = y_data[from_value:to_value]
        # with percentage
        x_data_fit = x_data_fit[:len(x_data_fit) * int(self.model.input_model.data_percentage) / 100]
        y_data_fit = y_data_fit[:len(y_data_fit) * int(self.model.input_model.data_percentage) / 100]

        model = self.model.options_model.epidemic_model
        N0 = self.model.options_model.epidemic_model_class.init_model(N=population, y0=y_data_fit[-1])

        parameters = self.get_model_parameters()

        if self.model.options_model.with_parameters:
            fitted_data, param, _corr_coef = fit(model=model,
                                                 N0=N0,
                                                 xdata=x_data_fit,
                                                 params=(parameters.values()))

        else:
            fitted_data, param, _corr_coef = fit(model=model,
                                                 xdata=x_data_fit,
                                                 ydata=y_data_fit,
                                                 N0=N0,
                                                 iter=10)
            parameters = param

        self.model.options_model.epidemic_model_parameters = parameters
        self.parent.set_plot_data(x_data, y_data,
                                  x_data_fit, fitted_data,
                                  {'r_value**2': _corr_coef})

        self.parent.set_info_text(str(self.model))
        self.update_current_group_box(param)

    def is_input_data_valid(self):
        """
        This function starts validation of input group box.

        :returns: None if valid, *Event* if not valid
        """
        if not self.is_data_range_valid():
            self.notify(Event.INVALID_DATA_RANGE)
            return False

        if not self.is_dates_valid():
            self.notify(Event.CANT_CONVERT_DATES)
            return False

        if not self.is_data_valid():
            self.notify(Event.INVALID_DATA)
            return False
        return True

    def is_data_range_valid(self):
        """
        This function check validity of data input range.

        :returns: True if data range is valid, False if not valid
        """

        _value = self.model.input_model.data_range
        try:
            # check if values contains minus, because
            if '-' in _value:
                raise ValueError

            from_value, to_value = _value.split(":")
            from_value = int(from_value)
            to_value = int(to_value)

            if from_value < 0 or from_value >= to_value or to_value > self.model.input_model.data_input_length:
                raise ValueError
            return True
        except ValueError:
            return False

    def is_dates_valid(self):
        """
        This function checks if date column contains valid dates and convert these dates.

        :returns: True if dates are valid, False if not valid
        """
        date_col_title = self.model.input_model.date_col_title
        dates = self.model.input_model.file_content[str(date_col_title)]
        try:
            np.array(dates, dtype=int)
        except ValueError:  # try to convert date into a valid format
            dates = dateconverter.convert(dates)
            print dates
            if len(dates) == 0:  # can not convert dates
                return False
            # can convert dates, replace dates
            self.model.input_model.file_content[date_col_title] = dates
        return True

    def is_data_valid(self):
        """
        This function checks if data column contains valid data.

        :returns: True if data are valid, False if not valid
        """
        data_col_title = self.model.input_model.data_col_title
        data = self.model.input_model.file_content[str(data_col_title)]
        try:
            np.array(data, dtype=float)
        except ValueError:
            return False
        return True

    def update_current_group_box(self, parameters):
        """
        This function updates the current parameter group box of a showing model.

        :param parameters: model parameters
        :type parameters: array
        """
        group_box = self.current_parameter_group_box
        if group_box.isEnabled():
            return

        spin_boxes_count = 0
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if widget != 0 and type(widget) is QtGui.QDoubleSpinBox:
                widget.setValue(parameters[spin_boxes_count])
                spin_boxes_count += 1
