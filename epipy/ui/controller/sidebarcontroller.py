# -*- coding: utf-8 -*-

import numpy as np
import random
from PyQt4 import QtGui

from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.utils import csvmanager, dateconverter


class SideBarController(BaseController):
    """
    This class represents a controller for notify views which are added
    to *SideBarWidget*. The controller include the logic of attached views.

    :param controller_service: a controller service
    :type controller_service: an instance of *ControllerService*

    :returns: an instance of *SideBarController*
    """

    def __init__(self, controller_service):
        BaseController.__init__(self)
        self.model = SideBarModel()

        self.controller_service = controller_service
        self.current_model_group_box = None
        self.current_date_col = None
        self.current_data_col = None
        self.data_input_length = 0
        self.current_data_range = None
        self.with_param = None
        self.data_percentage = 100
        self.options_group_box_is_enable = False

    def clear_input(self):
        """
        This function clears all input components on side bar view.
        """

        self.model.input_model.file_name = None
        self.model.input_model.file_content = None
        self.data_percentage = 100.00
        self.notify(Event.CLEAR_INPUT)

    def fit_data(self):
        """
        This function collects content from side bar view and start fitting based on collected content.
        """

        is_valid = self.validate_input_data()
        if not is_valid:
            return
        self.model.input_model.data_range = self.current_data_range

        data_range = self.model.input_model.data_range.split(":")
        from_value = int(data_range[0])
        to_value = int(data_range[1])

        file_content = self.model.input_model.file_content
        model_class = self.model.options_model.epidemic_model_class
        population = int(self.model.input_model.population)

        # x- and y-axis
        x_data = np.array(file_content[self.current_date_col], dtype=float)
        y_data = np.array(file_content[self.current_data_col], dtype=float)

        # fitted model range
        x_data_fit = x_data[from_value:to_value]
        y_data_fit = y_data[from_value:to_value]
        # with percentage
        x_data_fit = x_data_fit[:len(x_data_fit) * int(self.data_percentage) / 100]
        y_data_fit = y_data_fit[:len(y_data_fit) * int(self.data_percentage) / 100]

        # forecast model range = time + 29(t)
        x_data_forecast = [i for i in range(int(x_data[from_value]), int(x_data[to_value - 1]) + 30)]
        y_data_forecast = y_data[from_value]

        param = self.get_model_parameters_combo_box()
        if self.with_param:
            fitted_data = model_class.fit(x_data_fit, y_data_fit, N=population, **param)
        else:
            # fitted model - using optimize(), we don't know the parameters for all infected!
            fitted_data = model_class.fit(x_data_fit, y_data_fit, N=population)

        # forecast graph is based on I0 and optimized parameters
        forecast_param = dict(zip(param.keys(), fitted_data[1]))
        forecast = model_class.fit(x_data_forecast, [y_data_forecast], N=population, with_line_regress=False,
                                   **forecast_param)

        self.model.plot_model.set_data(x_data, y_data, x_data_fit, fitted_data[0], x_data_forecast, forecast[0],
                                       {'slope': fitted_data[2][0], 'intercept': fitted_data[2][1],
                                        'r_value**2': fitted_data[2][2], 'p_value': fitted_data[2][3],
                                        'std_err': fitted_data[2][4]})

        self.update_current_group_box(fitted_data[1])
        self.controller_service.redirect(Event.PLOT)

    def is_data_range_valid(self):
        """
        This function check validity of data input range.

        :returns: True if data range is valid, False if not valid
        """

        _value = self.current_data_range
        try:
            from_value, to_value = _value.split(":")
            # check if values contains minus, because
            # a cast of a value -1 to an integer returns 1
            if from_value.contains('-') or to_value.contains('-'):
                raise ValueError

            from_value = int(from_value)
            to_value = int(to_value)

            if from_value < 0 or from_value >= to_value or to_value > self.data_input_length:
                raise ValueError
            return True
        except ValueError:
            return False

    def is_data_valid(self):
        """
        This function checks if data column contains valid data.

        :returns: True if data are valid, False if not valid
        """
        data = self.model.input_model.file_content[self.current_data_col]
        try:
            np.array(data, dtype=float)
        except ValueError:
            return False
        return True

    def is_dates_valid(self):
        """
        This function checks if date column contains valid dates and convert these dates.

        :returns: True if dates are valid, False if not valid
        """
        dates = self.model.input_model.file_content[self.current_date_col]
        try:
            np.array(dates, dtype=int)
        except ValueError:  # try to convert date into a valid format
            dates = dateconverter.convert(dates)
            if len(dates) == 0:  # can not convert dates
                return False
            # can convert dates, replace dates
            self.model.input_model.file_content[self.current_date_col] = dates
        return True

    def get_data_range(self):
        """
        :returns: data range of *InputModel*
        """
        return self.model.input_model.data_range

    def get_epidemic_model(self):
        """
        :returns: the chosen epidemic model
        """
        return self.model.options_model.epidemic_model

    def get_current_model_parameter_group_box(self):
        """
        :returns: the current epidemic model parameter group box
        """
        return self.current_model_group_box

    def get_model_parameters(self):
        """
        :returns: the epidemic model parameters
        """
        return self.model.options_model.epidemic_model_parameters

    def get_model_parameters_combo_box(self):
        """
        This function collects data from epidemic model parameter group box.

        :returns: dict of epidemic model parameters
        """
        parameters = []
        parameter_values = []
        group_box = self.current_model_group_box
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                parameters.append((str(widget.text()).lower()))
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                parameter_values.append(widget.value())
        return dict(zip(parameters, parameter_values))

    def get_model(self):
        """
        :returns: the side bar view model
        """
        return self.model

    def get_plot_data(self):
        """
        :returns: the plotable data
        """
        return self.model.plot_model.get_data()

    def get_population(self):
        """
        :returns: the population
        """
        return self.model.input_model.population

    def get_file_header(self):
        """
        :returns: the input csv file header
        """
        return self.model.input_model.file_content.keys()

    def reset_data(self):
        """
        This function clear the side bar components and disable the epidemic option group box.
        """
        self.clear_input()
        self.notify(Event.DISABLE_OPTIONS_GROUP_BOX)

    def set_date_col(self, value):
        """
        This function sets the selected date column.

        :param value: a selected date column
        :type value: a *QString*
        """
        self.current_date_col = str(value)

    def set_data_col(self, value):
        """
        This function sets the selected data column.

        :param value: a selected data column
        :type value: a *QString*
        """
        self.current_data_col = str(value)

    def set_data_range(self, value):
        """
        This function stores the current input data range.

        :param value: input data range
        :type value: str has format from:to
        """
        self.current_data_range = value

    def set_model(self, model):
        """
        This function sets a given epidemic model to the *OptionsModel*.

        :param model: a epidemic model
        :type model: a *QString*
        """
        self.model.options_model.epidemic_model = model
        self.notify(Event.SELECT_NEW_MODEL)
        self.notify(Event.DISABLE_FIT_BUTTON)

    def set_model_group_box(self, model_group_box, model_class):
        """
        This function sets a given model group box and model class.

        :param model_group_box: a model group box
        :type model_group_box: a *QGroupBox*
        :param model_class: a model class
        :type model_class: a *BaseModel*
        """
        self.current_model_group_box = model_group_box
        self.model.options_model.epidemic_model_class = model_class
        self.notify(Event.SELECT_NEW_MODEL_TYPE)
        self.notify(Event.ENABLE_FIT_BUTTON)

    def set_population(self, value):
        """
        This function set a given value as population of a data set to the *InputModel*.

        :param value: the population of a data set
        :type value: a *QString*
        """
        try:
            if not value:
                self.model.input_model.population = '1'
                raise ValueError
            else:
                self.model.input_model.population = value
                self.notify(Event.UPDATE_POPULATION_SLIDER)
                self.notify(Event.ENABLE_OPTIONS_GROUP_BOX)
        except ValueError:
            self.notify(Event.INVALID_POPULATION)
            self.notify(Event.UPDATE_POPULATION_FIELD)

    def set_population_from_slider(self, value):
        """
        This function set a given value from the slider as population of a data set to the *InputModel*.

        :param value: the population of a data set
        :type value: an int
        """
        self.model.input_model.population = str(value)
        self.notify(Event.UPDATE_POPULATION_FIELD)

    def set_input_file(self, file_name):
        """
        This function sets a given file name to the *InputModel*.

        :param file_name: a file name
        :type file_name: a str
        """
        file_content = csvmanager.read(file_name)
        self.model.input_model.file_name = file_name
        self.data_input_length = len(file_content.values()[0])
        self.model.input_model.data_range = '0:%s' % self.data_input_length
        self.model.input_model.file_content = file_content
        self.model.input_model.population = '1'
        self.notify(Event.SET_FILE_CONTENT)
        self.notify(Event.ENABLE_COL_DATE_FORMAT)

    def set_data_percentage(self, percentage):
        """
        This function sets the percentage of data used in the fitting process.

        :param percentage: percentage of the data
        :type percentage: float from (0, 100]
        """
        self.data_percentage = percentage

    def update_current_group_box(self, parameters):
        """
        This function updates the current parameter group box of a showing model.

        :param parameters: model parameters
        :type parameters: array
        """
        group_box = self.get_current_model_parameter_group_box()
        if group_box.isEnabled():
            return

        self.model.options_model.epidemic_model_parameters = parameters
        spin_boxes_count = 0
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if widget != 0 and type(widget) is QtGui.QDoubleSpinBox:
                widget.setValue(parameters[spin_boxes_count])
                spin_boxes_count += 1

    def validate_input_data(self):
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

    def with_parameters(self, value):
        """
        This function notify the *OptionsGroupBox* view to enable/disable
        showing parameter group box of a model.

        :param value: status of the parameter checkbox
        :type value: bool
        """
        self.with_param = value
        self.notify(Event.SELECT_WITH_PARAMETERS)
