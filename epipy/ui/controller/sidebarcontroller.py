# -*- coding: utf-8 -*-

import numpy as np

from pyqtgraph import QtGui

from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.utils import csvmanager, dateconverter


class SideBarController(BaseController):
    def __init__(self, controller_service):
        BaseController.__init__(self)
        self.model = SideBarModel()

        self.controller_service = controller_service
        self.current_model_group_box = None
        self.current_date_col = None
        self.current_data_col = None

    def set_model(self, model):
        self.model.options_model.epidemic_model = model
        self.notify(Event.ENABLE_ADVANCED_BUTTON)
        if self.get_current_model_group_box():
            self.notify(Event.DISABLE_PARAMETERS)
        self.notify(Event.ENABLE_OPTIMIZE)

    def get_epidemic_model(self):
        return self.model.options_model.epidemic_model

    def get_current_model_group_box(self):
        return self.current_model_group_box

    def set_model_group_box(self, model_group_box, model_class):
        self.current_model_group_box = model_group_box
        self.model.options_model.epidemic_model_class = model_class
        self.notify(Event.SHOW_MODEL_PARAMETER_GROUP_BOX)
        self.notify(Event.ENABLE_FIT_BUTTON)

    def set_population(self, value):
        if value:
            self.model.input_model.population = int(value)

    def get_model_parameter_group_box(self):
        return self.current_model_group_box

    def get_model_parameters(self):
        return self.model.options_model.epidemic_model_parameters

    def get_model_parameters_combo_box(self):
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
        return self.model

    def fit_data(self):
        if not self.model.input_model.population:
            self.notify(Event.NO_POPULATION)
            return

        param = self.get_model_parameters_combo_box()
        file_content = self.model.input_model.file_content
        x_data = np.array(file_content[self.current_date_col], dtype=float)
        y_data = np.array(file_content[self.current_data_col], dtype=float)
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
        self.update_group_boxes(fitted_data[1])
        self.controller_service.redirect(Event.PLOT)

    def update_group_boxes(self, parameters):
        group_box = self.get_current_model_group_box()
        if group_box.isEnabled():
            return
        spin_boxes_count = 0
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                widget.setValue(parameters[spin_boxes_count])
                spin_boxes_count += 1

    def set_date_col(self, value):
        self.current_date_col = str(value)

    def set_data_col(self, value):
        self.current_data_col = str(value)

    def get_plot_data(self):
        return self.model.plot_model.get_data()

    def get_file_header(self):
        return self.model.input_model.file_content.keys()

    def get_file_values(self):
        return self.model.input_model.file_values

    def set_input_file(self, file_name):
        self.model.input_model.file_name = file_name
        file_content = csvmanager.read(file_name)
        self.model.input_model.file_content = file_content
        self.notify(Event.SET_FILE_CONTENT)
        self.notify(Event.ENABLE_COL_DATE_FORMAT)
        self.notify(Event.ENABLE_OPTIONS)

    def clear_input(self):
        self.model.input_model.file_name = None
        self.model.input_model.file_content = None
        self.model.input_model.population = None
        self.notify(Event.CLEAR_INPUT)

    def reset_data(self):
        self.clear_input()
        self.notify(Event.DISABLE_OPTIONS)

    def format_date(self):
        dates = self.model.input_model.file_content[self.current_date_col]
        dates = dateconverter.convert(dates)
        if len(dates) == 0:
            self.notify(Event.SHOW_CANT_CONVERT_DATES)
        else:
            self.model.input_model.file_content[self.current_date_col] = dates

    def set_optimize(self, value):
        if self.current_model_group_box:
            if value:
                self.notify(Event.DISABLE_PARAMETERS)
            else:
                self.notify(Event.ENABLE_PARAMETERS)

    def get_input_file(self):
        return self.model.input_model.file_name
