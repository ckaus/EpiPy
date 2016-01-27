# -*- coding: utf-8 -*-

import numpy as np
from pyqtgraph import QtGui, QtCore

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

        data_range = self.model.input_model.data_range.split(":")
        from_value = int(data_range[0])
        to_value = int(data_range[1])

        param = self.get_model_parameters_combo_box()
        file_content = self.model.input_model.file_content
        x_data = np.array(file_content[self.current_date_col][from_value:to_value], dtype=float)
        y_data = np.array(file_content[self.current_data_col][from_value:to_value], dtype=float)
        model_class = self.model.options_model.epidemic_model_class
        fitted_data = None
        if not param:
            # use optimize function for best fitted model
            fitted_data = model_class.fit(x_data, y_data, N=self.model.input_model.population)
        else:
            # use user input model parameters for fitting the model
            fitted_data = model_class.fit(x_data, y_data, N=self.model.input_model.population, **param)
        if not fitted_data:  # Runtime error during fitting
            self.notify(Event.SHOW_RUNTIME_ERROR)
            return
        # fitted model coordinates
        self.model.plot_model.x_data = x_data
        self.model.plot_model.y_data = y_data
        # model parameters
        self.model.options_model.epidemic_model_parameters = fitted_data[1]
        # fitted model
        self.model.plot_model.y_fitted_data = fitted_data[0]
        # some regression values of fitted model
        self.model.plot_model.regression_values = {'slope': fitted_data[2], 'intercept': fitted_data[3],
                                                   'r_value**2': fitted_data[4], 'p_value': fitted_data[5],
                                                   'std_err': fitted_data[6]}
        self.update_current_group_boxes(fitted_data[1])
        self.controller_service.redirect(Event.PLOT)

    def format_date(self):
        """
        This function check if the  time fields of an input file needs to convert.
        """
        dates = self.model.input_model.file_content[self.current_date_col]
        dates = dateconverter.convert(dates)
        if len(dates) == 0:
            self.notify(Event.SHOW_CANT_CONVERT_DATES)
        else:
            self.model.input_model.file_content[self.current_date_col] = dates

    def get_data_range(self):
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
        if not group_box.isEnabled():
            # optimize is choosen
            return None
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
        self.notify(Event.DISABLE_OPTIONS)

    def set_optimize(self, value):
        """
        This function set the optimize flag of the optimize check box and enable/disable the epidemic model parameters.

        :param value: the flag
        :type value: a bool
        """
        if self.current_model_group_box:
            if value:
                self.notify(Event.DISABLE_PARAMETERS)
            else:
                self.notify(Event.ENABLE_PARAMETERS)

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
        if not value:
            return
        try:
            _value = value
            from_value, to_value = _value.split(":")
            int(from_value)
            int(to_value)
            self.model.input_model.data_range = value
        except ValueError:
            self.notify(Event.INVALID_DATA_RANGE)

    def set_model(self, model):
        """
        This function set a given epidemic model to the *OptionsModel*.

        :param model: a epidemic model
        :type model: a QString
        """
        self.model.options_model.epidemic_model = model
        self.notify(Event.ENABLE_ADVANCED_BUTTON)
        if self.get_current_model_parameter_group_box():
            self.notify(Event.DISABLE_PARAMETERS)
        self.notify(Event.ENABLE_OPTIMIZE)

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
        self.notify(Event.SHOW_MODEL_PARAMETER_GROUP_BOX)
        self.notify(Event.ENABLE_FIT_BUTTON)

    def set_population(self, value):
        """
        This function set a given value as population of a data set to the *InputModel*.

        :param value: the population of a data set
        :type value: a QString
        """
        if value:
            self.model.input_model.population = int(value)

    def set_input_file(self, file_name):
        """
        This function set a given file name to the *InputModel*.

        :param file_name: a file name
        :type file_name: a str
        """
        self.model.input_model.file_name = file_name
        file_content = csvmanager.read(file_name)
        self.model.input_model.data_range = "0:%s" % len(file_content.values()[0])
        self.model.input_model.file_content = file_content
        self.notify(Event.SET_FILE_CONTENT)
        self.notify(Event.ENABLE_COL_DATE_FORMAT)
        self.notify(Event.ENABLE_OPTIONS)

    def update_current_group_boxes(self, parameters):
        """
        This function updates the current model parameter group boxes with given parameters.

        :param parameters: the parameters
        :type: a list of str
        """
        group_box = self.get_current_model_parameter_group_box()
        if group_box.isEnabled():
            return
        spin_boxes_count = 0
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                widget.setValue(parameters[spin_boxes_count])
                spin_boxes_count += 1
