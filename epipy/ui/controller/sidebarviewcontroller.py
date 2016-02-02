# -*- coding: utf-8 -*-

import numpy as np
import random

from pyqtgraph import QtGui

from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.utils import csvmanager, dateconverter


class SideBarController(BaseController):
    """
    This class represents a controller for notify and operating on views.

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

    def clear_input(self):
        """
        This function clear all input components on side bar view.
        """
        self.model.input_model.file_name = None
        self.model.input_model.file_content = None
        self.model.input_model.population = None
        self.notify(Event.CLEAR_INPUT)

    def fit_data(self):
        """
        This function collect content from side bar view and start fitting based on collected content.
        """
        if not self.model.input_model.population:
            self.notify(Event.NO_POPULATION)
            return
        # check validity of data range
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
            else:
                self.model.input_model.data_range = self.current_data_range
        except ValueError:
            self.notify(Event.INVALID_DATA_RANGE)
            return

        data_range = self.model.input_model.data_range.split(":")
        from_value = int(data_range[0])
        to_value = int(data_range[1])

        file_content = self.model.input_model.file_content

        if not self.is_dates_valid():
            self.notify(Event.SHOW_CANT_CONVERT_DATES)
            return

        model_class = self.model.options_model.epidemic_model_class
        population = self.model.input_model.population

        # x- and y-axis
        x_data = np.array(file_content[self.current_date_col], dtype=float)
        y_data = np.array(file_content[self.current_data_col], dtype=float)

        # fitted model range
        x_data_fit = x_data[from_value:to_value]
        y_data_fit = y_data[from_value:to_value]

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

        self.model.plot_model.x_data = x_data[from_value:to_value]
        self.model.plot_model.y_data = y_data[from_value:to_value]
        self.model.plot_model.x_fitted = x_data_fit
        self.model.plot_model.y_fitted = fitted_data[0]
        self.model.plot_model.x_forecast = x_data_forecast
        self.model.plot_model.y_forecast = forecast[0]
        self.update_current_group_box(fitted_data[1])
        self.model.options_model.epidemic_model_parameters = fitted_data[1]
        # some regression values of fitted model
        self.model.plot_model.regression_values = {'slope': fitted_data[2], 'intercept': fitted_data[3],
                                                   'r_value**2': fitted_data[4], 'p_value': fitted_data[5],
                                                   'std_err': fitted_data[6]}
        self.controller_service.redirect(Event.PLOT)

    def is_dates_valid(self):
        # check if date col contains valid dates
        dates = self.model.input_model.file_content[self.current_date_col]
        try:
            # select a random date and check if date has valid format
            int(dates[random.randint(0, len(dates) - 1)])
        except ValueError:  # try to convert date into a valid format
            dates = dateconverter.convert(dates)
            if len(dates) == 0:  # can not convert dates
                return False
            else:  # can convert dates, set converted dates
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
        This function collect data from epidemic model parameter group box.

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
        self.notify(Event.CHANGE_AVAILABILITY_OPTIONS)

    def set_date_col(self, value):
        """
        This function set the selected date column.
        :param value: a selected date column
        :type value: a QString
        """
        self.current_date_col = str(value)

    def set_data_col(self, value):
        """
        This function set the selected data column.

        :param value: a selected data column
        :type value: a QString
        """
        self.current_data_col = str(value)

    def set_data_range(self, value):
        """
        This function store the current input data range.

        :param value: input data range
        :type value: str has format from:to
        """
        self.current_data_range = value

    def set_model(self, model):
        """
        This function set a given epidemic model to the *OptionsModel*.

        :param model: a epidemic model
        :type model: a QString
        """
        self.model.options_model.epidemic_model = model
        self.notify(Event.SELECT_NEW_MODEL)
        self.notify(Event.ENABLE_FIT_BUTTON)

    def set_model_group_box(self, model_group_box, model_class):
        """
        This function set a given model group box and model class.

        :param model_group_box: a model group box
        :type model_group_box: a QGroupBox
        :param model_class: a model class
        :type model_class: a *BaseModel*
        """
        self.current_model_group_box = model_group_box
        self.model.options_model.epidemic_model_class = model_class
        self.notify(Event.SELECT_NEW_MODEL_TYPE)

    def set_population(self, value):
        """
        This function set a given value as population of a data set to the *InputModel*.

        :param value: the population of a data set
        :type value: a QString
        """
        try:
            if value.contains('-'):
                raise ValueError
            if not value.isEmpty():
                self.model.input_model.population = int(value)
        except ValueError:
            self.notify(Event.INVALID_POPULATION)

    def set_input_file(self, file_name):
        """
        This function set a given file name to the *InputModel*.

        :param file_name: a file name
        :type file_name: a str
        """
        self.model.input_model.file_name = file_name
        file_content = csvmanager.read(file_name)
        self.data_input_length = len(file_content.values()[0])
        self.model.input_model.data_range = "0:%s" % self.data_input_length
        self.model.input_model.file_content = file_content
        self.notify(Event.SET_FILE_CONTENT)
        self.notify(Event.ENABLE_COL_DATE_FORMAT)
        self.notify(Event.CHANGE_AVAILABILITY_OPTIONS)

    def update_current_group_box(self, parameters):
        group_box = self.get_current_model_parameter_group_box()
        if group_box.isEnabled():
            return
        spin_boxes_count = 0
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if widget != 0 and type(widget) is QtGui.QDoubleSpinBox:
                widget.setValue(parameters[spin_boxes_count])
                spin_boxes_count += 1

    def with_parameters(self, value):
        self.with_param = value
        self.notify(Event.SELECT_WITH_PARAMETERS)
